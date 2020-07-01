"""Main module."""

import os


def fmt(folder: str):
    os.system(f"isort --recursive  --force-single-line-imports --apply {folder}")
    os.system(
        f"autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place {folder} --exclude=__init__.py"
    )
    os.system(f"black {folder}")
    os.system(f"isort --recursive --apply {folder}")
