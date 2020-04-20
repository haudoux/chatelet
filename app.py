from flask import Flask
from test.chatelet.routes import chatelet

from extensions import mysql

app = Flask(__name__)
mysql.init_app(app)

app.register_blueprint(chatelet, url_prefix='/chatelet')
