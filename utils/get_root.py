from pathlib import Path

directory = "tests/fixtures/"


def get_root(file):
    path = directory + file
    return Path(__file__).parent.parent / path
