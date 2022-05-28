from faker import Faker
import json

from conf import MODEL


def main():
    with open("output.json", 'w', encoding="utf8") as f:  # записать список в JSON файл

        f.write(json.dumps(..., ensure_ascii=False, indent=4))


if __name__ == '__main__':
    main()
