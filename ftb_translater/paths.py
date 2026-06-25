from __future__ import annotations

from pathlib import Path


def has_lang_source(quests_dir: Path) -> bool:
    return (quests_dir / "lang" / "en_us.snbt").is_file()


def has_chapters_source(quests_dir: Path) -> bool:
    chapters_dir = quests_dir / "chapters"
    return chapters_dir.is_dir() and any(chapters_dir.glob("*.snbt"))


def resolve_quests_dir(selected_dir: Path) -> Path:
    selected_dir = selected_dir.expanduser().resolve()
    candidates = [
        selected_dir,
        selected_dir / "config" / "ftbquests" / "quests",
    ]
    for candidate in candidates:
        if has_lang_source(candidate) or has_chapters_source(candidate):
            return candidate
    raise FileNotFoundError(
        "Could not find FTB Quests lang/en_us.snbt or chapters/*.snbt. "
        "Select a modpack root or config/ftbquests/quests."
    )


def detect_source_mode(quests_dir: Path) -> str:
    if has_lang_source(quests_dir):
        return "lang"
    if has_chapters_source(quests_dir):
        return "chapters"
    raise FileNotFoundError("Could not find lang/en_us.snbt or chapters/*.snbt.")


def source_lang_path(quests_dir: Path) -> Path:
    return quests_dir / "lang" / "en_us.snbt"


def target_lang_path(quests_dir: Path) -> Path:
    return quests_dir / "lang" / "zh_cn.snbt"
