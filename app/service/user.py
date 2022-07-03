import base64
import hashlib
import hmac

from app.dao.user import UserDAO
from app.helpers.constants import PWD_SALT, PWD_ITERATIONS


class UserService:

    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_by_username(self, username, password):
        password_hash = self.generate_password(password)
        return self.dao.get_by_username(username, password_hash)

    def create(self, data):
        data['password'] = self.generate_password(data['password'])
        return self.dao.create(data)

    def update(self, data):
        data['password'] = self.generate_password(data['password'])
        uid = data.get('id')
        user = self.get_one(uid)
        user.username = data.get('username')
        user.password = data.get('password')
        user.role = data.get('role')
        self.dao.update(user)

    def delete(self, uid):
        self.dao.delete(uid)

    def generate_password(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_SALT,
            PWD_ITERATIONS
        )
        return base64.b64encode(hash_digest)

    def compare_passwords(self, password_hash, other_password) -> bool:
        decoded_digest = base64.b64decode(password_hash)
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            other_password.encode(),
            PWD_SALT,
            PWD_ITERATIONS
        )
        return hmac.compare_digest(decoded_digest, hash_digest)
