from flask import Flask, jsonify, request

from error_handler import special_exception_handler
from settings import MAX_CATEGORIES

app = Flask(__name__)
app.errorhandler(Exception)(special_exception_handler)


@app.route('/static/<path:filename>;<int:amount_shows>;<string:categories>')
def serve_static_image(filename, amount_shows, categories):
    return jsonify(filename, amount_shows, categories)


@app.route('/', methods=['GET'])
def index():
    categories = request.args.getlist('category[]')
    # проверяем допустимое количество запрашиваемых категорий
    if len(categories) > MAX_CATEGORIES:
        raise Exception(f'too much categories, must be less {MAX_CATEGORIES}')
    return jsonify(categories=categories)


if __name__ == '__main__':
    app.run(debug=True)
