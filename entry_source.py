import os
from pathlib import Path

TASKNADO_WORD = "Tasknado"


def emit(word: str) -> None:
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "entry.txt").write_text(word, encoding="utf-8")


if __name__ == "__main__":
    emit(TASKNADO_WORD)
