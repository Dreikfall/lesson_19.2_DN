from flask import request
from flask_restx import Resource, Namespace
from app.dao.model.user import UserSchema
from app.implemented import user_service

user_ns = Namespace('users')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        all_users = user_service.get_all()
        return users_schema.dump(all_users), 200

    def post(self):
        req_json = request.json
        user = user_service.create(req_json)
        return "", 201, {"location": f'/users/{user.id}'}


@user_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid):
        try:
            user = user_service.get_one(uid)
            return user_schema.dump(user), 200
        except Exception:
            return "", 404

    def put(self, uid):
        req_json = request.json
        req_json["id"] = uid
        user_service.update(req_json)
        return "", 204

    def delete(self, uid):
        user_service.delete(uid)
        return "", 204


