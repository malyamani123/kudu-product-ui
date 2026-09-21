# Part 4: Do/Don't and AI design contract

## Contents

1. Contract
2. Boundaries
3. Do/Don't rules
4. Execution and completion

## 1. Contract

Design within the established KUDU Product UI language. Solve the user's workflow clearly; express the brand subtly. Do not redesign KUDU or substitute a generic SaaS, marketing, or AI aesthetic. Apply the system to all KUDU product domains, not just AP.

A design instruction is not automatic enforcement. Inspect actual code and screenshots, run available tests, and report limitations. Never promise that a skill alone guarantees a unique or accessible UI.

## 2. Boundaries

| Fixed unless explicitly approved | Flexible with task-based justification |
| --- | --- |
| Brand HEX choices and approved font families | Page composition and information hierarchy |
| Control variants and state language | Sidebar/top/hybrid/minimal navigation |
| Spacing/radius vocabulary and simple outline icons | Column selection, content grouping, workflow structure |
| Minimal cards and no colored side strips | Meaningful tabs/sections, document previews, charts |
| Accessibility, responsive, and bidirectional requirements | Density application within agreed limits |

An unresolved value is not permission to invent an official rule. Record a compatible proposal and explain its status. Follow the source/status map where discussions contain provisional values or unresolved conflicts.

## 3. Do/Don't rules

| Area | Do | Do not |
| --- | --- | --- |
| Brand | Use approved blue, restrained yellow, correct logo assets | Paint the workspace blue/yellow; recreate the logo; change the font to a template default |
| Color | Use semantic roles and verify actual foreground/background pairs | Assign random colors to modules; equate brand coral/turquoise with error/success |
| Typography | Use a small role hierarchy and licensed approved fonts | Oversized operational headings; uppercase everything; per-project typefaces |
| Layout | Prioritize task, data, readable hierarchy, whitespace | Mandatory dashboard, sidebar, hero, chart, quick-links card, or four KPIs |
| Cards | Group genuine independent units | Wrap every heading, filter, number, table, and section; nest card shells |
| Side strips | Use text, icons, soft state surfaces, meaningful hierarchy | Colored left/right accent borders, pseudo-element strips, inset-shadow substitutes on cards/panels/alerts/navigation |
| Buttons | Blue outline primary, quiet neutral secondary, red destructive | Yellow primary, gradients, huge pills, shadows, competing prominent actions |
| Forms | Permanent labels, required marks, relevant helper copy, clear errors | Placeholder-only labels; unnecessary help paragraphs; arbitrary style per field |
| Tables | Structured headers/rows, useful labeled row action plus overflow | Excess cell borders, many icons, lost data to achieve visual simplicity |
| Status | Soft readable badges with state text | Color-only meaning, rainbow status systems, colored edge strips |
| Navigation | Match the product; light sidebar when appropriate | Assume every product is a dashboard; full-blue default sidebar |
| Feedback | Toast for temporary confirmations; inline actionable problems | Important errors that disappear before they can be acted on |
| AI tools | Structure input, processing, review, result | Default chat, robots, glow, futuristic grids, purple gradients, decorative sparkles |
| Icons | One consistent simple outline family | Mixed filled/outline/emoji/3D styles or unexplained action icons |
| Motion | Short functional transitions with reduced-motion support | Bounce, decorative pulse, movement without purpose |
| Responsive | Adapt composition and preserve capability | Desktop-only implementation with a future mobile patch |
| Access | Keyboard, readable contrast, named controls, clear focus | Remove focus to look clean; call a partial check WCAG compliance |
| User-facing copy | Use clear wording, punctuation, labels, or whitespace to separate ideas | Use hyphens or dashes (`-`, `–`, `—`) as visual separators between words; retain them only in values that semantically require them, such as ranges, IDs, filenames, commands, or negative numbers |
| Content | Direct, helpful, professional, warm text | Vague error messages, exaggerated success claims, invented metrics |

The prohibition concerns purposeful product styling. A focus outline around a complete control remains required; neutral row separators and useful stage connectors are not banned side strips.

## 4. Execution and completion

Before a screen, identify product type, actual users, task/action, essential data, secondary information, navigation needs, stack constraints, and available assets. Read the existing implementation and reuse its compatible components.

When building, use known tokens and existing component APIs. Do not invent an import from `@kudu/ui` before that package exists. Do not restyle each screen with a new button or arbitrary radius. Do not add dependencies or rewrite architecture merely for appearance.

When auditing, point to visible evidence or exact files. Separate observation, impact, applicable rule, proposed repair, and verification. Protect existing features, access checks, data contracts, and unrelated changes.

For a missing component, try composition first. Propose the smallest extension when needed; use a documented exception for an actual conflict. Do not silently change approved foundations.

Before delivery, review primary action recognition, repeated visual language, unnecessary decoration, actual responsive/RTL behavior, and relevant accessibility/states. State tests executed and missing evidence. An unknown test is NOT TESTED, not PASS.

## Reusable request

```text
Use the KUDU Product UI skill for this product. Inspect the requirements and
existing implementation first. Preserve working behavior and use the approved
foundations, draft token vocabulary, component contracts, and relevant product
patterns. Keep composition specific to the user's task. Do not add a dashboard,
chat, chart, cards, or navigation model without a functional reason. Never use
colored side accent strips. Explain unresolved assets or tokens and validate
responsive, RTL/LTR, accessibility, and states before claiming completion.
```
