# Contributing to Bisq AI Contributor Tools

Thank you for improving the AI setup for Bisq contributors. This repository should help agents produce safer, smaller, better-tested contributions to Bisq.

## Local Setup

```bash
git clone https://github.com/hiciefte/bisq-claude-plugin.git
cd bisq-claude-plugin
python3 scripts/validate-repo.py
```

For Claude Code, add and install the local marketplace:

```text
/plugin marketplace add /full/path/to/bisq-claude-plugin
/plugin install bisq-dev-tools@bisq-marketplace
```

For Codex, reinstall through your configured plugin source after local edits and start a new thread so skill metadata reloads.

## Branch Naming

Use hyphen-case:

```bash
git checkout -b feature/bisq-contributor-workflow
git checkout -b fix/pr-reviewer-trigger
git checkout -b docs/update-installation-guide
```

## Component Naming

All component names, files, and directories must use hyphen-case:

- Good: `bisq-pr-reviewer`, `git-commit-writer`, `review-pr.md`
- Avoid: `bisq_pr_reviewer`, `GitCommitWriter`, `reviewPR.md`

## Skills

Skills are shared by Codex and Claude Code.

Required structure:

```text
skills/{skill-name}/
├── SKILL.md
├── agents/openai.yaml
└── references/          # Optional
```

`SKILL.md` frontmatter must contain only `name` and `description`:

```markdown
---
name: bisq-example-skill
description: Explain what the skill does and when Codex or Claude Code should use it.
---
```

Put tool-specific behavior, slash-command references, and detailed workflows in the body. Keep the body focused; move long checklists or examples to `references/`.

## Commands

Claude Code slash-command workflows live in `commands/{command-name}.md`. Keep them executable as written, with clear phases, example inputs, and failure handling. When a command is useful to Codex too, document how a Codex agent can follow the same workflow manually from the command file.

## Quality Checklist

Before opening a pull request:

- Run `python3 scripts/validate-repo.py`.
- Run `git diff --check`.
- Test changed trigger phrases in Codex or Claude Code where possible.
- Verify all referenced files and commands exist.
- Keep examples free of private keys, seed phrases, credentials, and real user trade data.
- Use Bisq-specific guidance for Bitcoin, P2P networking, trade protocol, DAO, and JavaFX changes.

## Commit Messages

Use the `git-commit-writer` skill. Subjects should be imperative, capitalized, and concise:

```text
Add Bisq contributor workflow skill
Fix PR reviewer trigger wording
Document Codex plugin installation
```

Add a body for non-trivial changes explaining what changed and why. Reference issues with `Closes #123` when applicable.

## Pull Requests

PRs should include:

- Clear summary of the change.
- Testing performed, including validation output.
- Related issues or context.
- Screenshots or prompt/output examples when UX, command behavior, or rendered docs change.

## Security

Treat Bisq as security-sensitive financial software. Do not add unsafe examples around private keys, wallet seeds, transaction signing, peer trust, or user trade data. Review security-sensitive changes with `bisq-pr-reviewer`.

## License

By contributing, you agree that your contributions are licensed under AGPL-3.0.
