#!/usr/bin/env python3
"""Install a local skill snapshot without replacing existing project files."""
from __future__ import annotations
import argparse
import shutil
import sys
from pathlib import Path
from validate_repository import SKILL, check_skill

LOCATIONS = {'codex': '.agents', 'cursor': '.agents', 'claude': '.claude'}

def install(project: Path, tool: str, dry_run: bool = False, source: Path = SKILL) -> Path:
    project = project.expanduser().resolve()
    if not project.is_dir():
        raise ValueError('Project directory must already exist')
    if tool not in LOCATIONS:
        raise ValueError('Unsupported tool')
    errors = check_skill(source)
    if errors:
        raise ValueError('Invalid source skill: ' + '; '.join(errors))
    target = project / LOCATIONS[tool] / 'skills' / 'kudu-product-ui'
    if not target.parent.resolve().is_relative_to(project):
        raise ValueError('Destination parent resolves outside the project')
    if target.exists() or target.is_symlink():
        raise FileExistsError(f'Refusing to overwrite {target}; review the existing version first')
    if not dry_run:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, target, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    return target

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tool', choices=sorted(LOCATIONS), required=True)
    parser.add_argument('--project', type=Path, required=True)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    try:
        target = install(args.project, args.tool, args.dry_run)
    except (OSError, ValueError) as exc:
        print(f'Installation stopped: {exc}', file=sys.stderr)
        return 1
    print(('Would install: ' if args.dry_run else 'Installed: ') + str(target))
    print('Application files and existing agent rules were not changed.')
    print('This is a snapshot; future updates require an explicit review.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
