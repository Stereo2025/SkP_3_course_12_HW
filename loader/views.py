import logging
from json import JSONDecodeError
from flask import render_template, Blueprint, request
from functions import add_post, save_picture
from global_variables import EXTENSIONS, POST_PATH

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post')
def catalog_page():

    """Отображает страницу добавления поста через post_form.html"""

    return render_template("post_form.html")


@loader_blueprint.route('/post', methods=['POST'])
def add_post_page():

    """Функция добавления файлов. После обработки запроса отображает страницу добавленного поста.
    Использует метод POST для добавления поста на сервер."""

    picture = request.files.get("picture")
    content = request.form.get("content")

    if not picture or not content:
        return 'Картинка или текст отсутствует'

    if picture.filename.split('.')[-1] not in EXTENSIONS:
        logging.info('Проверьте формат файла')
        return f"Неверное расширение файла '{picture.filename}.\n" \
               f"Вы загрузили файл расширения: {picture.filename.split('.')[-1]}'" \
               f"<strong>Возможно загрузить только {EXTENSIONS} файлы</strong>"

    filename = save_picture(picture)
    post_to_add = {'pic': filename, 'content': content}

    logging.info(f'Новый пост в {POST_PATH} добавлен')

    try:
        by_post = add_post(post_to_add)

    except JSONDecodeError:
        logging.error(f'Ошибка файла {POST_PATH}')
        return f'Ошибка файла {POST_PATH}'

    except FileNotFoundError:
        logging.error(f'Файл {POST_PATH} не найден.')
        return f'Файл {POST_PATH} не найден.'

    return render_template('post_uploaded.html', post_to_add=by_post)
##################################################################################
