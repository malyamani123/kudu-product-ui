# Approved product decision register

D01-D45 preserve the completed interview. X01 is an additional user decision. Exact implementation values that were later described as draft remain draft; see [open decisions](open-decisions.md).

| ID | Topic | Agreed direction | Operational interpretation |
| --- | --- | --- | --- |
| D01 | Personality | Simple + Friendly/Warm + Operational/Practical | Help employees understand and complete work; avoid showmanship |
| D02 | Density | Balanced | Comfortable without wasted space; adapt within a shared scale |
| D03 | Brand presence | Subtle | Recognition through consistent details, not saturated page coverage |
| D04 | Shape | Soft/Rounded | Friendly but controlled; not pill-shaped everything |
| D05 | Depth | Flat/Clean | No default shadows; only justified floating-layer separation |
| D06 | Base surface | Warm Off-White | Quiet warm app background and light working surfaces |
| D07 | Yellow | Accent Only | Restrained signature details; not primary buttons or large blocks |
| D08 | Blue | Structural Brand Color | Meaningful actions, navigation details, focus, and hierarchy; no coverage quota |
| D09 | Sidebar appearance | Light Sidebar + Blue Details | Apply when a sidebar is actually appropriate |
| D10 | Icons | Simple Outline | One consistent family; library not chosen yet |
| D11 | Rounding amount | Medium, approximately 10-12 px | Controlled per-role scale; later exact modal values remain draft |
| D12 | Cards | Minimal Cards | Use only for a genuine independent information unit |
| D13 | Section separation | Whitespace + Light Dividers + Selective Soft Surface Blocks | Space first; lines and surfaces where functionally useful |
| D14 | Tables | Structured Table | Clear headers, light row dividers, restrained hover, consistent alignment |
| D15 | Inputs | Soft Filled | Light neutral fill, permanent labels, visible focus |
| D16 | Primary button | Blue Outline | Preserve the choice; validate prominence against secondary fill |
| D17 | Secondary button | Neutral Filled | Very quiet fill so it does not outrank primary |
| D18 | Destructive button | Red Filled | Reserve for genuinely destructive or negative high-impact actions |
| D19 | Status | Soft Badges | Subtle surface and readable state text; semantic colors remain unresolved |
| D20 | Messages | Mixed, Toast First | Temporary success via toast; persistent problems inline |
| D21 | Create/Edit | Modal First | Short/medium tasks; complex multi-stage work may need a page |
| D22 | Upload | Mixed | Drop zone for core upload workflow; button for secondary upload |
| D23 | Search/Filters | Search visible + Filters button | Active count, removable selections, Clear all |
| D24 | Row actions | Important Action + Kebab | One useful labeled action, remaining actions in overflow |
| D25 | Bulk actions | Only when needed + Contextual Action Bar | No default checkboxes on every table; count and clear-selection controls |
| D26 | Empty states | Very Minimal | Simple outline icon, clear title, short explanation, relevant action |
| D27 | Loading | Mixed | Skeletons for known content; spinner for short actions; meaningful status for longer work |
| D28 | Page header | Simple Header | Title, optional one-line description, primary action; breadcrumbs only for meaningful hierarchy |
| D29 | Modal action order | Language-Aware | Respect RTL/LTR; exact implementation ordering requires testing |
| D30 | Modal sizing | Hybrid | Standard width roles; content-based height capped by viewport |
| D31 | Confirmation | Destructive + High-Impact Only | Avoid confirmation for routine edits; explain actual consequences |
| D32 | Validation | Inline + Top Summary | Field messages; summary for longer/multi-error forms |
| D33 | Required fields | Asterisk | Visible mark plus programmatic required state |
| D34 | Labels | Minimal Labels | Permanent label; helper copy only when needed; placeholder not a substitute |
| D35 | Form layout | Adaptive | Single column by default; two for short/logically related fields |
| D36 | Long forms | Depends on complexity | Sections first; accordion/tabs only when justified; actual stages become a flow |
| D37 | Multi-step flow | Adaptive | Horizontal for roughly 3-5 clear stages; vertical when longer/complex; compact progress for constrained space |
| D38 | Dashboard/Home | Depends on product | Operational/KPI/navigation home only when useful; allow no dashboard |
| D39 | Detail pages | Adaptive | Essential summary first; single page or meaningful independent tabs |
| D40 | Content width | Adaptive | Limited reading/form width; wider data/drawing workspace; mixed sections can differ |
| D41 | Navigation architecture | Adaptive | Sidebar, top, hybrid, minimal, or none according to actual task |
| D42 | Responsive | From the start | Define desktop, tablet, and mobile behavior with every relevant component |
| D43 | Accessibility | WCAG AA as a target | Requirement from the start, not a claim of tested conformance |
| D44 | Motion | Soft Motion | Short, calm, functional transitions; reduced-motion behavior |
| D45 | Governance | Strict Foundations + Flexible Composition | Reuse the language; adapt layouts; do not silently redefine the system |
| D46 | Product typography | Nunito for English; Tajawal for Arabic | Use Medium/Bold weights for product UI; this owner clarification supersedes the earlier planning-font selection |
| D47 | Logo variants | Owner-supplied vertical and horizontal Arabic/English PNG artwork | Use the bundled artwork without recreation or distortion; request a source vector only when a product requires one |
| D48 | Application icon | Owner-specified 32 × 32 inverted yellow triangle | Use the exact SVG at `src/app/icon.svg` when that application path is used; retain `#F4B21B` fill and the supplied triangle geometry |
| X01 | Colored side accent strips | Prohibited | No decorative/status-colored left or right strips on cards, panels, alerts, or navigation items, including pseudo-element substitutes |

## Interpretive notes

Blue being structural does not contradict a light sidebar or outline primary buttons: structural describes the role of the color, not an obligation to paint large surfaces blue. A sidebar appearance choice does not require a sidebar in every product.

X01 does not remove full-perimeter keyboard focus outlines, ordinary neutral table dividers, or meaningful workflow connectors. Do not use those exceptions to recreate a decorative side strip. New visual exceptions need explicit owner approval.

The 3-5-step rule is a planning heuristic, not a reason to invent unnecessary steps. An asynchronous operation can show progress without being represented as a separate screen.

The completed interview must not be repeated for every product. Ask only for missing product-specific requirements or necessary assets.
