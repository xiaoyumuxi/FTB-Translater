from __future__ import annotations

import shutil
from datetime import datetime
from pathlib import Path


def create_backup(quests_dir: Path, directories: tuple[str, ...] = ("lang",)) -> Path:
    """Back up selected quest data directories before writing translations."""
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_root = quests_dir / ".ftb-translater" / "backups" / timestamp
    copied = False
    for directory in directories:
        source = quests_dir / directory
        if not source.is_dir():
            continue
        destination = backup_root / directory
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, destination)
        copied = True
    if not copied:
        names = ", ".join(directories)
        raise FileNotFoundError(f"Missing backup source directories under {quests_dir}: {names}")
    return backup_root
