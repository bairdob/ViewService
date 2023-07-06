from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/static/<path:filename>;<int:amount_shows>;<string:categories>')
def serve_static_image(filename, amount_shows, categories):
    return jsonify(filename, amount_shows, categories)


@app.route('/')
def index():
    return 'Index Page'


if __name__ == '__main__':
    app.run(debug=True)
