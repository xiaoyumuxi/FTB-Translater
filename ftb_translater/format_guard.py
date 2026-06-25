from __future__ import annotations

import re


TOKEN_PATTERNS = [
    re.compile(r"§[0-9a-fk-or]", re.IGNORECASE),
    re.compile(r"%(?:\d+\$)?[+#\- 0,(]*\d*(?:\.\d+)?[bcdeEufFgGosxX]"),
    re.compile(r"\{[^{}\n]+\}"),
    re.compile(r"<[^<>\n]+>"),
    re.compile(r"#[a-z0-9_.:-]+", re.IGNORECASE),
]


def preserved_token_warnings(source: str, translated: str) -> list[str]:
    warnings: list[str] = []
    for pattern in TOKEN_PATTERNS:
        source_tokens = pattern.findall(source)
        translated_tokens = pattern.findall(translated)
        if _normalize(source_tokens) != _normalize(translated_tokens):
            warnings.append(f"Token mismatch for pattern {pattern.pattern}")
    return warnings


def _normalize(tokens: list[str]) -> list[str]:
    return sorted(tokens)
