import logging
from flask import Flask, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint


logging.basicConfig(filename='logs.log', filemode='w', level=logging.INFO)
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024


app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):

    """Функция делает видимым для пользователя содержимое папки static."""

    return send_from_directory("uploads", path)


if __name__ == '__main__':
    app.run(debug=True)
#################################################################################
