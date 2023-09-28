"""initializate flask application and include api to app"""
from flask import Flask

from resources import api


app = Flask(__name__)

api.init_app(app)

if __name__ == "__main__":
    app.run('127.0.0.1', port=5000)
