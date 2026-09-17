#!/usr/bin/env python3
"""Check the bundled token subset; not a DOM/CSS parser or WCAG certification."""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path

TOKEN_DIR = Path(__file__).resolve().parents[1] / "assets" / "tokens"
DECL = re.compile(r"(--kudu-[\w-]+)\s*:\s*([^;{}]+);")
REF = re.compile(r"var\(\s*(--kudu-[\w-]+)")
HEX = re.compile(r"#[0-9a-fA-F]{6}\Z")

def read_tokens(directory: Path = TOKEN_DIR) -> dict[str, str]:
    tokens: dict[str, str] = {}
    for path in sorted(directory.glob("*.css")):
        text = re.sub(r"/\*.*?\*/", "", path.read_text(encoding="utf-8"), flags=re.S)
        for name, value in DECL.findall(text):
            if name in tokens:
                raise ValueError(f"Duplicate token definition: {name}")
            tokens[name] = value.strip()
    if not tokens:
        raise ValueError("No token declarations found")
    done: set[str] = set()
    def visit(name: str, trail: set[str]) -> None:
        if name not in tokens:
            raise ValueError(f"Undefined token: {name}")
        if name in trail:
            raise ValueError(f"Cyclic token reference: {name}")
        if name in done:
            return
        for ref in REF.findall(tokens[name]):
            visit(ref, trail | {name})
        done.add(name)
    for name in tokens:
        visit(name, set())
    return tokens

def resolve_color(name: str, tokens: dict[str, str]) -> str:
    seen: set[str] = set()
    while name.startswith("--"):
        if name in seen or name not in tokens:
            raise ValueError(f"Missing or cyclic color token: {name}")
        seen.add(name)
        value = tokens[name]
        alias = re.fullmatch(r"var\(\s*(--kudu-[\w-]+)\s*\)", value)
        name = alias.group(1) if alias else value
    if not HEX.fullmatch(name):
        raise ValueError(f"Unsupported color format: {name}")
    return name.upper()

def luminance(value: str) -> float:
    if not HEX.fullmatch(value):
        raise ValueError("Expected opaque six-digit HEX")
    channels = [int(value[i:i+2], 16) / 255 for i in (1, 3, 5)]
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return sum(c * w for c, w in zip(linear, (0.2126, 0.7152, 0.0722)))

def contrast(foreground: str, background: str) -> float:
    a, b = sorted((luminance(foreground), luminance(background)))
    return (b + 0.05) / (a + 0.05)

def report(tokens: dict[str, str]) -> list[dict[str, object]]:
    checks = []
    for text in ("primary", "secondary", "muted"):
        for surface in ("primary", "app", "subtle"):
            checks.append((f"text-{text} on surface-{surface}", f"--kudu-text-{text}", f"--kudu-surface-{surface}", 4.5, "normal-text"))
    checks.append(("primary action on primary surface", "--kudu-action-primary", "--kudu-surface-primary", 4.5, "normal-text"))
    checks.append(("primary action on soft state", "--kudu-action-primary", "--kudu-action-primary-soft", 4.5, "normal-text"))
    for border in ("subtle", "default"):
        checks.append((f"border-{border} as essential boundary on white", f"--kudu-border-{border}", "--kudu-surface-primary", 3.0, "conditional-control-risk"))
    results = []
    for label, fg, bg, minimum, kind in checks:
        ratio = contrast(resolve_color(fg, tokens), resolve_color(bg, tokens))
        results.append({"check": label, "kind": kind, "ratio": ratio, "minimum": minimum, "passes": ratio >= minimum})
    return results

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="Fail for any listed draft contrast risk")
    parser.add_argument("--json", action="store_true", help="Print machine-readable results")
    args = parser.parse_args(argv)
    try:
        tokens = read_tokens()
        results = report(tokens)
    except (OSError, ValueError) as exc:
        print(f"Token validation error: {exc}", file=sys.stderr)
        return 2
    risks = [r for r in results if not r["passes"]]
    if args.json:
        print(json.dumps({"token_count": len(tokens), "checks": results, "risk_count": len(risks), "scope": "Selected flat color pairs only; not live accessibility conformance"}, indent=2))
    else:
        print(f"Resolved {len(tokens)} tokens; selected opaque sRGB pairs:")
        for r in results:
            state = "PASS" if r["passes"] else "REVIEW"
            print(f"{state:6} {r['check']}: {r['ratio']:.2f}:1 (target {r['minimum']}:1)")
        print(f"{len(risks)} draft risks. Border checks apply only when essential for identification.")
        print("No browser, screen-reader, font, opacity, or full WCAG validation is performed.")
    return 1 if args.strict and risks else 0

if __name__ == "__main__":
    raise SystemExit(main())
