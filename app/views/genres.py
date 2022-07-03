from flask import request
from flask_restx import Namespace, Resource
from app.dao.model.genre import GenreSchema
from app.helpers.decorators import auth_required, admin_required
from app.implemented import genre_service

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200

    @admin_required
    def post(self):
        req_json = request.json
        genre_service.create(req_json)
        return "", 201


@genre_ns.route("/<int:gid>")
class GenreView(Resource):
    @auth_required
    def get(self, gid):
        genre_id = genre_service.get_one(gid)
        return genre_schema.dump(genre_id), 200

    @admin_required
    def put(self, gid):
        req_json = request.json
        req_json["id"] = gid
        genre_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, gid):
        genre_service.delete(gid)
        return "", 204
