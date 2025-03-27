#  завантаження та первинну обробку даних.
from pathlib import Path


def load_data(filename: str) -> list[str]:
    file_path = Path(__file__).parent / filename
    if file_path.exists():
        with file_path.open("r", encoding="utf-8") as f:
            return f.readlines()
    else:
        print(f"Файл {filename} не найден!")
        return []


def clean_data(salary_data: list[str]) -> list[dict]:
    result = []
    if len(salary_data) > 1:
        for name, salary in (item.strip().split(',') for item in salary_data):
            try:
                result.append({'name': name, 'salary': float(salary)})
            except ValueError:
                print(
                    f'Невірний формат даних для {name}, сума {salary} не є коректною.')
                continue
        return result
    else:
        print('Данні у файлі відсутні')
        return [{}]
