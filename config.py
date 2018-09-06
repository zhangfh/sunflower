import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Wtf012'
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = os.environ.get('FLASK_MAIL_SENDER')
    FLASKY_ADMIN = os.environ.get('FLASK_ADMIN')

    mysql_password = os.getenv('FLASK_MYSQL_PASSWORD') or 'default'
    mysql_url = 'mysql://root:' + mysql_password + '@localhost/sunflower'
    SQLALCHEMY_DATABASE_URI = mysql_url
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('FLASK_MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('FLASK_MAIL_PASSWORD')
    FLASKY_MAIL_SENDER = os.environ.get('FLASK_MAIL_SENDER')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Register]'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    @staticmethod
    def init_app(app):
        print("DevelopmentConfig init_app")
 
class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    PRODUCTION = True

config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'production' : ProductionConfig,
    'default' : DevelopmentConfig
}
