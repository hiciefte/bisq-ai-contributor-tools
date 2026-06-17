# Repository Guidelines

## Project Structure & Module Organization

This repository is a dual Codex and Claude Code plugin source for Bisq contributors. Codex metadata lives in `.codex-plugin/`; Claude Code metadata lives in `.claude-plugin/`. Shared skills live under `skills/{skill-name}/SKILL.md`, with optional `references/` files and Codex UI metadata in `agents/openai.yaml`. Slash commands live in `commands/{command-name}.md`. Planned component areas include `agents/`, `hooks/`, and `mcp-servers/`.

## Build, Test, and Development Commands

There is no compiled build step; most changes are Markdown, YAML, and JSON. Validate locally with:

```bash
python3 scripts/sync-codex-plugin-bundle.py
python3 scripts/validate-repo.py
git diff --check
```

For local testing in Claude Code, add and install the marketplace:

```text
/plugin marketplace add /path/to/bisq-ai-contributor-tools
/plugin install bisq-dev-tools@bisq-marketplace
/plugin list
```

After changing a component, reinstall with `/plugin uninstall bisq-dev-tools` followed by `/plugin install bisq-dev-tools@bisq-marketplace`. For Codex, reinstall through the configured plugin source and start a new thread.

Codex install smoke test:

```bash
codex plugin marketplace add hiciefte/bisq-ai-contributor-tools
codex plugin add bisq-dev-tools@bisq-ai-contributor-tools
```

## Coding Style & Naming Conventions

Use Markdown with YAML frontmatter for skills and commands. Prefer concise headings, tested examples, and direct workflow instructions. All component names, directories, and command files must use hyphen-case, for example `git-commit-writer`, `bisq-pr-reviewer`, or `review-pr.md`. For best Codex compatibility, keep skill frontmatter to `name` and `description`; put tool-specific guidance in the body.

## Testing Guidelines

Validate changed Markdown renders cleanly and that YAML frontmatter parses. For skills, test documented trigger phrases, confirm referenced files exist, and keep `agents/openai.yaml` aligned with `SKILL.md`. For commands, test example invocations and shell snippets. Security-sensitive guidance must not expose private keys, seed phrases, credentials, or real user trade data.

## Commit & Pull Request Guidelines

Follow the existing commit style: imperative, capitalized subjects such as `Add Bisq architecture analysis skill`; keep the subject under 50 characters when practical. Add a body for non-trivial changes explaining what changed and why. Pull requests should include a clear description, testing notes, linked issues such as `Closes #15`, and screenshots or examples when a workflow or rendered output changes.

## Agent-Specific Instructions

When adding or changing agent-facing content, keep instructions actionable and Bisq-specific. Preserve AGPL-3.0 compatibility, respect Bitcoin and P2P security constraints, and do not weaken existing review, security, or contribution checklists.
