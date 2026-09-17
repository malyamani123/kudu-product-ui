# Repository instructions

For any KUDU interface design, implementation, audit, refactor, or design-system task, read `.agents/skills/kudu-product-ui/SKILL.md` first and follow its task-specific reference routing.

This repository packages a design specification and reusable skill, not a finished frontend library. Treat `0.1.0-draft.1` as a draft. Do not claim visual approval, Arabic typography validation, live integrations, or WCAG conformance without evidence.

Keep all repository content in English. Preserve Arabic/RTL requirements in the system. Do not narrow the system to Finance or AP; support Intranet, Engineering, Supply Chain, and other KUDU products.

The canonical rules and tokens live inside the skill folder. Do not create divergent copies. Do not silently change approved decisions, bundle fonts, publish private source material, or overwrite unrelated application code.

Before delivering repository changes, run:

```bash
python scripts/validate_repository.py
python -m unittest discover -s tests -v
python .agents/skills/kudu-product-ui/scripts/check_tokens.py
```

Report checks actually run, known contrast limitations, and unperformed visual/interaction tests separately. Packaging is `python scripts/package_skill.py`.

## Code review rules

Flag colored side accent strips, hard-coded component restyling, unauthorized font changes, forced dashboards, inaccessible hidden fields, lost data/actions in mobile layouts, and changes that turn three products into one template. Do not approve a component merely because token checks pass.
