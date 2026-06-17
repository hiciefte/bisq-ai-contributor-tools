#!/usr/bin/env python3
"""Validate the Bisq AI plugin repository without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:[-+][0-9A-Za-z.-]+)?$")
BUNDLE = ROOT / "plugins" / "bisq-dev-tools"
BUNDLE_DIRS = (".codex-plugin", "commands", "skills")
BUNDLE_FILES = ("AGENTS.md", "CLAUDE.md", "INSTALLATION.md", "LICENSE", "README.md")


def main() -> int:
    errors: list[str] = []
    validate_plugin_manifest(ROOT / ".codex-plugin" / "plugin.json", errors)
    validate_plugin_manifest(ROOT / ".claude-plugin" / "plugin.json", errors, require_interface=False)
    validate_codex_marketplace(errors)
    validate_bundle_sync(errors)
    validate_skills(errors)
    validate_json(ROOT / ".claude-plugin" / "marketplace.json", errors)

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository validation passed")
    return 0


def validate_json(path: Path, errors: list[str]) -> dict | None:
    if not path.is_file():
        errors.append(f"Missing {path.relative_to(ROOT)}")
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"{path.relative_to(ROOT)} is not valid JSON: {exc}")
        return None
    if not isinstance(payload, dict):
        errors.append(f"{path.relative_to(ROOT)} must contain a JSON object")
        return None
    return payload


def validate_plugin_manifest(path: Path, errors: list[str], require_interface: bool = True) -> None:
    payload = validate_json(path, errors)
    if payload is None:
        return

    name = payload.get("name")
    if not isinstance(name, str) or not NAME_RE.fullmatch(name):
        errors.append(f"{path.relative_to(ROOT)} name must be hyphen-case")

    version = payload.get("version")
    if not isinstance(version, str) or not SEMVER_RE.fullmatch(version):
        errors.append(f"{path.relative_to(ROOT)} version must be semver")

    for key in ("description", "license", "repository"):
        if not isinstance(payload.get(key), str) or not payload[key].strip():
            errors.append(f"{path.relative_to(ROOT)} missing non-empty {key}")

    if require_interface:
        if payload.get("skills") != "./skills/":
            errors.append(f"{path.relative_to(ROOT)} skills must be ./skills/")
        interface = payload.get("interface")
        if not isinstance(interface, dict):
            errors.append(f"{path.relative_to(ROOT)} missing interface object")
            return
        for key in ("displayName", "shortDescription", "longDescription", "developerName", "category"):
            if not isinstance(interface.get(key), str) or not interface[key].strip():
                errors.append(f"{path.relative_to(ROOT)} interface.{key} must be non-empty")
        prompts = interface.get("defaultPrompt")
        if not isinstance(prompts, list) or not prompts:
            errors.append(f"{path.relative_to(ROOT)} interface.defaultPrompt must be a non-empty list")


def validate_codex_marketplace(errors: list[str]) -> None:
    path = ROOT / ".agents" / "plugins" / "marketplace.json"
    payload = validate_json(path, errors)
    if payload is None:
        return
    if payload.get("name") != "bisq-ai-contributor-tools":
        errors.append(f"{path.relative_to(ROOT)} name must be bisq-ai-contributor-tools")
    plugins = payload.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        errors.append(f"{path.relative_to(ROOT)} plugins must be a non-empty list")
        return
    match = next((plugin for plugin in plugins if plugin.get("name") == "bisq-dev-tools"), None)
    if not isinstance(match, dict):
        errors.append(f"{path.relative_to(ROOT)} must include bisq-dev-tools plugin")
        return
    source = match.get("source")
    if (
        not isinstance(source, dict)
        or source.get("source") != "local"
        or source.get("path") != "./plugins/bisq-dev-tools"
    ):
        errors.append(
            f"{path.relative_to(ROOT)} bisq-dev-tools source must point to ./plugins/bisq-dev-tools"
        )
    policy = match.get("policy")
    if not isinstance(policy, dict):
        errors.append(f"{path.relative_to(ROOT)} bisq-dev-tools policy must be an object")
    elif policy.get("installation") != "AVAILABLE" or policy.get("authentication") != "ON_INSTALL":
        errors.append(f"{path.relative_to(ROOT)} bisq-dev-tools policy values are invalid")
    bundle_manifest = ROOT / "plugins" / "bisq-dev-tools" / ".codex-plugin" / "plugin.json"
    if not bundle_manifest.is_file():
        errors.append("plugins/bisq-dev-tools is missing .codex-plugin/plugin.json")


def validate_bundle_sync(errors: list[str]) -> None:
    if not BUNDLE.is_dir():
        errors.append("plugins/bisq-dev-tools bundle is missing")
        return
    for directory in BUNDLE_DIRS:
        compare_tree(ROOT / directory, BUNDLE / directory, errors)
    for file_name in BUNDLE_FILES:
        compare_file(ROOT / file_name, BUNDLE / file_name, errors)


def compare_tree(source: Path, target: Path, errors: list[str]) -> None:
    if not target.is_dir():
        errors.append(f"{target.relative_to(ROOT)} is missing; run scripts/sync-codex-plugin-bundle.py")
        return
    source_files = sorted(path.relative_to(source) for path in source.rglob("*") if path.is_file())
    target_files = sorted(path.relative_to(target) for path in target.rglob("*") if path.is_file())
    if source_files != target_files:
        errors.append(f"{target.relative_to(ROOT)} file list is out of sync")
        return
    for relative_path in source_files:
        compare_file(source / relative_path, target / relative_path, errors)


def compare_file(source: Path, target: Path, errors: list[str]) -> None:
    if not target.is_file():
        errors.append(f"{target.relative_to(ROOT)} is missing; run scripts/sync-codex-plugin-bundle.py")
        return
    if source.read_bytes() != target.read_bytes():
        errors.append(f"{target.relative_to(ROOT)} is out of sync; run scripts/sync-codex-plugin-bundle.py")


def validate_skills(errors: list[str]) -> None:
    skills_root = ROOT / "skills"
    for skill_dir in sorted(path for path in skills_root.iterdir() if path.is_dir()):
        skill_name = skill_dir.name
        if not NAME_RE.fullmatch(skill_name):
            errors.append(f"Skill directory {skill_name} must be hyphen-case")
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            errors.append(f"{skill_name} is missing SKILL.md")
            continue
        frontmatter = parse_frontmatter(skill_md, errors)
        if frontmatter is None:
            continue
        extra_fields = sorted(set(frontmatter) - {"name", "description"})
        if extra_fields:
            errors.append(f"{skill_name} frontmatter has unsupported fields: {', '.join(extra_fields)}")
        if frontmatter.get("name") != skill_name:
            errors.append(f"{skill_name} frontmatter name must match directory")
        description = frontmatter.get("description")
        if not isinstance(description, str) or len(description.strip()) < 40:
            errors.append(f"{skill_name} description should be specific and trigger-oriented")
        agent_yaml = skill_dir / "agents" / "openai.yaml"
        if not agent_yaml.is_file():
            errors.append(f"{skill_name} is missing agents/openai.yaml")
        else:
            validate_agent_yaml(skill_name, agent_yaml, errors)


def validate_agent_yaml(skill_name: str, path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    required = ("interface:", "display_name:", "short_description:", "default_prompt:")
    for token in required:
        if token not in text:
            errors.append(f"{skill_name} openai.yaml missing {token.rstrip(':')}")
    if "$" + skill_name not in text:
        errors.append(f"{skill_name} openai.yaml default_prompt should mention ${skill_name}")
    if "\t" in text:
        errors.append(f"{skill_name} openai.yaml must not use tabs")


def parse_frontmatter(path: Path, errors: list[str]) -> dict[str, str] | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{path.relative_to(ROOT)} must start with YAML frontmatter")
        return None
    end = text.find("\n---", 4)
    if end == -1:
        errors.append(f"{path.relative_to(ROOT)} frontmatter is not closed")
        return None
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"{path.relative_to(ROOT)} frontmatter line is invalid: {line}")
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    for key in ("name", "description"):
        if not fields.get(key):
            errors.append(f"{path.relative_to(ROOT)} frontmatter missing {key}")
    return fields


if __name__ == "__main__":
    sys.exit(main())
