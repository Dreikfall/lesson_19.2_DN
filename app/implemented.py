from app.dao.director import DirectorDAO
from app.dao.genre import GenreDAO
from app.dao.movie import MovieDAO
from app.dao.user import UserDAO
from app.service.auth import AuthService
from app.service.director import DirectorService
from app.service.genre import GenreService
from app.service.movie import MovieService
from app.service.user import UserService
from app.setup_db import db

# создаются связанные объекты DAO и Service

movie_dao = MovieDAO(db.session)
director_dao = DirectorDAO(db.session)
genre_dao = GenreDAO(db.session)
user_dao = UserDAO(db.session)

movie_service = MovieService(movie_dao)
director_service = DirectorService(director_dao)
genre_service = GenreService(genre_dao)
user_service = UserService(user_dao)
auth_service = AuthService(user_service)





