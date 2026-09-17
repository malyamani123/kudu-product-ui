#!/usr/bin/env python3
"""Validate this repository's structure/links; not product UI compliance."""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / '.agents' / 'skills' / 'kudu-product-ui'
IGNORE = {'.git', '__pycache__', 'dist', '.pytest_cache', '.venv'}
BLOCKED = {'.ttf', '.otf', '.woff', '.woff2', '.eot', '.pdf'}
LINK = re.compile(r'\[[^\]\n]+\]\(([^)\n]+)\)')

def paths(root: Path):
    for path in sorted(root.rglob('*')):
        if not any(part in IGNORE for part in path.relative_to(root).parts):
            yield path

def check_links(root: Path) -> list[str]:
    errors = []
    for path in paths(root):
        if not path.is_file() or path.suffix != '.md':
            continue
        text = re.sub(r'```.*?```', '', path.read_text(encoding='utf-8'), flags=re.S)
        for target in LINK.findall(text):
            target = target.split('#', 1)[0].strip()
            if not target or re.match(r'[a-zA-Z][\w+.-]*:', target):
                continue
            dest = (path.parent / unquote(target)).resolve()
            if not dest.is_relative_to(root.resolve()):
                errors.append(f'Link escapes validation root: {path.relative_to(root)} -> {target}')
            elif not dest.exists():
                errors.append(f'Broken link: {path.relative_to(root)} -> {target}')
    return errors

def check_skill(skill: Path) -> list[str]:
    errors = []
    entry = skill / 'SKILL.md'
    if not entry.is_file():
        return ['Missing SKILL.md']
    text = entry.read_text(encoding='utf-8')
    match = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
    if not match:
        return ['Missing frontmatter']
    fields = dict(re.findall(r'^(name|description):\s*(.+)$', match.group(1), re.M))
    if fields.get('name') != 'kudu-product-ui':
        errors.append('Unexpected skill name')
    if not 20 <= len(fields.get('description', '')) <= 1024:
        errors.append('Description missing or outside expected length')
    if len(text.splitlines()) >= 500:
        errors.append('SKILL.md should stay below 500 lines')
    if not (skill / 'agents/openai.yaml').is_file():
        errors.append('Missing agent metadata')
    for path in paths(skill):
        if path.is_symlink():
            errors.append(f'Symlink not portable: {path.relative_to(skill)}')
        if path.suffix.lower() in BLOCKED:
            errors.append(f'Restricted binary/source asset: {path.relative_to(skill)}')
        if path.name in {'example.py', 'api_reference.md', 'example_asset.txt'}:
            errors.append(f'Unremoved initialization sample: {path.relative_to(skill)}')
    errors.extend(check_links(skill))
    return errors

def validate(root: Path = ROOT) -> list[str]:
    skill = root / '.agents/skills/kudu-product-ui'
    errors = check_skill(skill)
    errors.extend(check_links(root))
    for path in paths(root):
        if not path.is_file():
            continue
        try:
            if path.suffix == '.json':
                json.loads(path.read_text(encoding='utf-8'))
            elif path.suffix == '.py':
                compile(path.read_text(encoding='utf-8'), str(path), 'exec')
            elif path.suffix == '.css':
                for target in re.findall(r'@import\s+"([^"]+)"', path.read_text(encoding='utf-8')):
                    if not (path.parent / target).is_file():
                        errors.append(f'Missing CSS import: {path} -> {target}')
        except (OSError, ValueError, SyntaxError) as exc:
            errors.append(f'{path.relative_to(root)}: {exc}')
    return sorted(set(errors))

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skill-only', action='store_true')
    args = parser.parse_args()
    errors = check_skill(SKILL) if args.skill_only else validate()
    for error in errors:
        print(f'FAIL: {error}')
    if errors:
        return 1
    print('PASS: structure, local links, and relevant syntax checks.')
    print('This does not validate visual design or accessibility conformance.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
