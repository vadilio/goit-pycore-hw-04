from data import load_data, clean_data
from processing import calculate_stat


def main():
    filename = 'salary_file.txt'
    # завантажуємо данні та форматуємо у список словників
    salary_data = clean_data(load_data(filename))
    # виберемо зі словарю тільки сумми віплат та створимо список сум
    salaries = [person['salary'] for person in salary_data]
    # розрахунок та вивід:
    print(
        f"Загальна сума заробітної плати: {calculate_stat(salaries)[0]}, Середня заробітна плата: {calculate_stat(salaries)[1]}")


if __name__ == "__main__":
    main()
