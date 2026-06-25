from __future__ import annotations

from pathlib import Path

try:
    from dotenv import dotenv_values, load_dotenv
except ImportError:  # pragma: no cover - dependency is declared, fallback keeps imports readable.
    dotenv_values = None
    load_dotenv = None


ENV_KEY = "DEEPSEEK_API_KEY"


def env_path(base_dir: Path | None = None) -> Path:
    return (base_dir or Path.cwd()) / ".env"


def load_api_key(base_dir: Path | None = None) -> str:
    path = env_path(base_dir)
    if dotenv_values is not None and path.exists():
        value = dotenv_values(path).get(ENV_KEY)
        if value:
            return str(value)
    if path.exists():
        value = _read_env_file(path).get(ENV_KEY)
        if value:
            return value
    if load_dotenv is not None:
        load_dotenv(path)
    import os

    return os.getenv(ENV_KEY, "")


def save_api_key(api_key: str, base_dir: Path | None = None) -> None:
    path = env_path(base_dir)
    path.parent.mkdir(parents=True, exist_ok=True)

    lines: list[str] = []
    if path.exists():
        lines = path.read_text(encoding="utf-8").splitlines()

    replacement = f"{ENV_KEY}={api_key.strip()}"
    found = False
    next_lines: list[str] = []
    for line in lines:
        if line.startswith(f"{ENV_KEY}="):
            next_lines.append(replacement)
            found = True
        else:
            next_lines.append(line)
    if not found:
        next_lines.append(replacement)

    path.write_text("\n".join(next_lines).rstrip() + "\n", encoding="utf-8")


def _read_env_file(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        value = value.strip().strip('"').strip("'")
        values[key.strip()] = value
    return values
