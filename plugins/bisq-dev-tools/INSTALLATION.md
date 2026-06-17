# Installation Guide

This guide covers using `bisq-dev-tools` with Claude Code or Codex.

## Prerequisites

- Git
- Claude Code and/or Codex
- A terminal

## Claude Code Installation

For the published marketplace:

```text
/plugin marketplace add hiciefte/bisq-ai-contributor-tools
/plugin install bisq-dev-tools@bisq-marketplace
/plugin list
```

For local development:

```text
/plugin marketplace add /full/path/to/bisq-ai-contributor-tools
/plugin install bisq-dev-tools@bisq-marketplace
/plugin list
```

After editing skills or commands, reinstall locally:

```text
/plugin uninstall bisq-dev-tools
/plugin install bisq-dev-tools@bisq-marketplace
```

## Codex Installation

Install from the GitHub-backed Codex marketplace:

```bash
codex plugin marketplace add hiciefte/bisq-ai-contributor-tools
codex plugin add bisq-dev-tools@bisq-ai-contributor-tools
```

Verify that Codex sees the marketplace and plugin:

```bash
codex plugin marketplace list
codex plugin list --marketplace bisq-ai-contributor-tools --available
```

Start a new Codex thread after installation so the bundled skills are loaded.

Before installing or submitting changes, validate the repo:

```bash
python3 scripts/validate-repo.py
git diff --check
```

To update an existing install after this repository changes:

```bash
codex plugin marketplace upgrade bisq-ai-contributor-tools
codex plugin add bisq-dev-tools@bisq-ai-contributor-tools
```

Then start a new Codex thread.

## Maintaining The Codex Bundle

Codex installs the generated bundle at `plugins/bisq-dev-tools`. When editing root-level skills, commands, or docs, regenerate the bundle before validation:

```bash
python3 scripts/sync-codex-plugin-bundle.py
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
