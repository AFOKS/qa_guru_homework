from pathlib import Path
import pytest


def pytest_generate_tests(metafunc):
    data_dir = Path(__file__).parent.parent / "test_data"

    if "data_file" not in metafunc.fixturenames:
        return

   # data_dir = Path(__file__).parent.parent / "test_data"

    files = sorted(
        file
        for pattern in ("*.txt", "*.json")
        for file in data_dir.glob(pattern)
    )

    if not files:
        pytest.skip("В папке test_data нет файлов")

    metafunc.parametrize(
        "data_file",
        files,
        ids=lambda file: f"{file.suffix[1:]}::{file.stem}"
    )