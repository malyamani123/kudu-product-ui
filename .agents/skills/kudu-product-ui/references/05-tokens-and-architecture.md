# Part 5: Design tokens and implementation architecture

## Contents

1. Token layers and ownership
2. Available draft values
3. Unresolved values and limitations
4. Implementation and distribution

## 1. Token layers and ownership

Use primitive -> semantic -> component tokens. A primitive records an underlying value; a semantic token records its role; a component consumes that role. Blue is an official primitive, while a primary action is a product role. Do not use brand primitives arbitrarily in application screens.

The canonical CSS is in `assets/tokens/` relative to the skill directory. The repository's top-level `tokens/index.css` is a convenience import; it is not a second editable palette. Keep documentation, decisions, and technical values synchronized. Do not treat an unresolved token as approved merely because a CSS variable can be declared.

## 2. Available draft values

The bundle preserves values from the planning conversation, rather than silently replacing them during packaging.

| Area | Draft values or roles |
| --- | --- |
| Brand | Six printed HEX values from the brand guide |
| Neutral | 0, 25, 50, 100, 200, 300, 500, 600, 800, 900 |
| Surfaces | app, primary, subtle, hover, selected, disabled |
| Text | primary, secondary, muted, brand, on-brand |
| Borders | subtle, default, brand |
| Actions | primary, primary-hover, primary-soft, secondary, secondary-hover, disabled |
| Typography | approved font names, Medium/Bold, role sizes, three line heights |
| Spacing | 4, 8, 12, 16, 20, 24, 32, 40, 48, 64 px |
| Radius | small 6, control 10, panel 12, modal 14 px; pill only for suitable badges/chips |
| Controls | small 32, medium 40, large 44 px; use min-height where content must grow |
| Icons | 16, 20, 24 px; clickable targets are a separate requirement |
| Content widths | reading 760, form 840, standard 1200, wide 1440 px; adapt to content |
| Motion | 120, 180, 240 ms; standard easing; reduced-motion behavior |
| Layers | base 0, sticky 100, dropdown 200, overlay 300, modal 400, toast 500 |
| Breakpoints | initial boundaries at 640, 1024, 1440 px |

The simple layer scale does not solve every portal/stacking-context problem. A menu opened inside a dialog must remain in an appropriate dialog layer; do not blindly portal it beneath an overlay because its global token is lower. Dialog implementation and stacking require browser tests.

CSS custom properties cannot simply be substituted into ordinary media-query conditions. `breakpoints.json` stores the draft boundaries; use them through the chosen build system or documented literal media queries. Do not claim variables in `:root` make all responsive queries work automatically.

## 3. Unresolved values and limitations

The original muted grey `#8A9099` is preserved for traceability but is not a safe default for normal readable text on the draft light backgrounds. Similarly, subtle/default neutral borders and soft fills may not identify essential input boundaries strongly enough. Run the bundled checker; do not deploy these combinations as accessibility-approved.

Semantic success/warning/error/info values, destructive button colors, pressed surfaces, overlay scrim/shadows, modal widths, final icon library, font-file provisioning, and Arabic metric refinements remain open. `pending.json` lists roles without inventing production values. No runtime token intentionally references one of these undefined roles.

Do not use the yellow accent as small text on a light surface. Semantic status meaning is independent of the brand palette. A computed color-pair pass is only evidence about that pair, not about gradients, opacity, actual DOM, icon shapes, typography, or overall conformance.

## 4. Implementation and distribution

Use the existing project's framework and dependencies. React examples in the planning material specify desired APIs only; the repository does not ship a production React library or installable `@kudu/ui` package.

Suggested future variants: Button primary/secondary/destructive/ghost; StatusBadge success/warning/error/info/neutral. Inputs own labels, required/error associations, and state styling. Tables enable search/filter/selection only where the product requires them. Navigation composition remains adaptive.

Start with tokens and representative core controls, then three distinct product pilots. Finalize tested values before publishing a shared package. Keep product layout local; avoid project-level rebranding and parallel button libraries. Integration does not update other projects automatically: pin a revision, review changes, and intentionally adopt releases.

Read [responsive and RTL](responsive-rtl.md) for logical layout and mixed-direction content. Read [build plan](08-build-plan.md) before turning a specification into a production library.
