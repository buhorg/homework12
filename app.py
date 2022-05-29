from flask import Flask
from main.views import main_blueprint
from loader.views import loader_blueprint
import logging, loggers

app = Flask(__name__)
app.config['POST_PATH'] = "posts.json"
app.config['UPLOAD_FOLDER'] = "uploads/images"
loggers.create_logger()
logger = logging.getLogger('basic')
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)
logger.info('Приложение запускается')
if __name__ == '__main__':
    app.run(debug=True)

