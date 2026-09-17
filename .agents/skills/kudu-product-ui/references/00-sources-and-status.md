# Sources, authority, and release status

## Status

`0.1.0-draft.1` packages the approved product direction and the planning material. It does not declare a corporate design standard formally ratified by KUDU, a completed implementation, or tested accessibility conformance. The request owner approved the direction in the planning conversation; technical values explicitly left for testing remain provisional.

## Source layers

| Layer | Source | Authority |
| --- | --- | --- |
| Brand | User-supplied `KUDU-FV02BGuideline_LR.pdf`, titled KUDU Brand Guidelines, 2026 Full Version 02, 59 pages | Report only what the document states; do not invent new official assets |
| Product choices | Completed user interview, D01-D45 | Approved product direction |
| Additional prohibition | User's card screenshot and explicit rejection of colored edge lines | X01, mandatory in KUDU product UI |
| Implementation values | Later Parts 1-8 in the planning conversation | Draft where values were explicitly proposed or deferred |
| Packaging | This repository's portable skill and helper scripts | Implementation organization, not a new design choice |
| Technical references | Official tool and W3C documentation linked below | External implementation context, not brand evidence |

## Brand document map

| Topic | PDF pages | Source-supported facts |
| --- | --- | --- |
| Purpose | 4 | Consistent recognition with room for creative expression |
| Logo versions | 9 | Flat version for communications/documentation; 3D version for branch facade signage |
| Logo variants | 10-11 | Primary vertical and secondary horizontal/language variants |
| Clear space | 12 | Minimum clear space equals the height of the letter K |
| Minimum printed size | 13 | 15 mm constraints by illustrated dimension; this is not a tested CSS-pixel rule |
| Color variants/backgrounds | 14-15 | Use the appropriate approved logo version on each background |
| Palette | 18 | Blue `#27468B`; yellow `#FDB515`; turquoise `#4DB8B6`; coral `#FF7354`; peach `#FFD4B3`; grey `#D8D7D6` |
| Gradients | 19 | Gradients are allowed in the brand document; the product system separately rejects them as a default UI treatment |
| Typography | 20-21 | Config Rounded Medium/Bold; DIN Next Arabic Medium/Bold; accent Baretelly Signature Script |
| Food/lifestyle photography | 22-23 | Product-focused food imagery and natural, warm, unstaged lifestyle direction |
| Graphic devices | 24 | Approved solid and stroke motifs contribute to brand recognition |
| Digital look and feel | 43-45 | Email, presentation, and website references use approved patterns, colors, and logo formats |

Preserve the printed HEX strings verbatim. Page 18 contains RGB/HEX inconsistencies, including the blue and grey entries. Do not silently normalize either representation or infer an updated corporate value. This draft uses the HEX choices already approved in the conversation; the brand owner should resolve the discrepancies before final publication.

The file describes brand applications, not a component library. Warm off-white surfaces, outline primary buttons, modal behavior, and icon rules are product decisions, not direct PDF requirements. The typography specification is not proof that the logo lettering is a commercially available font.

## Asset handling

The original PDF, fonts, production screenshots, and operational data are intentionally absent. Request approved logo/vector and photography assets through internal channels. Do not extract or redistribute embedded fonts. Do not invent a font license, a product data source, or a brand permission.

## External implementation references

Checked 2026-09-17. These support tooling and technical implementation only:

- Codex skill discovery: https://developers.openai.com/codex/skills/
- Codex project instructions: https://developers.openai.com/codex/guides/agents-md/
- Cursor skills: https://cursor.com/docs/skills
- Cursor project rules: https://cursor.com/docs/rules
- Claude Code skills: https://code.claude.com/docs/en/skills
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- Text contrast: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- Non-text contrast: https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
- Dialog interaction guidance: https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/

The user chose a WCAG AA target without naming a version. This draft proposes WCAG 2.2 AA as the specific implementation baseline; record that refinement for owner review rather than claiming it was an explicit original selection.
