import os
from typing import Union

from flask import Flask, Response, make_response, request, send_file, render_template, url_for

from error_handler import special_exception_handler
from models.images import ImagesDao
from settings import MAX_CATEGORIES, CSV_FILE

app = Flask(__name__)
app.errorhandler(Exception)(special_exception_handler)

# получаем данные csv файла
images_csv = os.path.join(app.root_path, CSV_FILE)
data = ImagesDao().load(file_path=images_csv)


@app.route('/static/<path:image_url>;<int:amount_shows>;<string:categories>', methods=['GET'])
def serve_static_image(image_url: str, amount_shows: int, categories: str) -> Response:
    """
    Возвращает картинку c кастомным хедером категорий.

    :param image_url: имя картинки в папке static
    :param amount_shows: необходимое количество показов
    :param categories: категории картинки
    :return: картинку с кастомным хедером
    """
    response = make_response(send_file(os.path.join(app.root_path, 'static', image_url)))
    response.mimetype = 'image/jpeg'
    response.headers['Categories'] = categories.split(';')
    return response


@app.route('/', methods=['GET'])
def index() -> Union[Response, str]:
    """
    Возвращает картинку, по соответствующей категории.

    :return: картинку
    """
    categories = request.args.getlist('category[]')

    # проверяем допустимое количество запрашиваемых категорий
    if len(categories) > MAX_CATEGORIES:
        raise Exception(f'too much categories, must be less {MAX_CATEGORIES}')

    if categories:
        image = data.get_image_by_categories(categories=categories)
    else:
        image = data.get_random_image()

    if not image:
        return Response(status=204)

    return render_template("index.html", image=url_for('static', filename=image))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
