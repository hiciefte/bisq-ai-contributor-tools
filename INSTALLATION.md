# Installation Guide

This guide covers using `bisq-dev-tools` with Claude Code or Codex.

## Prerequisites

- Git
- Claude Code and/or Codex
- A terminal

## Claude Code Installation

For the published marketplace:

```text
/plugin marketplace add hiciefte/bisq-claude-plugin
/plugin install bisq-dev-tools@bisq-marketplace
/plugin list
```

For local development:

```text
/plugin marketplace add /full/path/to/bisq-claude-plugin
/plugin install bisq-dev-tools@bisq-marketplace
/plugin list
```

After editing skills or commands, reinstall locally:

```text
/plugin uninstall bisq-dev-tools
/plugin install bisq-dev-tools@bisq-marketplace
```

## Codex Installation

The repository includes `.codex-plugin/plugin.json` and shared skills under `skills/`. Add or reinstall this plugin through your configured Codex plugin marketplace/source, then start a new thread so Codex reloads skill metadata.

Before installing or submitting changes, validate the repo:

```bash
python3 scripts/validate-repo.py
git diff --check
```

## Verifying Skills

Try prompts that should trigger each skill:

```text
Use bisq-contributor-workflow to implement this Bisq issue safely.
Use bisq2-javafx-ui to implement this Bisq2 JavaFX screen.
Use bisq-pr-reviewer to review bisq-network/bisq2#123.
Use git-commit-writer to draft a commit message for my staged changes.
Use ui-design-principles to review this JavaFX layout.
```

## Troubleshooting

- Plugin not found: verify the marketplace or local path points to this repository.
- Skills not activating: reinstall the plugin and start a fresh agent thread.
- Codex validation issues: check `.codex-plugin/plugin.json`, `skills/*/SKILL.md`, and `skills/*/agents/openai.yaml`.
- Claude Code installation issues: check `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`.

## Getting Help

Open an issue in this repository and include your tool, install method, validation output, and the prompt that did not behave as expected.
