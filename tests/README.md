# Validation scope

Repository checks cover file/reference integrity, decision coverage, token references, packaging constraints, installation safety, and contrast-calculation correctness.

They do not execute Claude, Cursor, or Codex; they do not certify UI behavior or WCAG conformance. `evals/scenarios.json` contains behavior scenarios for later agent evaluation, not claims that those evaluations have run.

Run:

```bash
python scripts/validate_repository.py
python -m unittest discover -s tests -v
python .agents/skills/kudu-product-ui/scripts/check_tokens.py
```

`check_tokens.py --strict` exits nonzero when checked normal-text draft pairs fail. This is intentional until the draft palette is refined. See [open decisions](../.agents/skills/kudu-product-ui/references/open-decisions.md).
