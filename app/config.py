import os


class Config:
    """Main configurations class"""

    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://cynthia:gitz254@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "gitz254"
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'nyambucindy0@gmail.com'
    MAIL_PASSWORD = 'tuit1436'
    SUBJECT_PREFIX = 'BLOG'
    SENDER_EMAIL = 'nyambucindy0@gmail.com'

 # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cynthia:gitz254@localhost/blog'
    DEBUG = True


class TestConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cynthia:gitz254@localhost/blog_test'


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
