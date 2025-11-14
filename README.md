# Bisq Claude Code Plugin Marketplace

> **Official Claude Code plugin marketplace for Bisq contributors**

Comprehensive development tools and configurations for Bisq development, providing domain knowledge, automation, and intelligent assistance specifically designed for P2P Bitcoin exchange development workflows.

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL%203.0-blue.svg)](LICENSE)
[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-purple)](https://code.claude.com/docs/en/plugins)
[![Bisq Network](https://img.shields.io/badge/Bisq-Network-green)](https://bisq.network)

## Features

### ✅ Available Now
- **git-commit-writer**: Professional Git commit message guidance following industry best practices

### 🚧 Planned Components
- **Slash Commands**: Common Bisq build, test, and analysis workflows
- **Specialized Agents**: Expert assistants for trade protocol, P2P networking, Bitcoin transactions, DAO governance
- **Development Hooks**: Automated security checks, build validation, test execution
- **MCP Servers**: Integration with local Bisq instances, trade history, network monitoring

## Installation

### For Bisq Contributors

1. **Add the Bisq marketplace to Claude Code:**
   ```
   /plugin marketplace add hiciefte/bisq-claude-plugin
   ```

2. **Install the Bisq development tools:**
   ```
   /plugin install bisq-dev-tools@bisq-marketplace
   ```

### For Local Development/Testing

1. **Clone this repository:**
   ```bash
   git clone https://github.com/hiciefte/bisq-claude-plugin.git
   cd bisq-claude-plugin
   ```

2. **Add local marketplace:**
   ```
   /plugin marketplace add /path/to/bisq-claude-plugin
   ```

3. **Install the plugin:**
   ```
   /plugin install bisq-dev-tools@bisq-marketplace
   ```

## Current Components

### Skills

#### git-commit-writer
Professional Git commit message guidance following industry best practices based on Chris Beams' widely-adopted guidelines.

**Features:**
- Seven core rules for great commit messages
- Imperative mood enforcement
- Subject line optimization (50 character limit)
- Body wrapping at 72 characters
- What/why focus over how

See [skills/git-commit-writer/](skills/git-commit-writer/) for detailed documentation.

## Project Structure

```
bisq-claude-plugin/
├── .claude-plugin/
│   ├── plugin.json          # Plugin manifest
│   └── marketplace.json     # Marketplace catalog
├── skills/
│   ├── git-commit-writer/   # Git commit standards skill
│   └── README.md
├── commands/                 # Custom slash commands (coming soon)
├── agents/                   # Specialized AI agents (coming soon)
├── hooks/                    # Event handlers (coming soon)
├── mcp-servers/             # MCP server integrations (coming soon)
├── CLAUDE.md                # Claude Code project guidance
└── README.md                # This file
```

## Bisq Development Context

This plugin is designed for Bisq's specific development environment:

- **Multi-module Gradle project** with complex dependencies
- **Java-based** with JavaFX for desktop UI
- **P2P networking** architecture with custom protocols
- **Bitcoin/cryptocurrency** integration requiring security awareness
- **Decentralized** design with no central server
- **Trade protocol** state machines and workflows
- **DAO governance** system integration

## Contributing

We welcome contributions from the Bisq community! To add new components:

1. **Commands**: Add slash commands for common Bisq tasks in `commands/`
2. **Agents**: Create specialized agents for Bisq domain expertise in `agents/`
3. **Skills**: Add domain knowledge and patterns in `skills/`
4. **Hooks**: Create automation hooks in `hooks/`
5. **MCP Servers**: Build integrations with Bisq tools in `mcp-servers/`

See [CLAUDE.md](CLAUDE.md) for detailed guidance on creating configurations.

## Security Considerations

All configurations in this plugin respect:
- Private key and seed phrase protection
- Financial transaction safety
- User privacy in P2P context
- Secure coding practices for cryptocurrency software

## Roadmap

### Phase 1: Foundation (Current)
- [x] Plugin structure and marketplace setup
- [x] Git commit writer skill
- [x] Project documentation

### Phase 2: Core Development Tools
- [ ] Gradle build commands
- [ ] Module-specific build helpers
- [ ] Integration test runners
- [ ] Trade protocol analysis commands

### Phase 3: Specialized Agents
- [ ] Trade protocol debugging agent
- [ ] P2P networking analysis agent
- [ ] Bitcoin transaction review agent
- [ ] DAO proposal evaluation agent

### Phase 4: Advanced Integration
- [ ] Local Bisq instance MCP server
- [ ] Trade history analysis tools
- [ ] Network monitoring integration
- [ ] DAO data access server

## License

This project is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)** - the same license as Bisq 2.

### Why AGPL-3.0?

The AGPL-3.0 ensures that:
- All modifications remain open source
- Network services must provide source code to users (Section 13)
- Full compatibility with Bisq 2 project licensing
- Community contributions stay freely available

See [LICENSE](LICENSE) file for full details.

## Support

- **Issues**: [GitHub Issues](https://github.com/hiciefte/bisq-claude-plugin/issues)
- **Bisq Documentation**: [Bisq Docs](https://docs.bisq.network)
- **Claude Code Docs**: [Claude Code Documentation](https://code.claude.com/docs)

## Links

- [Bisq Network](https://bisq.network)
- [Bisq GitHub](https://github.com/bisq-network/bisq)
- [Claude Code Plugins](https://code.claude.com/docs/en/plugins)
