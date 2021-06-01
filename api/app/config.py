import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_ECHO = True # 會把查詢語句打印到console中。


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_URI')
    SQLALCHEMY_ENGINE_OPTIONS = {
            'pool_size':0,
            'max_overflow':20,
            'encoding':'utf-8',
            'pool_timeout':60, 
            'pool_recycle':299,
            'pool_pre_ping': True
            }


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('URI')
    SQLALCHEMY_ENGINE_OPTIONS = {
            'pool_size':0,
            'max_overflow':20,
            'encoding':'utf-8',
            'pool_timeout':60, 
            'pool_recycle':299,
            'pool_pre_ping': True
            }


app_config = {
    'testing': TestingConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig
}