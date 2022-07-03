from app.dao.model.genre import Genre


class GenreDAO:

    def __init__(self, session):
        self.session = session

    def get_all(self):
        director_query = self.session.query(Genre)
        return director_query.all()

    def get_one(self, gid):
        return self.session.query(Genre).filter(Genre.id == gid).one()

    def create(self, data):
        genre = Genre(**data)
        self.session.add(genre)
        self.session.commit()
        return genre

    def update(self, genre):
        self.session.add(genre)
        self.session.commit()

    def delete(self, gid):
        self.session.query(Genre).filter(Genre.id == gid).delete()
        self.session.commit()
