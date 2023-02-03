from pathlib import Path


def get_root(file):
    print(Path(__file__).parent.parent / file)
    return Path(__file__).parent.parent / file
