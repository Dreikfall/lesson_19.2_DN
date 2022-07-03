from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self, **request_args):
        return self.dao.get_all(**request_args)

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_one_update(self, mid):
        return self.dao.get_one_update(mid)

    def create(self, data):
        self.dao.create(data)

    def update(self, data):
        mid = data.get('id')
        movie = self.get_one_update(mid)
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')
        self.dao.update(movie)

    def update_partial(self, data):
        mid = data.get('id')
        movie = self.get_one_update(mid)
        if "title" in data:
            movie.title = data.get('title')
        if "description" in data:
            movie.description = data.get('description')
        if "trailer" in data:
            movie.trailer = data.get('trailer')
        if "year" in data:
            movie.year = data.get('year')
        if "rating" in data:
            movie.rating = data.get('rating')
        if "genre_id" in data:
            movie.genre_id = data.get('genre_id')
        if "director_id" in data:
            movie.director_id = data.get('director_id')
        self.dao.update(movie)

    def delete(self, mid):
        self.dao.delete(mid)


