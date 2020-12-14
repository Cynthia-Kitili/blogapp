import os


class Config:
    """Main configurations class"""

    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://cynthia:gitz254@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("EMAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
    SUBJECT_PREFIX = 'BLOGAPP'
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
