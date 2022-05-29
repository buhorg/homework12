import exeptions
import json
import os


def get_post_list(filename):
    """
    Получаем из json файла данные в виде списка словарей
    """
    try:
        with open(filename, encoding='utf-8') as file:
            post_list = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise exeptions.DataSourceBroken("Ошибка загрузки файла. Файл не найден или не в формате json")
    else:
        return post_list


def get_post_by_text(text, post_list):
    """
    Проверка на вхождение text в пост
    """
    posts = []
    for post in post_list:
        if post['content'].lower().count(text.lower()):
            posts.append(post)
    return posts


def write_post_to_file(path, data, post_list):
    """
    Записывает пост в файл
    """
    post_list.append(data)
    with open(path, "w", encoding="utf-8") as file:
        json.dump(post_list, file, ensure_ascii=False, indent=4)


def get_upload_file_name(path, filename):
    """
    Считаем количество файлов в директории и каждой следующей картинке присваиваем
    следующий номер
    """
    count = len(os.listdir(path))
    file_extension = filename[filename.find('.'):len(filename)]
    new_filename = str(count+1)+file_extension
    return new_filename


def is_file_picture(filename):
    """
    Проверяем расширение файла на картинку
    """
    file_extension = filename[filename.find('.'):len(filename)]
    if file_extension.lower() in ['.jpg', 'jpeg', '.bmp', '.tif', '.png']:
        return True
    else:
        return False



