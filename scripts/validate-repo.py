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


def main() -> int:
    errors: list[str] = []
    validate_plugin_manifest(ROOT / ".codex-plugin" / "plugin.json", errors)
    validate_plugin_manifest(ROOT / ".claude-plugin" / "plugin.json", errors, require_interface=False)
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
