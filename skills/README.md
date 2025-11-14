# Bisq Claude Code Skills

This directory contains skills for Claude Code to enhance its capabilities when working with Bisq development.

## Available Skills

### git-commit-writer

Guides Claude to write professional, informative Git commit messages following industry best practices based on Chris Beams' widely-adopted guidelines.

**When to use:**
- Writing commit messages for Bisq code changes
- Reviewing proposed commits before they're pushed
- Improving commit message quality
- Questions about commit message standards

**Key features:**
- Follows the seven core rules of great commit messages
- Subject line limited to 50 characters
- Uses imperative mood ("Fix bug" not "Fixed bug")
- Body wrapped at 72 characters
- Explains what and why, not how

**Reference:** See `git-commit-writer/references/detailed-guide.md` for comprehensive examples and patterns.

## Using Skills

Claude Code automatically activates skills when appropriate context is detected. Skills can also be manually invoked using the Skill tool.

## Adding New Skills

When adding skills for Bisq development, consider:

1. **Bisq-Specific Knowledge**: Domain expertise about P2P networking, Bitcoin integration, DAO governance
2. **Development Workflows**: Common patterns and practices in Bisq development
3. **Security Awareness**: Financial software security best practices
4. **Architecture Patterns**: Multi-module Gradle project patterns, JavaFX UI patterns

Skills should include:
- `SKILL.md` with clear activation triggers and usage patterns
- `references/` directory with detailed guides and examples
- Frontmatter with name and description for Claude Code integration
