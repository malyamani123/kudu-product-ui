# Installation and daily use

## What you are installing

A self-contained agent skill: instructions, references, draft tokens, review templates, and a diagnostic script. It is not a frontend application, a font installer, or a published `@kudu/ui` library. Adding the repository to GitHub does not automatically activate it in every local project or editor.

## 1. Get the repository

```bash
git clone https://github.com/malyamani123/kudu-product-ui.git
cd kudu-product-ui
```

The scripts require Python 3.10 or later and only use the standard library. On Windows, `py -3` can replace `python`; in WSL/Linux, `python3` may be the available command. Use an existing local project path for the next step.

## 2. Install in a product project

Choose one command for the agent you use:

```bash
python scripts/install_skill.py --tool codex --project /absolute/path/to/project
python scripts/install_skill.py --tool cursor --project /absolute/path/to/project
python scripts/install_skill.py --tool claude --project /absolute/path/to/project
```

| Tool | Installed project directory |
| --- | --- |
| Codex | `.agents/skills/kudu-product-ui/` |
| Cursor | `.agents/skills/kudu-product-ui/` |
| Claude Code | `.claude/skills/kudu-product-ui/` |

Codex and Cursor share the `.agents` location, so installing both into the same project is unnecessary. Do not create duplicate copies for a tool that discovers both directories. The installer refuses an existing destination rather than overwriting it. It does not alter application files, existing agent instructions, or dependencies. Add `--dry-run` to inspect the destination without writing.

For a Windows-native path, quote it:

```powershell
py -3 scripts/install_skill.py --tool cursor --project "C:\Projects\your-project"
```

Open the destination project in the agent environment. Restart or refresh the session when necessary, then explicitly request the skill if automatic discovery does not select it. This repository has not been interactively tested inside your installed editor versions.

## 3. Give it a real task

For Codex, an explicit invocation can start with `$kudu-product-ui`. For Claude Code, use `/kudu-product-ui`. A plain-language request is also useful in a compatible agent:

```text
Use the kudu-product-ui skill. Inspect this project's requirements and existing
implementation. Preserve working behavior. Propose one representative screen
using the approved KUDU foundations and a composition appropriate to this product.
Do not redesign the brand or assume this is an AP system. Identify missing assets,
components, and validation gaps before implementation.
```

For an existing interface:

```text
Use the kudu-product-ui skill to audit this screen and its actual source files.
Report evidence, violated rule, impact, and the smallest compatible repair.
Check typography, hierarchy, controls, tokens, responsive/RTL behavior, and states.
Remove colored side accent strips without changing business logic.
```

For implementation, authorize the proposed scope explicitly. The skill does not grant repository permissions, read inaccessible files, or automatically perform a full application rewrite.

## Working in this repository

`AGENTS.md`, `CLAUDE.md`, and `.cursor/rules/kudu-ui.mdc` route agents to the same canonical skill. The complete references live under `.agents/skills/kudu-product-ui/` so copying the skill alone preserves its relative links. `docs/` and `ai/` are entrypoints, not parallel copies of the specification.

## Updating an installed skill

An installed copy is a snapshot. Pull a reviewed repository revision, compare the installed copy, preserve any local work, and deliberately replace only the named skill directory. The installer has no force/overwrite option. Do not remove project-wide `.agents`, `.claude`, or `.cursor` folders. Never assume central edits update existing products automatically.

## Packaging

```bash
python scripts/validate_repository.py
python -m unittest discover -s tests -v
python scripts/package_skill.py
```

The output is `dist/skill.zip`, containing exactly one portable skill. Upload it only where the destination supports skill ZIP uploads, or extract the skill folder into a supported location. Packaging is not installation into a cloud account. No fonts, source brand PDF, or production data are included.

## Draft limitations

Use the skill as design guidance now. Do not describe the draft CSS as an accessibility-approved palette: the diagnostics expose unresolved contrast combinations. The semantic status palette, icon library, licensed fonts, exact overlay styling, component implementation, and three product pilots still need work. See [open decisions](../.agents/skills/kudu-product-ui/references/open-decisions.md).

## Official tool references

Directory conventions checked 2026-09-17:

- Codex skills: https://developers.openai.com/codex/skills/
- Codex instructions: https://developers.openai.com/codex/guides/agents-md/
- Cursor skills: https://cursor.com/docs/skills
- Cursor rules: https://cursor.com/docs/rules
- Claude Code skills: https://code.claude.com/docs/en/skills

These explain tool conventions, not a guarantee that every installed version has identical behavior.
