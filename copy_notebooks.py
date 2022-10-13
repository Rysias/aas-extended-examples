"""Create a scrapbook of question notebooks for personal editing"""
from pathlib import Path
import shutil


def main() -> None:
    # Find all -questions.ipynb files
    notebooks = list(Path(".").rglob("*questions.ipynb"))
    print(f"Found {len(notebooks)} notebooks")
    # Create a copy in each directory with "JHR" appended
    for notebook in notebooks:
        new_name = notebook.with_name(notebook.stem + "-JHR" + notebook.suffix)

        # If notebook was modified after the last copy, copy it
        if not new_name.exists():
            shutil.copy(notebook, new_name)
        elif notebook.stat().st_mtime > new_name.stat().st_mtime:
            shutil.copy(notebook, new_name)


if __name__ == "__main__":
    main()
