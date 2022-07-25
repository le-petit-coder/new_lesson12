import logging

from flask import Blueprint, render_template, request
from functions import get_posts_by_word
from json import JSONDecodeError

main_web = Blueprint('main_web', __name__, template_folder='templates')


@main_web.route('/')
def main_page():
    return render_template('index.html')


@main_web.route('/search/')
def search_page():
    search_query = request.args.get('s', '')
    logging.info("Выполняю поиск поста")
    try:
        posts = get_posts_by_word(search_query)
    except FileNotFoundError:
        logging.info("Файл не найден")
        return "Файл не найден"
    except JSONDecodeError:
        return "Невалидный файл"
    return render_template('post_list.html', query=search_query, posts=posts)


