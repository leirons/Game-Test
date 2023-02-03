from pathlib import Path


def get_root(file):
    return Path(__file__).parent.parent.parent / file