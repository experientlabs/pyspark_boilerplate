import os


def update_test_path(path: str) -> str:
    return os.path.abspath(path).replace("test/", "")
