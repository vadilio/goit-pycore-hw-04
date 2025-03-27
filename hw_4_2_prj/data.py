from pathlib import Path


def get_cats_info(path: str) -> list[dict]:
    result = []
    cat_data_list = load_data(path)
    for item in cat_data_list:
        # Split the string to list
        Cat_data = item.rstrip().split(',')
        # Создаем словарь и добавляем его в список.
        # Також виявляємо можливу помилку перетворення типів
        try:
            result.append({
                'id': Cat_data[0],
                'name': Cat_data[1],
                'value': int(Cat_data[2])
            })
        except ValueError:
            print(f"Невірний формат даних в стрічці:\n{Cat_data}\n")
            continue
    return result

# Reading the data from the file


def load_data(filename: str) -> list[str]:
    file_path = Path(__file__).parent / filename
    if file_path.exists():
        with file_path.open("r", encoding="utf-8") as f:
            return f.readlines()
    else:
        print(f"Файл {filename} не знайдено!")
        return []
