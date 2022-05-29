import logging

from flask import render_template, Blueprint, request, current_app
import exeptions
import functions

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template("index.html")


@main_blueprint.route('/search/')
def search_page():
    path = current_app.config.get('POST_PATH')
    post_list = functions.get_post_list(path)
    text = request.args.get('s')
    logger = logging.getLogger('basic')
    logger.info(f"Выполняется поиск {text}")
    posts = functions.get_post_by_text(text, post_list)
    return render_template("post_list.html", posts=posts, text=text)


@main_blueprint.errorhandler(exeptions.DataSourceBroken)
def data_source_broken(e):
    logger = logging.getLogger('basic')
    logger.error(f"Ошибка загрузки json-файла")
    return "Ошибка загрузки файла. Файл не найден или не в формате json"
