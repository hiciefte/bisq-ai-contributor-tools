# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Purpose

This repository contains a **Claude Code Plugin Marketplace** for Bisq developers and contributors. It provides:
- **Skills**: Domain knowledge for Git commits, Bisq architecture, security practices
- **Commands**: Slash commands for common Bisq development workflows (planned)
- **Agents**: Specialized AI assistants for Bisq-specific tasks (planned)
- **Hooks**: Event handlers for Bisq development automation (planned)
- **MCP Servers**: Integration with Bisq instances and tools (planned)

## Tech Stack & Versions

- **Plugin System**: Claude Code Plugin System (2025 Spec)
- **License**: GNU AGPL-3.0 (matching Bisq 2 project)
- **Documentation Format**: Markdown with YAML frontmatter
- **Naming Convention**: hyphen-case for all identifiers
- **Repository**: Git-based with GitHub hosting

## Repository Map

```
bisq-claude-plugin/
├── .claude-plugin/           # Plugin configuration (DO NOT MODIFY manually)
│   ├── plugin.json          # Plugin manifest with metadata
│   └── marketplace.json     # Marketplace catalog definition
├── skills/                   # Skill definitions following 2025 spec
│   ├── git-commit-writer/   # ✅ ACTIVE: Git commit standards
│   └── [future-skills]/     # Planned: Bisq architecture, security
├── commands/                 # Slash command definitions
├── agents/                   # Specialized AI agent definitions
├── hooks/                    # Event-driven automation hooks
├── mcp-servers/             # MCP server implementations
├── claudedocs/              # Claude-generated documentation
├── CLAUDE.md                # THIS FILE: Project guidance for Claude
├── README.md                # User-facing project documentation
├── INSTALLATION.md          # Installation and setup guide
└── LICENSE                  # AGPL-3.0 license text
```

**Standard Commands:**
- `/plugin marketplace add takahiro/bisq-claude-plugin` - Add marketplace
- `/plugin install bisq-dev-tools@bisq-marketplace` - Install plugin
- `/plugin list` - View installed plugins
- `/plugin update bisq-dev-tools` - Update plugin to latest version

## Bisq Development Context

Key aspects of Bisq development that configurations should address:
- **Multi-module Gradle project** with complex dependencies
- **Java-based** with JavaFX for desktop UI
- **P2P networking** architecture with custom protocols
- **Bitcoin/cryptocurrency** integration requiring security awareness
- **Decentralized** design with no central server
- **Trade protocol** state machines and workflows
- **DAO governance** system integration

## Naming Conventions & Style Guide

**Follow these naming patterns for all new components:**

### File & Directory Names
- **Format**: `hyphen-case` (lowercase with hyphens)
- **Examples**: `git-commit-writer/`, `bisq-dev-tools`, `trade-protocol-analyzer`
- **Avoid**: `camelCase`, `snake_case`, `PascalCase` in directory/file names

### Plugin Identifiers
- **Plugin Name**: `bisq-dev-tools` (hyphen-case)
- **Marketplace Name**: `bisq-marketplace` (hyphen-case)
- **Skill Names**: `git-commit-writer`, `bisq-architecture` (hyphen-case)

### Skill Structure (2025 Spec)
```yaml
---
name: skill-name
description: Brief description (one sentence)
allowed-tools: [Read, Write, Bash]  # Explicit tool permissions
---

# Skill Name

[Comprehensive documentation with trigger phrases, workflows, examples]
```

### Documentation Standards
- **YAML frontmatter**: Required for all skills
- **Trigger phrases**: Explicit activation keywords
- **File size**: Comprehensive (>3000 bytes recommended)
- **Examples**: Include code examples and error handling
- **Version tracking**: Semantic versioning (1.0.0)

## Creating Configurations

When adding new components, follow these guidelines:

