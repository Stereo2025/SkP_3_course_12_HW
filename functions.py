import json
from global_variables import POST_PATH, UPLOAD_FOLDER


def load_json() -> list[dict]:

    """Загружает посты из posts.json"""

    with open(POST_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_picture(picture) -> str:

    """
    Принимает картинку типа FileStorage, сохраняет его в папку /uploads/images и возвращает этот путь.
    :param picture:
    :return:строка, путь к картинке
    """

    picture_name = picture.filename
    path = f'{UPLOAD_FOLDER}/{picture_name}'
    picture.save(path)
    return path


def find_post(word: str) -> list[dict]:

    """
    Возвращает список словарей, в котором пост - это словарь у которого
    по ключу content лежит вводимая подстрока
    :param word: подстрока которую мы ищем
    :return: список словарей
    """

    return [post for post in load_json() if word.lower() in post['content'].lower()]


def add_post(post: dict) -> dict:

    """
    Добавляет пост к исходному списку с постами и возвращает добавленный словарь
    :param post: пост для добавления
    :return: словарь
    """

    posts = load_json()
    posts.append(post)

    with open(POST_PATH, 'w', encoding='utf-8') as file:
        json.dump(posts, file, indent=2, ensure_ascii=False)
    return post
#####################################################################################
