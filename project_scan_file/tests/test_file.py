import json
import pytest


def test_data_files(data_file):
    match data_file.suffix:
        case ".txt":
            content = data_file.read_text(encoding="utf-8")
            assert content.strip()

        case ".json":
            content = json.loads(data_file.read_text(encoding="utf-8"))
            assert isinstance(content, dict)
            assert content

        case _:
            pytest.fail(f"Неизвестный формат файла: {data_file}")