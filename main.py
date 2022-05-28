import random

from faker import Faker
import json

from conf import MODEL


def pk_gen():
    input_ = int(input("введите чило: "))
    yield input_
    input_ += 1


def random_title():
    with open('book.txt', 'r', encoding='utf8') as f:
        title = random.choice(f.readlines())
    return title


def random_book_num():
    fake_ru = Faker('ru_RU')
    return fake_ru.isbn13()


def random_author():
    fake_ru = Faker('ru_RU')
    author_count = random.randint(1, 3)
    authors = []
    for _ in range(author_count):
        authors.append(fake_ru.name())
    return authors


def main(first_num):
    model = MODEL
    pk = pk_gen()
    title = random_title()
    year = random.randint(1000, 2022)
    pages = random.randint(1, 10000)
    isbn13 = random_book_num()
    rating = f"{random.uniform(0, 5):.2f}"
    price = f"{random.uniform(10, 5000):.2f}"
    author = random_author()

    with open("output.json", 'w', encoding="utf8") as f:  # записать список в JSON файл

        f.write(json.dumps(..., ensure_ascii=False, indent=4))


if __name__ == '__main__':
    print(random_title())
    # print(next(pk_gen()))
    # main()
