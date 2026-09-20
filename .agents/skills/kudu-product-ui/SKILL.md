---
name: kudu-product-ui
description: Design, implement, review, and refactor KUDU internal product interfaces using the approved KUDU Product UI direction. Use for KUDU Intranet, Engineering, Supply Chain, Finance, HR, Operations, administration, document workflows, or AI tools; for requests to apply KUDU identity, remove generic template styling, audit screens, choose page patterns, or add shared components. Accept product requirements, accessible repository files, screenshots, and design-system change proposals. Produce task-specific composition plans, code changes, review findings, or compatible component proposals while preserving existing behavior. Keep foundations strict and product composition flexible. Do not restrict the system to AP or treat it as a marketing, slide, or document-design skill.
---

# KUDU Product UI

Apply the established visual language; do not invent a new brand or force a shared page template. Keep output in English unless the user requests another language. Product UI must support English/LTR and Arabic/RTL as required by the product.

## Start with authority and scope

Read [sources and status](references/00-sources-and-status.md) and [foundations](references/01-foundations.md). Preserve the [decision register](references/decisions.md), including X01. Treat the release as `0.1.0-draft.1`, not a validated production component library. Check [open decisions](references/open-decisions.md) before selecting unapproved details.

Inspect the user's actual requirements, accessible files, framework, existing components, tests, and available assets. A path or repository name alone is not evidence of its contents. Read before editing; preserve working features, permissions, data contracts, and unrelated changes. Use only available authorized tools. Ask for a missing asset or project input only when essential; do not repeat the completed design interview.

Classify the task as **plan**, **build**, **audit**, **migrate**, or **extend**. Classify the product as content, operational, data-heavy, workflow, document-heavy, engineering/project, AI tool, administration, or a combination.

## Load only relevant references

| Need | Read |
| --- | --- |
| Controls and states | [Component specifications](references/02-components.md) |
| Navigation, layouts, product types | [Product patterns](references/03-product-patterns.md) |
| Non-negotiable rules and agent boundaries | [AI contract](references/04-ai-contract.md) |
| CSS variables and implementation architecture | [Tokens and architecture](references/05-tokens-and-architecture.md), [token assets](assets/tokens/README.md) |
| Test plans and evidence | [Validation](references/06-validation.md) |
| Changes, exceptions, migration, versioning | [Governance](references/07-governance.md) |
| Build sequence and release gates | [Build plan](references/08-build-plan.md) |
| Keyboard, contrast, forms, dialogs | [Accessibility](references/accessibility.md) |
| Small screens, bidirectionality, tables | [Responsive and RTL](references/responsive-rtl.md) |

## Apply the fixed language

- Keep the interface simple, warm, practical, balanced, subtly branded, flat, and clean.
- Use official brand HEX values: blue `#27468B`, yellow `#FDB515`. Use yellow only as a restrained accent. Do not treat supporting brand colors as status colors automatically.
- Use approved Poppins for English and Tajawal for Arabic, with Medium/Bold weights. Provision font files through the approved product asset path; do not extract, download, or redistribute font files through this skill. Do not recreate a KUDU logo as ordinary text. Use the approved [horizontal](assets/logos/kudu-logo-horizontal.png) logo in headers and wide placements, or the approved [vertical](assets/logos/kudu-logo-vertical.png) logo in tall or narrow placements. Disclose any temporary preview fallback.
- Use the approved [KUDU favicon](assets/logos/kudu-favicon.svg) when the product needs an application icon. Install the exact SVG at `src/app/icon.svg` in projects that use that path; retain its 32 × 32 viewBox, inverted-triangle geometry (`M4 6h24L16 28 4 6Z`), and `#F4B21B` fill. Do not use it as a substitute for the full KUDU logo.
- Use blue outline primary buttons, quiet neutral filled secondary buttons, red filled destructive buttons, soft filled inputs, soft badges, and one simple outline icon family. The library and semantic HEX values are not finalized.
- Use controlled rounding, minimal cards, whitespace, light dividers, and selective soft surfaces. Use approved draft geometry tokens rather than arbitrary values.
- **Never use colored vertical/side accent strips** on cards, panels, alerts, or navigation items. This includes pseudo-elements and inset-shadow substitutes. A full-perimeter keyboard focus indicator is not a decorative side strip and must remain visible.
- Do not automatically add dashboards, four KPI cards, charts, sidebars, tabs, hero banners, AI chat, gradients, glow, or decorative illustrations. Justify each element by a task.
- Keep responsive, accessible, RTL/LTR, loading, empty, error, permission, and disabled behavior in scope from the beginning.

## Execute the selected workflow

### Plan

Use [screen brief](assets/templates/screen-brief.md). State the primary user/task/action, essential information, navigation rationale, component reuse, responsive behavior, and missing inputs. Propose one representative screen before expanding the product. Do not substitute a Finance/AP example for a different department.

### Build or migrate

Read component and product references. Inventory reusable code before creating anything. Use the project's existing stack; the repository does not provide a working `@kudu/ui` import. Implement only the authorized scope. During migration, preserve application behavior and data. Use the draft tokens with their known limitations; propose unresolved values explicitly instead of labeling them approved. Do not change blue outline primary actions without permission.

Run available project tests and inspect actual rendered screens when tools permit. Run `python3 <skill-directory>/scripts/check_tokens.py` for bundled token diagnostics. This checks a limited set of flat color pairs and token references, not live pages or overall accessibility. Never convert a partial pass into a compliance claim.

### Audit

Use [screen review](assets/templates/screen-review.md). Reference exact files/lines or visible screenshot regions. Distinguish observed violations from recommendations and unknowns. Prioritize workflow, accessibility, and consistent controls over decoration. Never claim to inspect a repository or screen that was not available.

### Extend

Use [component proposal](assets/templates/component-proposal.md). Try reuse and composition first; keep a truly product-specific capability local. Document the smallest extension and any departure from approved rules. Seek approval for a new visual language, semantic mapping, icon library, or primitive change. Do not silently redefine the core.

## Report completion with evidence

State what was designed or changed, which approved rules informed it, which checks ran, and what remains untested or blocked. Distinguish proposed, implemented, and validated. Keep user review focused on actual decisions rather than repeating the entire system.

The skill provides guidance and diagnostics, not guaranteed visual uniqueness, automatic installation into other tools, repository access, or production certification.
