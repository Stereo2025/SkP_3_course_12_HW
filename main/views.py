import logging
from json import JSONDecodeError
from flask import render_template, Blueprint, request
from functions import find_post, POST_PATH


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():

    """Отображает страницу приложения через шаблон index.html"""

    return render_template("index.html")


@main_blueprint.route('/search/')
def show_page():

    """Отображает страницу поиска постов /search. Получает значение введенной строки через
    request.args.get() и передает его функции find_post() для поиска постов,
    содержащих введенную подстроку."""

    logging.info('Поиск постов...')
    some_query = request.args.get('s')

    try:
        looking_post = find_post(some_query)

    except JSONDecodeError:
        logging.error(f'Ошибка файла {POST_PATH}')
        return f'Ошибка файла {POST_PATH}'

    except FileNotFoundError:
        logging.error(f'Файл {POST_PATH} не найден.')
        return f'Файл {POST_PATH} не найден.'

    return render_template("post_list.html", looking_post=looking_post, some_query=some_query)
#######################################################################################
