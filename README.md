# KUDU Product UI System

**Version: 0.1.0-draft.1 | Status: approved direction, unvalidated implementation draft**

A reusable design system and agent skill for KUDU's internal digital products. It covers Intranet, Engineering, Supply Chain, Finance, HR, Operations, administration, document workflows, and AI tools. It is not an AP-specific system and is not a single dashboard template.

**Strict foundations. Reusable components. Flexible product composition.**

## Start here

| Your task | Read or use |
| --- | --- |
| Understand the agreed design direction | [Foundations](.agents/skills/kudu-product-ui/references/01-foundations.md) |
| See all 45 decisions and the additional prohibition | [Decision register](.agents/skills/kudu-product-ui/references/decisions.md) |
| Ask an agent to design, implement, or review a KUDU UI | [Skill entrypoint](.agents/skills/kudu-product-ui/SKILL.md) |
| Install the skill into another project | [Installation guide](docs/INSTALLATION.md) |
| Apply the draft CSS variables | [Token entrypoint](tokens/index.css) |
| Review component behavior | [Component specifications](.agents/skills/kudu-product-ui/references/02-components.md) |
| Understand what is not finalized | [Open decisions and validation gaps](.agents/skills/kudu-product-ui/references/open-decisions.md) |
| Continue the first real pilot | [Intranet pilot brief](prototypes/intranet/README.md) |

## What is included

All documentation, code comments, templates, and instructions are in English. The product system requires Arabic/RTL and English/LTR support.

- All eight planning parts, consolidated without repetitive conversation text.
- A traceable register of the 45 choices plus the prohibition on colored side accent strips.
- A self-contained `kudu-product-ui` skill, with references, token assets, templates, and a token-checking script.
- Owner-supplied horizontal and vertical KUDU PNG logo variants for approved product placements.
- `AGENTS.md`, `CLAUDE.md`, and a Cursor rule that route agents to the same canonical skill.
- Draft CSS tokens, a source/status map, prototype briefs, evaluation scenarios, and review checklists.
- Local scripts to validate, install, and package the skill without network access or third-party Python dependencies.

## What is not included

This is **not** a completed React component library, a published `@kudu/ui` package, or three validated product prototypes. No production accessibility conformance is claimed. Framework selection, icon library, licensed fonts, semantic color values, overlay shadows, and visual approval still have open work.

No font binaries, original brand PDF, production data, internal screenshots, or private business records are distributed here. The approved horizontal and vertical KUDU PNG logo variants are included for this skill; do not recreate, distort, or redistribute the official logo outside approved use.

## Use the skill immediately

Open this repository in a compatible agent environment and ask:

```text
Use the kudu-product-ui skill. Review the product requirements and existing
implementation first. Propose the page composition using the approved KUDU
rules. Do not invent a new visual language or assume this is an AP system.
Identify missing components and validation gaps before implementation.
```

To use it inside a different project, clone this repository and install the self-contained folder:

```bash
git clone https://github.com/malyamani123/kudu-product-ui.git
cd kudu-product-ui
python scripts/install_skill.py --tool cursor --project /absolute/path/to/your-project
```

Use `--tool codex` or `--tool claude` for the corresponding project location. On Windows, use `py -3` instead of `python` when needed. The installer refuses to overwrite an existing skill and never changes your application's source files. See the installation guide before upgrading an installed copy.

## Local checks and packaging

Requires Python 3.10 or later.

```bash
python scripts/validate_repository.py
python -m unittest discover -s tests -v
python .agents/skills/kudu-product-ui/scripts/check_tokens.py
python scripts/package_skill.py
```

The last command creates `dist/skill.zip`. The contrast checker intentionally reports known draft limitations; it is not an accessibility certification. Run it with `--strict` before claiming the checked normal-text pairs meet the target.

## Single source of truth

The portable skill owns the full references and token assets:

```text
.agents/skills/kudu-product-ui/
  SKILL.md
  agents/openai.yaml
  references/
  assets/tokens/
  assets/logos/
  assets/templates/
  scripts/check_tokens.py
```

`docs/`, `ai/`, `components/`, and `tokens/` are navigation or integration entrypoints, not competing copies of the rules. This intentionally refines the proposed repository layout: copying the skill alone must not break its reference links.

## Design signature

Simple, warm, practical, balanced, subtly branded, flat and clean. Warm off-white workspace, white working surfaces, blue outline primary actions, neutral filled secondary actions, red filled destructive actions, soft badges, simple outline icons, controlled rounded corners, minimal cards, and no colored vertical/side accent strips.

## Next milestone

Provision Poppins and Tajawal in the actual product; audit one real Intranet page; implement core components in the actual project stack; then test operational and engineering compositions. Freeze `v1.0.0` only after the three pilots and accessibility, responsive, and RTL checks have evidence.
