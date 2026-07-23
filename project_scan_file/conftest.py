from pathlib import Path


def pytest_generate_tests(metafunc):
    if "data_file" in metafunc.fixturenames:
        data_dir = Path("test_data")

        files = list(data_dir.glob("*.txt"))
        files += list(data_dir.glob("*.json"))

        metafunc.parametrize(
            "data_file",
            files,
            ids=[file.name for file in files]
        )