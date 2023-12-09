import os


def update_unittest_path(path: str) -> str:
    output_path = os.path.abspath(path).replace("test/unittest_tests", "")
    return output_path


def update_pytest_path(path: str) -> str:
    return os.path.abspath(path).replace("test/pytest_tests", "")