from flask import Flask
from flask_restx import Api
from app.config import Config
from app.dao.model.user import User
from app.setup_db import db
from app.views.auth import auth_ns
from app.views.genres import genre_ns
from app.views.movies import movie_ns
from app.views.directors import director_ns


# функция создания основного объекта app
from app.views.users import user_ns


def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    register_extensions(application)
    return application


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)

def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)
    #create_data(application, db)


# функция создания новой таблицы с добавлением записей
def create_data(app, db):
    with app.app_context():
        db.create_all()

        u1 = User(username="vasya", password="my_little_pony", role="user")
        u2 = User(username="oleg", password="qwerty", role="user")
        u3 = User(username="oleg", password="P@ssw0rd", role="admin")

        with db.session.begin():
            db.session.add_all([u1, u2, u3])


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    app.run()
