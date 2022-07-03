from app.dao.model.director import Director
from app.dao.model.genre import Genre
from app.dao.model.movie import Movie


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get_all(self, **request_args):
        movie_query = self.session.query(Movie.id, Movie.title, Movie.description, Movie.trailer,
                                         Movie.year, Movie.rating, Genre.name.label('genre'),
                                         Director.name.label('director')).join(Genre).join(Director)
        if 'director_id' in request_args:
            movie_query = movie_query.filter(Movie.director_id == request_args.get('director_id'))
        if 'genre_id' in request_args:
            movie_query = movie_query.filter(Movie.genre_id == request_args.get('genre_id'))
        if 'year' in request_args:
            movie_query = movie_query.filter(Movie.year == request_args.get('year'))
        return movie_query.all()

    def get_one(self, mid):
        return self.session.query(Movie.id, Movie.title, Movie.description, Movie.trailer,
                                  Movie.year, Movie.rating, Genre.name.label('genre'),
                                  Director.name.label('director')).join(Genre).join(Director). \
            filter(Movie.id == mid).one()

    def get_one_update(self, mid):
        """ Создается только для применения в методах update в классе MovieService, тк метод выше возвращает
         поля из разных таблиц"""
        return self.session.query(Movie).filter(Movie.id == mid).one()

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete(self, mid):
        self.session.query(Movie).filter(Movie.id == mid).delete()
        self.session.commit()
