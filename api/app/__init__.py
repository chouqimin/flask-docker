from flask import Flask, request, escape
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

from app.view.task_view import TaskCR, TaskUD
from app.config import app_config

def create_app(config_name='production'):
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(app_config[config_name])
    db.init_app(app)
    migrate.init_app(app, db)

    api.add_resource(TaskCR, '/task')
    api.add_resource(TaskUD, '/task/<int:task_id>')

    @app.route('/')
    def hello():
        name = request.args.get("name", "World")
        return f'Hello, {escape(name)}, I\'m Edison!'

    return app
