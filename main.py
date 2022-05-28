from faker import Faker
import random
import json

from conf import MODEL


def random_title(book_name: str) -> str:
    """
    Получение случайного названия книги

    :param book_name: Название файла с книгами
    :return: Название случайной книги из списка
    """
    with open(book_name, 'r', encoding='utf8') as f:
        list_books = []
        for line in f:
            list_books.append(line.rstrip('\n'))
    return random.choice(list_books)


def faster_random_title(book_name: str) -> str:
    """
    Cчитывает только одну случайную строку с названием книги

    :param book_name: Название файла с книгами
    :return: Название случайной книги из списка
    """
    with open(book_name, 'r', encoding='utf8') as f:
        for line in f:
            return line


def random_book_num() -> str:
    """
    Получение международного стандартного книжного номера. Генерируется случайным образом с помощью модуля Faker

    :return: Книжный номер
    """
    fake_ru = Faker('ru_RU')
    return fake_ru.isbn13()


def random_author() -> list[str]:
    """
    Получение списка от 1 до 3 ФИО авторов. Генерируется случайным образом с помощью модуля Faker

    :return: Cписок авторов
    """
    fake_ru = Faker('ru_RU')
    author_count = random.randint(1, 3)
    authors = []
    for _ in range(author_count):
        authors.append(fake_ru.name())
    return authors


def main(start_num: int = 1) -> None:
    """
    Генерация списка 100 словарей случайных книг c указанием названия, года, кол-ва страниц... .

    :param start_num: Число с которого начинается нумерация
    :return: .json файл со списком из 100 словарей случайных книг
    """
    with open("output.json", 'w', encoding="utf8") as f:  # записать список в JSON файл
        data_list = []
        for i in range(start_num, start_num+100):
            iner_data_dict = {
                'title': random_title('book.txt'),
                'year': random.randint(1000, 2022),
                'pages': random.randint(1, 10000),
                'isbn13': random_book_num(),
                'rating': f"{random.uniform(0, 5):.2f}",
                'price': f"{random.uniform(10, 5000):.2f}",
                'author': random_author()
                }
            data = {'model': MODEL, 'pk': i, 'fields': iner_data_dict}
            data_list.append(data)
        f.write(json.dumps(data_list, ensure_ascii=False, indent=4))


if __name__ == '__main__':

    main()
