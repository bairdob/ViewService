import os

from flask import Flask, request, send_file, make_response

from error_handler import special_exception_handler
from models.images import ImagesDao
from settings import MAX_CATEGORIES

app = Flask(__name__)
app.errorhandler(Exception)(special_exception_handler)

# получаем данные csv файла
images_csv = os.path.join(app.root_path, 'data', 'images.csv')
data = ImagesDao().load(file_path=images_csv)


@app.route('/static/<path:image_url>;<int:amount_shows>;<string:categories>')
def serve_static_image(image_url, amount_shows, categories):
    response = make_response(send_file(os.path.join(app.root_path, 'static', image_url)))
    response.mimetype = 'image/jpeg'
    response.headers['Categories'] = categories.split(';')
    return response


@app.route('/', methods=['GET'])
def index():
    categories = request.args.getlist('category[]')

    # проверяем допустимое количество запрашиваемых категорий
    if len(categories) > MAX_CATEGORIES:
        raise Exception(f'too much categories, must be less {MAX_CATEGORIES}')

    # если можем получаем картинку
    image = data.get_image_by_categories(categories=categories)
    if not image:
        return Response(status=204)

    return send_file(
        os.path.join(app.root_path, 'static', image))


if __name__ == '__main__':
    app.run(debug=True)
