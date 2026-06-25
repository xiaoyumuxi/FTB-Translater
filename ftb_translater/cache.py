from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


class TranslationCache:
    def __init__(self, path: Path):
        self.path = path
        self._data: dict[str, str] = {}

    def load(self) -> None:
        if not self.path.exists():
            self._data = {}
            return
        with self.path.open("r", encoding="utf-8") as file:
            raw = json.load(file)
        if not isinstance(raw, dict):
            raise ValueError(f"Invalid cache file: {self.path}")
        self._data = {str(key): str(value) for key, value in raw.items()}

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w", encoding="utf-8") as file:
            json.dump(self._data, file, ensure_ascii=False, indent=2, sort_keys=True)

    def get(self, source_text: str, model: str, target_locale: str, style: str) -> str | None:
        return self._data.get(self._key(source_text, model, target_locale, style))

    def set(self, source_text: str, model: str, target_locale: str, style: str, translation: str) -> None:
        self._data[self._key(source_text, model, target_locale, style)] = translation

    @staticmethod
    def _key(source_text: str, model: str, target_locale: str, style: str) -> str:
        payload: dict[str, Any] = {
            "source_text": source_text,
            "model": model,
            "target_locale": target_locale,
            "style": style,
        }
        encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True).encode("utf-8")
        return hashlib.sha256(encoded).hexdigest()
