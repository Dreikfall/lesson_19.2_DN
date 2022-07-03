from flask_restx import Namespace, Resource
from app.dao.model.director import DirectorSchema
from app.helpers.decorators import auth_required, admin_required
from app.implemented import director_service
from flask import request

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200

    @admin_required
    def post(self):
        req_json = request.json
        director_service.create(req_json)
        return "", 201


@director_ns.route("/<int:did>")
class DirectorView(Resource):
    @auth_required
    def get(self, did):
        director_id = director_service.get_one(did)
        return director_schema.dump(director_id), 200

    @admin_required
    def put(self, did):
        req_json = request.json
        req_json["id"] = did
        director_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, did):
        director_service.delete(did)
        return "", 204
