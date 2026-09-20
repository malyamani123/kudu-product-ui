"""Local tooling tests; these are not browser or agent-behavior tests."""
from __future__ import annotations
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from install_skill import install
from package_skill import package
from validate_repository import SKILL, validate

spec = importlib.util.spec_from_file_location('kudu_tokens', SKILL / 'scripts/check_tokens.py')
assert spec is not None and spec.loader is not None
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)

class ToolingTests(unittest.TestCase):
    def test_repository_integrity(self):
        self.assertEqual(validate(), [])

    def test_black_white_reference(self):
        self.assertAlmostEqual(checker.contrast('#000000', '#FFFFFF'), 21.0)
        self.assertAlmostEqual(checker.contrast('#FFFFFF', '#FFFFFF'), 1.0)

    def test_brand_alias(self):
        tokens = checker.read_tokens()
        self.assertEqual(checker.resolve_color('--kudu-action-primary', tokens), '#27468B')
        self.assertEqual(checker.resolve_color('--kudu-accent-brand', tokens), '#FDB515')

    def test_draft_contrast_is_not_silently_passed(self):
        results = checker.report(checker.read_tokens())
        muted = [row for row in results if row['check'].startswith('text-muted')]
        self.assertEqual(len(muted), 3)
        self.assertTrue(all(not row['passes'] for row in muted))

    def test_undefined_token_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory)
            (p / 'test.css').write_text(':root { --kudu-a: var(--kudu-missing); }')
            with self.assertRaises(ValueError):
                checker.read_tokens(p)

    def test_cycle_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory)
            (p / 'test.css').write_text(':root { --kudu-a: var(--kudu-b); --kudu-b: var(--kudu-a); }')
            with self.assertRaises(ValueError):
                checker.read_tokens(p)

    def test_duplicate_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory)
            (p / 'test.css').write_text(':root { --kudu-a: #FFFFFF; --kudu-a: #000000; }')
            with self.assertRaises(ValueError):
                checker.read_tokens(p)

    def test_strict_mode_reports_risks(self):
        result = subprocess.run([sys.executable, str(SKILL / 'scripts/check_tokens.py'), '--strict', '--json'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertGreater(json.loads(result.stdout)['risk_count'], 0)

    def test_install_dry_run(self):
        with tempfile.TemporaryDirectory() as directory:
            target = install(Path(directory), 'cursor', dry_run=True)
            self.assertFalse(target.exists())
            self.assertIn('.agents', str(target))

    def test_install_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            marker = project / 'application.txt'
            marker.write_text('preserve')
            target = install(project, 'claude')
            self.assertTrue((target / 'SKILL.md').is_file())
            with self.assertRaises(FileExistsError):
                install(project, 'claude')
            self.assertEqual(marker.read_text(), 'preserve')

    def test_package_is_portable_and_reproducible(self):
        with tempfile.TemporaryDirectory() as directory:
            target = package(Path(directory))
            first = target.read_bytes()
            with zipfile.ZipFile(target) as archive:
                self.assertIsNone(archive.testzip())
                entries = archive.namelist()
                self.assertEqual(sum(name.endswith('/SKILL.md') for name in entries), 1)
                self.assertIn('kudu-product-ui/references/decisions.md', entries)
                self.assertIn('kudu-product-ui/assets/logos/kudu-logo-horizontal.png', entries)
                self.assertIn('kudu-product-ui/assets/logos/kudu-logo-vertical.png', entries)
                self.assertIn('kudu-product-ui/assets/logos/kudu-favicon.svg', entries)
                self.assertFalse(any(name.endswith(('.ttf', '.woff', '.pdf')) for name in entries))
            self.assertEqual(package(Path(directory)).read_bytes(), first)

if __name__ == '__main__':
    unittest.main()
