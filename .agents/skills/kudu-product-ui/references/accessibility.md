# Accessibility implementation reference

## Authority and scope

D43 sets WCAG AA as the target. WCAG 2.2 AA is a proposed implementation version, not a claim that the user named that version. The technical details below come from external W3C guidance; they are not requirements printed in the brand PDF. No live component has been certified by this repository.

## Baseline checks

| Area | Implementation check | Reference |
| --- | --- | --- |
| Normal text | At least 4.5:1 contrast against its actual background | WCAG 1.4.3 |
| Large text | At least 3:1 where the WCAG large-text definition actually applies | WCAG 1.4.3 |
| Essential non-text UI | At least 3:1 for visual information needed to identify controls/states against adjacent colors, subject to the criterion's exceptions | WCAG 1.4.11 |
| Color meaning | Include text or other non-color information | WCAG 1.4.1 |
| Keyboard | Operate controls without requiring pointer input; avoid traps | WCAG 2.1.1, 2.1.2 |
| Focus | Visible keyboard focus and not entirely obscured by author-created content | WCAG 2.4.7, 2.4.11 |
| Targets | Evaluate the 24 by 24 CSS-pixel minimum or its defined spacing/exceptions | WCAG 2.5.8 |
| Reflow | Check narrow equivalent viewport/zoom where the criterion applies; preserve necessary two-dimensional content appropriately | WCAG 1.4.10 |
| Forms | Labels/instructions, textual error identification, meaningful programmatic name/role/value | WCAG 3.3.1, 3.3.2, 4.1.2 |
| Status feedback | Announce relevant status changes without forcing focus | WCAG 4.1.3 |

A 16 px icon may sit inside a larger target. A 40 px button does not automatically satisfy every spacing or mobile usability need. The 44 px control option is a design choice, not the general AA threshold. Full WCAG 2.2 AA assessment includes all applicable A and AA criteria, not only this table.

## Dialog implementation

Follow the WAI-ARIA Authoring Practices dialog pattern as interaction guidance: accessible name, appropriate dialog semantics, deliberate initial focus, contained keyboard navigation, background inactivity, appropriate dismissal, and focus return. Complex destructive dialogs need careful initial-focus selection. Avoid stacking modals. Using `aria-modal` alone does not implement these behaviors.

## Color diagnostics and unresolved tokens

The draft preserves `#8A9099` muted text and quiet border/fill values from the planning conversation. The checker intentionally exposes their contrast risks; it does not silently change approved material. Do not use them for meaningful normal text or essential control identification without validated replacements. Propose and review replacements before production.

Check all real states, including hover, selected, disabled where applicable, errors, badges, overlays, and alternate surfaces. Alpha blending, backgrounds, actual font sizes/weights, and component shapes affect the result. A flat HEX calculation is not a screen audit.

## Language and motion

Use real language tags, logical DOM order, and appropriate direction for Arabic/English content. RTL support is a separate product requirement; it is not synonymous with WCAG compliance. Respect reduced-motion preferences as an explicit system requirement and evaluate other applicable motion criteria. Do not label every reduced-motion preference as an AA criterion.

## Primary sources

- Normative WCAG 2.2: https://www.w3.org/TR/WCAG22/
- Contrast: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- Non-text contrast: https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
- Focus not obscured: https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html
- Target size: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- Modal dialogs: https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/

Verify with the actual rendered application and document methods and limitations. Automated checks alone do not establish complete conformance.
