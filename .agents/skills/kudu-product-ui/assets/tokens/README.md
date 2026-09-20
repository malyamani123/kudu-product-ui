# Draft token assets

Import `index.css` to load the available custom properties. No component styling,
font loading, native control behavior, or package import is implemented here.

The values preserve the planning draft, including known contrast concerns.
Do not use muted text `#8A9099` for meaningful normal text on these light surfaces
without an approved readable replacement. Quiet border/fill combinations need
review when they are essential to identifying an input. The distinction matters:
not every decorative divider is an accessibility failure.

Run `python3 ../../scripts/check_tokens.py` from this directory, or use the full
script path from any working directory. `--strict` returns nonzero for the listed
risks. Default mode reports them without representing the palette as compliant.

`pending.json` records deferred roles; it is not runtime CSS. `breakpoints.json`
records draft boundaries for the eventual build system. Font families are names
only; no font binaries are bundled. Apply logical layout, accessible control
behavior, and reduced-motion handling in the actual implementation.

See [architecture](../../references/05-tokens-and-architecture.md) and
[open decisions](../../references/open-decisions.md). The canonical source is
this directory; the repository-level `tokens/index.css` only imports it.
