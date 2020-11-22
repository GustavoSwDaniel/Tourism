import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL','postgres://tourism:tourism@localhost:5432/tourism')


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL','postgres://tourism_test:tourism_test@localhost:5432/tourism_test')
    DEBUG = True


class ProductionConfig(Config):
    TESTING = False
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
