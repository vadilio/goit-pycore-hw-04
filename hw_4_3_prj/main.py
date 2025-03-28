import sys
from pathlib import Path
from colorama import Fore, Style


# префікс потрібен на кожної наступної рекурсії
def print_directory_structure(directory, prefix=""):
    try:
        path = Path(directory)
        # перевірка на відсутність каталогу
        if not path.exists() or not path.is_dir():
            print(
                Fore.RED + "Помилка: Вказаний шлях не є директорією або не існує." + Style.RESET_ALL)
            return
        # створюємо список папок та файлів у заданної дир., сортуємо файли.
        entries = sorted(path.iterdir(), key=lambda e: (
            e.is_file(), e.name.lower()))
        # перебіраємо всі каталоги та файли у списку, для кожного каталогу рекурсівно визиваємо функцію
        for index, entry in enumerate(entries):
            # print(index, entry)
            connector = "|-- " if index < len(entries) - 1 else "|__ "
            if entry.is_dir():
                print(Fore.BLUE + prefix + connector +
                      entry.name + "/" + Style.RESET_ALL)
                # для папки - рекурсія. До префіксу додаємо сімвол конектора
                print_directory_structure(
                    entry, prefix + ("|   " if index < len(entries) - 1 else "    "))
            else:
                # для файла віводимо його зеленим кольором з префіксом та конектором
                print(Fore.GREEN + prefix + connector +
                      entry.name + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Помилка: {e}" + Style.RESET_ALL)


if __name__ == "__main__":
    # перевіряємо, чи додано шлях до потрібного каталогу (нулевий аргумент - ісх. файл, перший - шлях до каталогу)
    if len(sys.argv) != 2:
        print(Fore.YELLOW +
              "Відсутні параметри: python main.py <шлях_до_директорії>" + Style.RESET_ALL)
    else:
        print_directory_structure(sys.argv[1])
