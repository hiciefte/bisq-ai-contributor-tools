# Installation Guide

This guide walks you through installing the Bisq Claude Code Plugin marketplace and its tools.

## Prerequisites

- [Claude Code](https://claude.ai/code) installed and configured
- Git (for remote installation method)
- Access to a terminal/command line

## Installation Methods

### Method 1: GitHub Installation (Recommended for Users)

Once this repository is published to GitHub:

1. **Add the Bisq marketplace:**
   ```
   /plugin marketplace add hiciefte/bisq-claude-plugin
   ```

2. **Install the Bisq development tools:**
   ```
   /plugin install bisq-dev-tools@bisq-marketplace
   ```

3. **Verify installation:**
   ```
   /plugin list
   ```

   You should see `bisq-dev-tools` in the list of installed plugins.

### Method 2: Local Installation (For Development/Testing)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hiciefte/bisq-claude-plugin.git
   cd bisq-claude-plugin
   ```

2. **Add the local marketplace to Claude Code:**

   In Claude Code, run:
   ```
   /plugin marketplace add /full/path/to/bisq-claude-plugin
   ```

   Replace `/full/path/to/bisq-claude-plugin` with the actual path where you cloned the repository.

3. **Install the plugin:**
   ```
   /plugin install bisq-dev-tools@bisq-marketplace
   ```

4. **Verify installation:**
   ```
   /plugin list
   ```

### Method 3: Git URL Installation

If you have access to the repository via HTTPS or SSH:

1. **Add marketplace via Git URL:**
   ```
   /plugin marketplace add https://github.com/hiciefte/bisq-claude-plugin.git
   ```

2. **Install the plugin:**
   ```
   /plugin install bisq-dev-tools@bisq-marketplace
   ```

## Managing the Plugin

### View Available Marketplaces
```
/plugin marketplace list
```

### Enable/Disable the Plugin

Temporarily disable without uninstalling:
```
/plugin disable bisq-dev-tools
```

Re-enable:
```
/plugin enable bisq-dev-tools
```

### Update the Plugin

To get the latest version:
```
/plugin update bisq-dev-tools
```

### Uninstall the Plugin

```
/plugin uninstall bisq-dev-tools
```

### Remove the Marketplace

```
/plugin marketplace remove bisq-marketplace
```

## Verifying Installation

After installation, you should have access to:

### Skills
- **git-commit-writer**: Professional Git commit message guidance

Try asking Claude Code:
```
How should I write this commit message for my authentication refactoring?
```

### Commands (Coming Soon)
Custom Bisq development commands will be available via slash commands like `/bisq-build`

### Agents (Coming Soon)
Specialized Bisq domain experts will be available for specific development tasks

## Troubleshooting

### Plugin Not Found
- Verify the marketplace was added correctly: `/plugin marketplace list`
- Check the repository path or URL is correct
- Ensure you have network access (for remote installations)

### Installation Fails
- Check that `.claude-plugin/plugin.json` exists in the repository
- Verify the JSON files are valid (no syntax errors)
- Try removing and re-adding the marketplace

### Plugin Not Working
- Verify the plugin is enabled: `/plugin list`
- Try disabling and re-enabling: `/plugin disable bisq-dev-tools` then `/plugin enable bisq-dev-tools`
- Check Claude Code logs for errors

### Skills Not Activating
- Skills activate automatically based on context
- Try explicitly mentioning relevant keywords (e.g., "git commit message")
- Ensure the plugin is properly installed and enabled

## Getting Help

- **Issues**: Report problems at [GitHub Issues](https://github.com/hiciefte/bisq-claude-plugin/issues)
- **Documentation**: See [README.md](README.md) for plugin features
- **Claude Code Help**: Run `/help` in Claude Code for general assistance

## Next Steps

After installation:
1. Review the [README.md](README.md) to understand available features
2. Check [skills/README.md](skills/README.md) for skill documentation
3. Watch for updates as new commands and agents are added
4. Consider contributing! See [CLAUDE.md](CLAUDE.md) for guidance
