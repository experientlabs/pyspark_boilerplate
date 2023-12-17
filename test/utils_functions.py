import os


def update_test_path(path: str) -> str:
    return os.path.abspath(path).replace("test/", "")


def update_pytest_path(path: str) -> str:
    return os.path.abspath(path).replace("test/pytest_tests", "")