from data import get_cats_info


def main():
    filename = 'cat_data_file.txt'
    # завантажуємо данні та форматуємо у список словників
    cat_dict = get_cats_info(filename)
    print(cat_dict)


if __name__ == "__main__":
    main()
