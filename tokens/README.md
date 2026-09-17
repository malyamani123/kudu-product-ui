# Draft design tokens

Import [index.css](index.css) to access the canonical CSS variables. Their definitions live in the [portable skill assets](../.agents/skills/kudu-product-ui/assets/tokens/README.md).

These variables are a draft implementation of the agreed direction. They are not a finalized accessible palette. Read the known issues before using them. Do not use `--kudu-text-muted` as normal active text until its contrast is resolved. Status semantic colors and overlay shadows are not silently invented in this version.

Raw palette definitions belong in the token files. Product-level CSS should consume semantic tokens. Keep all relative imports together when relocating token files; do not copy only this wrapper.
