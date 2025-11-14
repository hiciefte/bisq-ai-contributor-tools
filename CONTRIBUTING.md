# Contributing to Bisq Claude Code Plugin Marketplace

Thank you for your interest in contributing to the Bisq Claude Code Plugin Marketplace! This guide will help you understand our contribution process and best practices.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Naming Conventions](#naming-conventions)
- [Component Guidelines](#component-guidelines)
- [Quality Standards](#quality-standards)
- [Submitting Changes](#submitting-changes)

## Code of Conduct

We are committed to providing a welcoming and inclusive environment. Please be respectful and professional in all interactions.

## Getting Started

### Prerequisites

- [Claude Code](https://claude.ai/code) installed
- Git for version control
- Familiarity with Bisq development (for domain-specific contributions)

### Local Setup

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/bisq-claude-plugin.git
   cd bisq-claude-plugin
   ```

2. **Add the local marketplace to Claude Code:**
   ```
   /plugin marketplace add /path/to/bisq-claude-plugin
   /plugin install bisq-dev-tools@bisq-marketplace
   ```

3. **Verify installation:**
   ```
   /plugin list
   ```

## Development Workflow

### 1. Create a Feature Branch

Follow our branch naming convention:

```bash
# For new skills
git checkout -b feature/bisq-architecture-skill

# For new commands
git checkout -b feature/bisq-build-module

# For bugfixes
git checkout -b fix/git-commit-typo

# For documentation
git checkout -b docs/update-installation-guide
```

### 2. Make Your Changes

Follow the guidelines for your component type (see [Component Guidelines](#component-guidelines)).

### 3. Test Your Changes

- Uninstall and reinstall the plugin to test: `/plugin uninstall bisq-dev-tools` then `/plugin install bisq-dev-tools@bisq-marketplace`
- Verify the component activates correctly
- Test all documented trigger phrases and workflows

### 4. Commit Your Changes

Use the `git-commit-writer` skill to ensure professional commit messages:

```bash
git add .
# Claude Code will help you write a proper commit message
```

**Commit message format:**
- **Subject**: Imperative mood, <50 characters
- **Body**: Explain what and why (not how)
- **References**: Link to related issues

**Example:**
```
Add Bisq architecture analysis skill

Implements a comprehensive skill for analyzing Bisq's multi-module
architecture, including P2P networking patterns, DAO integration,
and Bitcoin transaction handling.

The skill includes:
- Module dependency analysis
- Architecture pattern documentation
- Security consideration guidelines

Closes #15
```

### 5. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a pull request on GitHub with:
- Clear description of changes
- Screenshots/examples if applicable
- Reference to related issues

## Naming Conventions

### Critical Rule: Always Use hyphen-case

**✅ Correct:**
- `git-commit-writer`
- `bisq-architecture`
- `trade-protocol-analyzer`
- `p2p-network-diagnostics`

**❌ Incorrect:**
- `gitCommitWriter` (camelCase)
- `git_commit_writer` (snake_case)
- `GitCommitWriter` (PascalCase)
- `GITCOMMITWRITER` (UPPERCASE)

### File and Directory Names

```
skills/
├── git-commit-writer/         ✅ hyphen-case
│   ├── SKILL.md              ✅ UPPERCASE for special files
│   └── references/           ✅ lowercase
│       └── detailed-guide.md ✅ hyphen-case

commands/
├── bisq-build-module.md      ✅ hyphen-case with .md extension

agents/
├── trade-protocol-analyzer.md ✅ hyphen-case with .md extension

mcp-servers/
├── bisq-instance-connector/   ✅ hyphen-case for directories
│   ├── server.js
│   └── config.json
```

## Component Guidelines

### Skills

Skills must follow the Anthropic Agent Skills Specification v1.0 (October 2025).

**Required Structure:**

```markdown
---
name: skill-name
description: Brief one-sentence description
allowed-tools: [Read, Write, Bash, Grep]
---

# Skill Name

## Overview
[Brief explanation of what this skill does]

## When to Use This Skill

Activate this skill when:
- [Specific trigger scenario 1]
- [Specific trigger scenario 2]
- [Specific trigger scenario 3]

## [Core functionality sections]

[Comprehensive documentation with examples]
```

**Quality Requirements:**
- ✅ YAML frontmatter with `name`, `description`, `allowed-tools`
- ✅ Minimum 3000 bytes of comprehensive documentation
- ✅ Explicit trigger phrases for automatic activation
- ✅ Code examples with proper syntax highlighting
- ✅ Error handling guidance
- ✅ References to relevant documentation

**Example Skill Structure:**

```
skills/bisq-architecture/
├── SKILL.md              # Main skill definition
└── references/           # Supporting documentation
    ├── module-map.md
    ├── p2p-patterns.md
    └── security-notes.md
```

### Commands

Commands are markdown files that define slash commands for Claude Code.

**Required Structure:**

```markdown
---
name: command-name
description: Brief description of what the command does
---

# Command Implementation

[Detailed instructions for Claude Code to execute this command]

## Usage
`/bisq-build-module [module-name]`

## Examples
- `/bisq-build-module core`
- `/bisq-build-module desktop`
```

**File Location:** `commands/command-name.md`

### Agents

Agents are specialized AI assistants with domain expertise.

**Required Structure:**

```markdown
---
name: agent-name
description: Brief description of agent specialization
expertise: [domain1, domain2, domain3]
---

# Agent Name

## Expertise
[Detailed description of agent capabilities]

## Activation
[When this agent should be used]

## Behavior
[How the agent analyzes and responds]
```

**File Location:** `agents/agent-name.md`

### MCP Servers

MCP servers integrate external tools and services.

**Required Structure:**

```
mcp-servers/server-name/
├── README.md           # Server documentation
├── package.json        # Node.js metadata (if applicable)
├── server.js           # Server implementation
└── config.json         # Configuration
```

## Quality Standards

### Before Submitting

Run through this checklist:

#### General
- [ ] Naming follows hyphen-case convention
- [ ] No typos in documentation
- [ ] All links work correctly
- [ ] Changes tested locally
- [ ] Commit messages follow standards

#### For Skills
- [ ] YAML frontmatter present with required fields
- [ ] `name` field matches directory name
- [ ] `description` is clear and concise (one sentence)
- [ ] `allowed-tools` explicitly lists required tools
- [ ] Documentation exceeds 3000 bytes
- [ ] Trigger phrases are explicit and clear
- [ ] Code examples are tested and functional
- [ ] References directory included if needed
- [ ] No security-sensitive information exposed

#### For Commands
- [ ] Command name is descriptive
- [ ] Usage examples included
- [ ] Error handling documented
- [ ] Compatible with Bisq development workflow

#### For Agents
- [ ] Expertise clearly defined
- [ ] Activation triggers specified
- [ ] Behavior patterns documented
- [ ] Bisq domain knowledge accurate

## Submitting Changes

### Pull Request Process

1. **Ensure your PR:**
   - Has a clear, descriptive title
   - References related issues (e.g., "Closes #123")
   - Includes a comprehensive description
   - Follows all quality standards above

2. **PR Description Template:**

   ```markdown
   ## Description
   [Clear description of what this PR does]

   ## Type of Change
   - [ ] New skill
   - [ ] New command
   - [ ] New agent
   - [ ] New MCP server
   - [ ] Bug fix
   - [ ] Documentation update

   ## Testing
   [How you tested these changes]

   ## Checklist
   - [ ] Follows naming conventions (hyphen-case)
   - [ ] Includes comprehensive documentation
   - [ ] All quality standards met
   - [ ] Commit messages follow standards
   - [ ] No security-sensitive information included

   ## Related Issues
   Closes #[issue number]
   ```

3. **Review Process:**
   - Maintainers will review within 7 days
   - Address review feedback promptly
   - Ensure CI/CD passes (when implemented)
   - Be responsive to questions

4. **After Merge:**
   - Your contribution will be included in the next release
   - You'll be credited in release notes
   - Thank you for contributing!

## Component Examples

### Example: Creating a New Skill

1. **Create directory:**
   ```bash
   mkdir -p skills/bisq-architecture
   cd skills/bisq-architecture
   ```

2. **Create SKILL.md:**
   ```bash
   touch SKILL.md
   ```

3. **Add YAML frontmatter and content:**
   ```markdown
   ---
   name: bisq-architecture
   description: Analyze and explain Bisq's multi-module architecture, P2P networking patterns, and system design
   allowed-tools: [Read, Grep, Bash]
   ---

   # Bisq Architecture

   [Comprehensive documentation...]
   ```

4. **Add references if needed:**
   ```bash
   mkdir references
   touch references/module-map.md
   ```

5. **Test the skill:**
   - Reinstall plugin
   - Test activation triggers
   - Verify tool permissions work

6. **Commit and push:**
   ```bash
   git add skills/bisq-architecture
   git commit -m "Add Bisq architecture analysis skill"
   git push origin feature/bisq-architecture-skill
   ```

## Getting Help

- **Questions**: Open a [GitHub Discussion](https://github.com/takahiro/bisq-claude-plugin/discussions)
- **Issues**: Report bugs via [GitHub Issues](https://github.com/takahiro/bisq-claude-plugin/issues)
- **Bisq Help**: See [Bisq Documentation](https://docs.bisq.network)
- **Claude Code**: See [Claude Code Docs](https://code.claude.com/docs)

## License

By contributing, you agree that your contributions will be licensed under the AGPL-3.0 license, the same as Bisq 2.

---

**Thank you for contributing to the Bisq Claude Code Plugin Marketplace!** Your contributions help make Bisq development more efficient and accessible for everyone.