### 1. Skills
- **Location**: `skills/{skill-name}/SKILL.md`
- **Required**: YAML frontmatter with `name`, `description`, `allowed-tools`
- **Content**: Activation triggers, workflow steps, code examples
- **Examples**:
  - `git-commit-writer` - Git commit standards ✅ IMPLEMENTED
  - `bisq-architecture` - Bisq system architecture patterns (planned)
  - `p2p-networking` - P2P protocol best practices (planned)
  - `bitcoin-security` - Bitcoin integration security (planned)

### 2. Commands
- **Location**: `commands/{command-name}.md`
- **Naming**: Use descriptive hyphen-case names
- **Focus**: Common Bisq development tasks
- **Examples**:
  - `bisq-build-module` - Build specific Bisq modules
  - `bisq-run-tests` - Execute integration tests
  - `bisq-analyze-protocol` - Analyze trade protocol states
  - `bisq-security-review` - Security-focused code review

### 3. Agents
- **Location**: `agents/{agent-name}.md`
- **Purpose**: Specialized AI assistants with domain expertise
- **Examples**:
  - `trade-protocol-analyzer` - Trade protocol debugging
  - `p2p-network-diagnostics` - P2P networking analysis
  - `bitcoin-transaction-reviewer` - Bitcoin tx validation
  - `dao-proposal-evaluator` - DAO governance analysis

### 4. MCP Servers
- **Location**: `mcp-servers/{server-name}/`
- **Purpose**: External tool integration
- **Examples**:
  - `bisq-instance-connector` - Local Bisq instance API
  - `trade-history-analyzer` - Trade data analysis
  - `network-monitor` - P2P network diagnostics
  - `dao-data-provider` - DAO blockchain queries

## Security & Compliance

### Critical Security Zones ("DO NOT TOUCH")
- `.claude-plugin/plugin.json` - Auto-managed, manual edits break marketplace
- `.claude-plugin/marketplace.json` - Modify only during releases
- `LICENSE` - AGPL-3.0, must not be changed without legal review

### Security Best Practices
All plugin configurations must respect:
- **Private Key Protection**: Never commit or expose private keys, seed phrases
- **Financial Transaction Safety**: Validate all Bitcoin transaction operations
- **User Privacy**: Respect P2P anonymity and data protection
- **Secure Coding**: Follow OWASP Top 10 for cryptocurrency software
- **Dependency Security**: Verify all MCP server dependencies

### Compliance Requirements
- **License Compliance**: All code must be AGPL-3.0 compatible
- **Attribution**: Maintain proper copyright notices
- **Source Availability**: Network services must provide source access (AGPL Section 13)
- **Modification Notices**: Document all changes with timestamps

## Testing & Quality

### Before Creating Pull Requests
- [ ] All skill files include YAML frontmatter with required fields
- [ ] Skill names use hyphen-case format
- [ ] Documentation exceeds 3000 bytes (comprehensive)
- [ ] Trigger phrases are explicit and clear
- [ ] Code examples are tested and functional
- [ ] Tool permissions declared in `allowed-tools`
- [ ] Version numbers follow semantic versioning

### CI/CD Integration (Future)
- Automated skill validation against 2025 spec
- YAML frontmatter schema validation
- Naming convention enforcement
- Documentation completeness checks
- Security vulnerability scanning

## Branch & PR Etiquette

### Branch Naming
- **Features**: `feature/skill-name` or `feature/command-name`
- **Bugfixes**: `fix/issue-description`
- **Documentation**: `docs/update-description`
- **Examples**: `feature/bisq-architecture-skill`, `fix/git-commit-typo`

### Commit Messages
- Use the `git-commit-writer` skill for all commits
- Follow imperative mood: "Add skill" not "Added skill"
- Keep subject under 50 characters
- Include body for non-trivial changes
- Reference issues: `Fixes #123`

### Pull Request Process
1. Create feature branch following naming convention
2. Implement changes with comprehensive documentation
3. Self-review using quality checklist above
4. Create PR with clear description of changes
5. Address review feedback promptly
6. Ensure CI/CD passes (when implemented)
