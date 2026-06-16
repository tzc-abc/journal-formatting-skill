# Contributing

Contributions are welcome.

## Scope

Useful contributions include:

- Better manuscript formatting workflows.
- More robust DOCX inspection utilities.
- Journal checklist improvements.
- Clearer handling of references, declarations, figures, tables, and supplementary files.
- Tests or example prompts that reveal formatting edge cases.

## Guidelines

- Keep `SKILL.md` concise and procedural.
- Put detailed checklists or long reference material in `references/`.
- Put reusable deterministic code in `scripts/`.
- Do not hard-code unverified journal requirements.
- Prefer official journal or publisher sources for journal-specific rules.
- Preserve user manuscript content unless a task explicitly asks for rewriting.

## Validation

Before opening a pull request, run:

```bash
python -m py_compile journal-formatting/scripts/inspect_docx.py
python journal-formatting/scripts/inspect_docx.py --help
```

If you have access to Codex's skill validation script, also run it against the `journal-formatting` folder.
