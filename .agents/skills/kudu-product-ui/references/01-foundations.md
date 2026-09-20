# Part 1: Design principles and foundations

## Contents

1. Purpose and personality
2. Brand foundations
3. Surfaces and typography
4. Geometry, depth, and iconography
5. Behavior and flexibility

## 1. Purpose and personality

Build a common family of KUDU internal products, not an AP system, customer restaurant app, or single reusable page template. Support Intranet, Engineering, Supply Chain, Finance, HR, Operations, administration, and AI-assisted work.

The approved personality is **Simple + Friendly/Warm + Operational/Practical**. Use balanced density, subtle branding, flat/clean treatment, responsive composition, and restrained soft rounding. Help the employee work first; express the brand without competing with content.

Simplicity does not mean removing necessary data, accessibility information, or useful actions. Warmth comes from typography, calm surfaces, clear language, and comfortable spacing, not mascots or decoration. Different product needs justify different compositions.

## 2. Brand foundations

Source: [brand map](00-sources-and-status.md), PDF p.18 and the request owner's later typography clarification.

| Brand primitive | Official printed HEX | Product usage |
| --- | --- | --- |
| Blue | `#27468B` | Structural action/navigation/focus language |
| Yellow | `#FDB515` | Small brand accent only |
| Turquoise | `#4DB8B6` | Supporting brand asset, not automatic success color |
| Coral | `#FF7354` | Supporting brand asset, not automatic error color |
| Peach | `#FFD4B3` | Supporting brand asset, not a default panel fill |
| Grey | `#D8D7D6` | Brand reference, distinct from product-neutral palette |

Keep blue meaningful rather than universal: primary button border/text, active navigation, important links, and focus. Do not make every body paragraph blue or create a full-blue sidebar by default. Yellow is not a success indicator, default CTA fill, or repeated large background.

Use approved logo files and respect clear space equivalent to the letter K height (PDF p.12). Do not convert the printed 15 mm minimum to an assumed digital limit; test the actual approved logo at the chosen display size. Use the flat variant for UI; do not imitate facade signage effects.

The brand guide allows gradients and patterns (pp.19,24). The product system separately chooses flat UI and exceptional use of graphic devices. These are deliberate product restrictions, not claims that the source prohibits gradients.

## 3. Surfaces and typography

| Draft role | Value | Notes |
| --- | --- | --- |
| App | `#F7F6F2` | Warm off-white, not a beige theme |
| Primary surface | `#FFFFFF` | Working content |
| Subtle surface | `#F2F1ED` | Selected functional regions/quiet controls |
| Subtle border | `#E2E1DC` | Separators, not guaranteed sufficient for essential control identification |
| Primary text | `#20242A` | Body content |
| Secondary text | `#667085` | Supporting text; test against actual surface |
| Muted text | `#8A9099` | Preserved draft value; known normal-text contrast concern |

Do not treat these draft numbers as approved accessible combinations. Read [open decisions](open-decisions.md) and run the token diagnostics. Use a verified text token for meaningful metadata and placeholders; do not hide important information in low-contrast grey.

Use **Poppins Medium/Bold** for English and **Tajawal Medium/Bold** for Arabic. Do not use an accent script as a normal application UI face. Font files are not included in this repository and must be provisioned through the approved product asset path. Ordinary text saying KUDU is not an official logo asset.

Draft hierarchy: page title 28 px; section title 20 px; component title 16 px; body 14-16 px; controls/tables 14 px; captions 12 px. Use a 16 px body option for reading-oriented content. Draft line heights are 1.25, 1.5, and 1.65; verify Arabic with the actual font rather than assuming English measurements work.

## 4. Geometry, depth, and iconography

Use a 4 px spacing base: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64. Choose spacing by relationship and content; do not apply large panel padding to every control. Whitespace is the first separator, then light dividers, then selective surfaces.

Draft radius roles: small 6 px; control 10 px; panel 12 px; modal 14 px. Pill radius is limited to suitable badges/chips, not all controls. These refine the approved approximate 10-12 px rounded direction; visual validation is pending.

Default shadow is none. Floating menus and dialogs may need subtle depth, but exact shadow values are unresolved. No glassmorphism, glow, neumorphism, heavy elevation, or floating dashboard-card styling.

Cards must represent genuinely independent information units. Do not wrap page headers, filters, tables, and every section automatically. Avoid nested cards.

**X01: colored vertical/side accent strips are prohibited.** This applies to cards, panels, alerts, and navigation items. Do not reproduce the motif with pseudo-elements, background gradients, or inset shadows.

Use one simple outline icon family, consistent stroke treatment, and 16/20/24 px icon sizes. The family is not chosen yet. Default icons are neutral; important/active icons may be blue. Do not mix filled, 3D, emoji, and outline styles. Neutral symbols such as search do not flip in RTL; directional symbols are evaluated individually.

## 5. Behavior and flexibility

Soft motion communicates change, not personality through spectacle. Draft durations: 120/180/240 ms with standard easing. Honor reduced-motion preferences. Do not make focus depend on an animation completing.

Responsive and accessibility requirements apply from the start. Reading, forms, tables, project drawings, and mixed pages need different widths and mobile strategies. Do not simply shrink desktop layouts.

Keep brand, tokens, controls, states, and interaction conventions strict. Keep information architecture, navigation choice, dashboard need, workflow, content order, charts, and page composition product-specific. The same family must support a content-led Intranet and a project-led Engineering product without making either look like a generic finance dashboard.
