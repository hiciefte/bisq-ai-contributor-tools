# Bisq Commands

This directory contains custom slash commands for common Bisq development workflows.

## Coming Soon

Commands will be added for:
- Building specific Bisq modules
- Running integration tests
- Analyzing trade protocols
- Reviewing security-sensitive code
- Gradle task shortcuts
- DAO governance operations

## Command Structure

Each command is defined in a markdown file with the following structure:

```markdown
---
name: command-name
description: Brief description of what the command does
---

# Command Implementation

[Command prompt/instructions for Claude Code]
```

## Examples

Future commands might include:
- `/bisq-build [module]` - Build specific Bisq module
- `/bisq-test [test-class]` - Run integration tests
- `/bisq-analyze-protocol` - Analyze trade protocol state machines
- `/bisq-security-review` - Security-focused code review

## Contributing

See [CLAUDE.md](../CLAUDE.md) for guidance on creating Bisq-specific commands.
