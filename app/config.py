# конфиги
class Config:
    SECRET = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2, 'sort_keys': False}
    DEBUG = True
