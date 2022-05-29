import logging

from flask import render_template, Blueprint, request, current_app, send_from_directory
import functions, exeptions


loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post', methods=['GET'])
def post_page():
    return render_template("post_form.html")


@loader_blueprint.route('/post', methods=['POST'])
def post_uploaded_page():
    path = current_app.config.get('POST_PATH')
    folder = current_app.config.get('UPLOAD_FOLDER')
    picture = request.files.get('picture')
    filename = picture.filename
    if not functions.is_file_picture(filename):
        raise exeptions.PictureExtensionNotAllowed('Формат файла не картинка!')
    new_filename = functions.get_upload_file_name(folder, filename)
    data = {'content': request.values.get('content'), 'pic': f'../{folder}/{new_filename}'}
    try:
        picture.save(f'{folder}/{new_filename}')
    except (FileNotFoundError, EOFError):
        raise exeptions.PictureNotUploadedError('Ошибка загрузки файла')
    post_list = functions.get_post_list(path)
    functions.write_post_to_file(path, data, post_list)
    return render_template('post_uploaded.html', data=data)


@loader_blueprint.route('/uploads/<path:path>')
def static_dir(path):
    return send_from_directory('uploads', path)


@loader_blueprint.errorhandler(exeptions.PictureExtensionNotAllowed)
def error_format_not_allowed(e):
    logger = logging.getLogger('basic')
    logger.info(f"Пытаются загрузить файл, не являющийся картинкой")
    return 'Формат файла не картинка!'


@loader_blueprint.errorhandler(exeptions.PictureNotUploadedError)
def error_picture_not_uploaded(e):
    logger = logging.getLogger('basic')
    logger.error(f"Ошибка загрузки файла")
    return 'Ошибка загрузки файла'
