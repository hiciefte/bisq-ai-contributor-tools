# Bisq AI Skills

Skills in this directory are shared by Codex and Claude Code. Each skill must be self-contained, use hyphen-case, and define `SKILL.md` with YAML frontmatter containing `name` and `description`.

## Available Skills

### bisq-contributor-workflow

Guides day-to-day Bisq implementation work: issue analysis, narrow changes, Java/JavaFX conventions, Gradle verification, P2P safety, wallet and transaction checks, DAO impact, and documentation updates.

### bisq2-javafx-ui

Guides production-ready Bisq2 JavaFX UI work with strict MVC structure, lifecycle cleanup, design system conventions, navigation wiring, automation selectors, desktop harness verification, and review checklists.

### bisq-pr-reviewer

Performs comprehensive Bisq pull request review by combining review-comment extraction with contribution standards, architecture review, and Bitcoin/P2P security validation.

### git-commit-writer

Drafts and reviews professional commit messages with imperative subjects, concise summaries, and body text focused on what changed and why.

### ui-design-principles

Applies pragmatic UI quality checks for JavaFX, web, desktop, mobile, and CLI interfaces.

## Required Structure

```text
skills/{skill-name}/
├── SKILL.md
├── agents/openai.yaml
└── references/          # Optional, for detailed material loaded as needed
```

Use `references/` for long checklists or examples. Keep the main `SKILL.md` focused on workflow and routing.

## Validation

Run from the repository root:

```bash
python3 scripts/validate-repo.py
git diff --check
```
