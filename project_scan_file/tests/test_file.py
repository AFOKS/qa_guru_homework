import json



def test_data_files(data_file):
    print(f"\nПроверяем файл: {data_file.name}")

    if data_file.suffix == ".txt":
        content = data_file.read_text(encoding="utf-8")
        assert len(content) > 0

    elif data_file.suffix == ".json":
        content = json.loads(data_file.read_text(encoding="utf-8"))
        assert isinstance(content, dict)