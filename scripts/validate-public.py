#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError as exc:
    raise SystemExit("Pillow is required. Use the bundled Codex Python runtime.") from exc

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "fabricator"


def fail(message: str) -> None:
    print(f"[fail] {message}", file=sys.stderr)
    raise SystemExit(1)


def ok(message: str) -> None:
    print(f"[ok] {message}")


def load_json(path: Path) -> dict:
    if not path.exists():
        fail(f"missing {path.relative_to(ROOT)}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")


def require_file(path: Path) -> None:
    if not path.is_file():
        fail(f"missing file {path.relative_to(ROOT)}")


def validate_marketplace() -> None:
    marketplace = load_json(ROOT / ".agents" / "plugins" / "marketplace.json")
    if marketplace.get("name") != "fabricator":
        fail("marketplace name must be fabricator")
    entries = marketplace.get("plugins")
    if not isinstance(entries, list):
        fail("marketplace plugins must be a list")
    entry = next((item for item in entries if item.get("name") == "fabricator"), None)
    if not entry:
        fail("marketplace must include fabricator entry")
    if entry.get("source", {}).get("path") != "./plugins/fabricator":
        fail("fabricator source path must be ./plugins/fabricator")
    policy = entry.get("policy", {})
    if policy.get("installation") != "AVAILABLE" or policy.get("authentication") != "ON_INSTALL":
        fail("fabricator policy must be AVAILABLE / ON_INSTALL")
    ok("marketplace entry is valid")


def validate_manifest() -> None:
    manifest = load_json(PLUGIN / ".codex-plugin" / "plugin.json")
    if manifest.get("name") != "fabricator":
        fail("plugin name must be fabricator")
    version = manifest.get("version", "")
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", version):
        fail(f"unexpected plugin version: {version}")
    if manifest.get("skills") != "./skills/":
        fail("manifest skills path must be ./skills/")
    if manifest.get("license") != "PolyForm-Noncommercial-1.0.0":
        fail("manifest license must match LICENSE")
    interface = manifest.get("interface", {})
    for key in ("displayName", "shortDescription", "longDescription", "developerName", "category"):
        if not interface.get(key):
            fail(f"manifest interface.{key} is required")
    if interface.get("displayName") != "Fabricator":
        fail("displayName must be English: Fabricator")
    default_prompt = interface.get("defaultPrompt", "")
    if default_prompt and len(default_prompt) > 128:
        fail("manifest interface.defaultPrompt must be at most 128 characters")
    for icon_key in ("composerIcon", "logo"):
        icon_path = interface.get(icon_key)
        if not icon_path:
            fail(f"manifest interface.{icon_key} is required")
        if ".." in Path(icon_path).parts:
            fail(f"manifest interface.{icon_key} must not contain '..'")
        require_file(PLUGIN / icon_path)
    ok(f"plugin manifest is valid ({version})")


def validate_skills() -> None:
    for name in ("craft", "publish", "watch"):
        skill_path = PLUGIN / "skills" / name / "SKILL.md"
        require_file(skill_path)
        text = skill_path.read_text(encoding="utf-8")
        if f"name: {name}" not in text.split("---", 2)[1]:
            fail(f"{name} frontmatter must contain name: {name}")
        require_file(PLUGIN / "skills" / name / "agents" / "openai.yaml")
    craft = (PLUGIN / "skills" / "craft" / "SKILL.md").read_text(encoding="utf-8")
    publish = (PLUGIN / "skills" / "publish" / "SKILL.md").read_text(encoding="utf-8")
    watch = (PLUGIN / "skills" / "watch" / "SKILL.md").read_text(encoding="utf-8")
    if "public release" not in publish or "fresh-chat" not in publish:
        fail("Publish skill must mention public release and fresh-chat evidence")
    if "public GitHub page" not in publish:
        fail("Publish skill must require public GitHub page refresh")
    if "Post-Public Monitoring" not in publish or "Fabricator: Watch" not in publish:
        fail("Publish skill must require post-public Watch setup")
    if "stale linked skill path" not in craft and "UI skill chip" not in craft:
        fail("Craft skill must recover from stale linked skill cache paths")
    if "passive monitoring" not in watch or "backlog" not in watch:
        fail("Watch skill must cover passive monitoring and backlog intake")
    if "clarify" not in craft.lower() or "Publish" not in craft:
        fail("Craft skill must route ambiguous publication intent")
    ok("Craft, Publish, and Watch skills are present")


def validate_public_docs() -> None:
    for rel in ("README.md", "CHANGELOG.md", "CONTRIBUTING.md", "LICENSE", "docs/release-checklist.md"):
        require_file(ROOT / rel)
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for required in ("Fabricator", "Craft", "Publish", "Watch", "Install", "Update", "License"):
        if required not in readme:
            fail(f"README is missing {required}")
    if "codex plugin marketplace add iamjudin/Fabricator" not in readme:
        fail("README install command must mention iamjudin/Fabricator")
    if "\n## Development\n" in readme or "scripts/validate.sh" in readme:
        fail("README must not expose internal development commands as a main public section")
    checklist = (ROOT / "docs" / "release-checklist.md").read_text(encoding="utf-8")
    if "Public Page Done" not in checklist:
        fail("release checklist must include Public Page Done")
    for required in ("raw public", "isolated `CODEX_HOME`", "local marketplace smoke", "propagation", "Post-Public Watch"):
        if required not in checklist:
            fail(f"release checklist must mention {required}")
    ok("public docs are present")


def validate_icon() -> None:
    icon_path = PLUGIN / "assets" / "icon_fab.png"
    require_file(icon_path)
    with Image.open(icon_path) as icon:
        if icon.size != (512, 512):
            fail(f"{icon_path.relative_to(ROOT)} must be 512x512, got {icon.size}")
        if getattr(icon, "n_frames", 1) != 1:
            fail(f"{icon_path.relative_to(ROOT)} should be static")
    ok("Fabricator icon is 512x512")


def validate_github_files() -> None:
    for rel in (
        ".github/workflows/ci.yml",
        ".github/ISSUE_TEMPLATE/bug_report.yml",
        ".github/PULL_REQUEST_TEMPLATE.md",
    ):
        require_file(ROOT / rel)
    ok("GitHub community and CI files are present")


def validate_no_russian_public_names() -> None:
    public_files = [
        ROOT / "README.md",
        ROOT / "CHANGELOG.md",
        ROOT / "CONTRIBUTING.md",
        PLUGIN / ".codex-plugin" / "plugin.json",
        PLUGIN / "skills" / "publish" / "SKILL.md",
        PLUGIN / "skills" / "publish" / "references" / "publication-principles.md",
        PLUGIN / "skills" / "watch" / "SKILL.md",
        PLUGIN / "skills" / "watch" / "references" / "watch-principles.md",
    ]
    forbidden = ("Фабрикатор", "Крафт", "Паблишь", "Паблик")
    for path in public_files:
        text = path.read_text(encoding="utf-8")
        for word in forbidden:
            if word in text:
                fail(f"{path.relative_to(ROOT)} contains Russian public name {word}")
    ok("public names are English")


def main() -> None:
    validate_marketplace()
    validate_manifest()
    validate_skills()
    validate_public_docs()
    validate_icon()
    validate_github_files()
    validate_no_russian_public_names()
    ok("Fabricator public package validation passed")


if __name__ == "__main__":
    main()
