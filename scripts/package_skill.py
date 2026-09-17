#!/usr/bin/env python3
"""Build a reproducible, single-skill dist/skill.zip using the standard library."""
from __future__ import annotations
import argparse
import sys
import zipfile
from pathlib import Path
from validate_repository import ROOT, SKILL, check_skill, paths

MAX_BYTES = 25 * 1024 * 1024
ALLOWED = {'.md', '.yaml', '.css', '.json', '.py'}

def package(output: Path, source: Path = SKILL) -> Path:
    errors = check_skill(source)
    if errors:
        raise ValueError('; '.join(errors))
    source = source.resolve()
    output = output.expanduser().resolve()
    if output.is_relative_to(source):
        raise ValueError('Package output must be outside the skill source')
    output.mkdir(parents=True, exist_ok=True)
    target = output / 'skill.zip'
    stage = output / 'skill.zip.tmp'
    try:
        with zipfile.ZipFile(stage, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for path in paths(source):
                if path.is_symlink():
                    raise ValueError(f'Refusing symlink: {path}')
                if not path.is_file():
                    continue
                if path.suffix not in ALLOWED:
                    raise ValueError(f'Unexpected asset type: {path.name}')
                name = f'{source.name}/{path.relative_to(source).as_posix()}'
                info = zipfile.ZipInfo(name, date_time=(2026, 9, 17, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, path.read_bytes())
        if stage.stat().st_size > MAX_BYTES:
            raise ValueError('Skill archive exceeds the 25 MiB package limit')
        with zipfile.ZipFile(stage) as archive:
            if archive.testzip() is not None:
                raise ValueError('Archive integrity check failed')
        stage.replace(target)
        return target
    finally:
        stage.unlink(missing_ok=True)

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'dist')
    args = parser.parse_args()
    try:
        target = package(args.output)
    except (OSError, ValueError, zipfile.BadZipFile) as exc:
        print(f'Packaging stopped: {exc}', file=sys.stderr)
        return 1
    print(f'Created {target} ({target.stat().st_size:,} bytes)')
    print('Only the portable skill is included; no fonts, source PDF, or production data.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
