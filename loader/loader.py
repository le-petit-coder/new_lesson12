import logging

from flask import Blueprint, render_template, request
from loader.utils import save_picture
from functions import add_post
from json import JSONDecodeError

loader_bp = Blueprint('loader_bp', __name__, template_folder='templates')


@loader_bp.route('/post')
def create_post():
    return render_template('post_form.html')


@loader_bp.route('/post', methods=['POST'])
def add_post_to_web():
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:
        return 'Отсутствует картинка или текст'

    if picture.filename.split('.')[-1] not in ['jpeg', 'png', 'jpg']:
        logging.info("Загруженный файл не картинка")
        return "Неверный формат файла"
    try:
        picture_path = '/' + save_picture(picture)
    except FileNotFoundError:
        logging.info("Файл не найден")
        return "Файл не найден"
    except JSONDecodeError:
        return "Невалидный файл"
    post = add_post({'pic': picture_path, 'content': content})
    return render_template('post_uploaded.html', post=post)

