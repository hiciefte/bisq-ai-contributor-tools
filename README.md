# Bisq AI Contributor Tools

> Dual-use Codex and Claude Code plugin resources for Bisq contributors.

This repository packages skills, commands, and contributor guidance that help AI coding agents work safely and productively on Bisq. The focus is high-quality contribution flow: understanding Bisq architecture, making narrow changes, respecting Bitcoin/P2P security constraints, reviewing pull requests, and writing clear commits.

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL%203.0-blue.svg)](LICENSE)
[![Bisq Network](https://img.shields.io/badge/Bisq-Network-green)](https://bisq.network)

## Available Skills

- **bisq-contributor-workflow**: Day-to-day implementation guidance for Bisq issues, Java/JavaFX changes, Gradle verification, P2P logic, wallet safety, DAO work, and documentation.
- **bisq2-javafx-ui**: Production-ready Bisq2 JavaFX UI implementation guidance covering MVC, lifecycle cleanup, design system usage, navigation, automation selectors, and desktop harness verification.
- **bisq-pr-reviewer**: Pull request review workflow with CodeRabbitAI extraction, Bisq contribution standards, architecture checks, and cryptocurrency security review.
- **git-commit-writer**: Commit message guidance using imperative subjects, concise summaries, and useful bodies.
- **ui-design-principles**: Cross-platform UI quality guidance with special value for Bisq JavaFX screens.

## Installation

### Claude Code

```text
/plugin marketplace add hiciefte/bisq-claude-plugin
/plugin install bisq-dev-tools@bisq-marketplace
```

For local development, replace the marketplace argument with this repository path:

```text
/plugin marketplace add /path/to/bisq-claude-plugin
/plugin install bisq-dev-tools@bisq-marketplace
```

### Codex

This repo includes `.codex-plugin/plugin.json`, so it can be installed as a Codex plugin from a local or marketplace-backed plugin source. During local iteration, validate the repository first:

```bash
python3 scripts/validate-repo.py
```

Then reinstall the plugin through your configured Codex marketplace or plugin workflow so the updated skills are loaded in a new thread.

## Project Structure

```text
bisq-claude-plugin/
├── .codex-plugin/           # Codex plugin manifest
├── .claude-plugin/          # Claude Code plugin manifest and marketplace
├── skills/                  # Shared Codex/Claude Code skills
├── commands/                # Claude Code slash commands and reusable workflows
├── agents/                  # Planned specialized agent definitions
├── hooks/                   # Planned automation hooks
├── mcp-servers/             # Planned Bisq integration servers
├── scripts/                 # Repository validation helpers
├── AGENTS.md                # Contributor guide
└── CLAUDE.md                # Agent-facing repository guidance
```

## Development

Most changes are Markdown, YAML frontmatter, and JSON metadata. Use hyphen-case for every skill, command, and component name. Keep `SKILL.md` frontmatter limited to `name` and `description` for best Codex compatibility; place tool-specific guidance in the body.

Run before submitting changes:

```bash
python3 scripts/validate-repo.py
git diff --check
```

## Bisq Context

AI agents using this plugin should account for Bisq's multi-module Gradle codebase, Java/JavaFX desktop UI, decentralized P2P architecture, Bitcoin wallet and transaction safety, trade protocol state machines, DAO governance, and strict privacy expectations.

## Security

Never add prompts, examples, scripts, or docs that expose private keys, seed phrases, credentials, real user trade data, or unsafe Bitcoin transaction behavior. Security-sensitive changes should trigger `bisq-pr-reviewer` and use focused verification.

## License

This project is licensed under the [AGPL-3.0](LICENSE), matching Bisq 2.
