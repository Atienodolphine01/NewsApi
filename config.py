import os

class Config:
    BASE_URL = 'https://newsapi.org/v2/{}?apiKey={}&{}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # asd='https://newsapi.org/v2/top-headlines?apiKey=12dbjhasdbj&category=business'

class DevConfig(Config):
    DEBUG=True
class ProdConfig(Config):
    DEBUG=False






config_options = {
    'development': DevConfig,
    'production': ProdConfig
}