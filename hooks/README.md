# Bisq Hooks

This directory contains event handlers for automating Bisq development workflows.

## Coming Soon

Hooks will be added for:
- Pre-commit security checks
- Build validation after code changes
- Test execution triggers
- Code formatting enforcement

## Hook Structure

Hooks are defined in a `hooks.json` file with event matchers and handler scripts.

## Planned Hooks

### Pre-Commit Hooks
- Security sensitive file detection
- Private key pattern checking
- Code style validation

### Post-Tool-Use Hooks
- Automatic build after Java file changes
- Test execution after implementation changes
- Documentation updates after API changes

### Tool Use Hooks
- Gradle dependency resolution
- Module dependency validation

## Contributing

See [CLAUDE.md](../CLAUDE.md) for guidance on creating Bisq-specific hooks.
