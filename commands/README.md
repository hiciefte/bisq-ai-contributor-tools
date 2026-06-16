# Bisq Commands

This directory contains Claude Code slash-command workflows and reusable command playbooks for Bisq development.

## Available Commands

### review-pr

`commands/review-pr.md` defines a comprehensive pull request review workflow. It checks CI status, extracts review comments from GitHub and CodeRabbitAI, filters new feedback, verifies comments against current code, and produces an action checklist.

Use in Claude Code:

```text
/review-pr owner/repo#123
```

Use in Codex by opening `commands/review-pr.md` and following the same phases with `gh`, repository inspection, and local verification.

## Planned Commands

- Build specific Bisq modules
- Run focused integration tests
- Analyze trade protocol state transitions
- Review security-sensitive Bitcoin/P2P changes
- Inspect DAO governance impacts

## Command Structure

Each command is a Markdown file with YAML frontmatter:

```markdown
---
name: command-name
description: Brief description of what the command does
---

# Command Implementation

[Detailed instructions for the agent]
```

Use hyphen-case names and include examples, expected outputs, and failure handling.
