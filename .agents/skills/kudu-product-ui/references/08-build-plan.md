# Part 8: Final package and build plan

## Current deliverables

This draft packages the eight planning sections, decision register, source map, practical skill instructions, draft CSS tokens, checklists/templates, prototype briefs, and local helper scripts. All authored content is in English. It is usable as agent guidance now, but not a completed component library.

## Repository organization

- `.agents/skills/kudu-product-ui/`: canonical portable skill, references, token assets, templates, diagnostics.
- `docs/`: readable navigation to canonical references and installation guidance.
- `ai/`, `AGENTS.md`, `CLAUDE.md`, `.cursor/rules/`: short agent entrypoints, not parallel specifications.
- `tokens/`: convenience import to canonical CSS.
- `components/`: implementation status and planned core controls, not fake exports.
- `prototypes/`: three test briefs, explicitly not rendered screens.
- `scripts/`: validate, install a local skill snapshot, and package `skill.zip`.
- `tests/`: tests for the helper scripts and check plans.

Do not commit the supplied brand PDF, font files, credentials, operational records, or production screenshots. Provide licensed internal assets through approved channels. A public repository is not an internal asset store.

## Build sequence

| Stage | Outcome | Gate |
| --- | --- | --- |
| Documentation | Consistent source hierarchy and preserved decisions | No unresolved conflict disguised as approval |
| Token prototype | Draft values inspected and accessible alternatives proposed | Owner approves changes; no silent palette replacement |
| Core controls | Button, Input, Select, Badge, Modal, Table, Search/Filters, Feedback, Navigation, Upload | Real implementation and state tests |
| Intranet pilot | One actual representative page | Actual input/source available; design review |
| Operational pilot | Data workspace plus representative form | Density, actions, filtering, state review |
| Engineering pilot | Project/document composition | Distinct composition with shared language |
| Validation | Screen evidence for devices/locales/states/accessibility | Open defects handled explicitly |
| v1.0 freeze | Approved tokens, controls, and release documentation | All release gates met |
| Shared packages | Deliberate reuse across projects | Stack/API compatibility established |

Use the existing Intranet as the first real-world pilot only after its source or relevant screens are available. The repository URL in this task is the design-system destination, not the Intranet source. No Intranet application edits are authorized or claimed by this packaging step.

Avoid premature infrastructure: no need for dozens of components, a published package, elaborate automation, or separate per-department libraries before validation. A component catalog can be introduced when it helps actual implementation.

## What makes v1.0 ready

The release is ready only when a single tested vocabulary produces three meaningfully different KUDU products, controls behave correctly, approved fonts/assets are available, known contrast gaps are resolved, and responsive/RTL/accessibility checks are documented. Writing specifications alone does not satisfy that gate.

The immediate next implementation task is a token/control specimen followed by one representative Intranet screen, using available project code and assets. Do not start another long general design interview.
