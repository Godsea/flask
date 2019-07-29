class Config:
    SECRET_KEY = '1234'

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI= "mysql+pymysql://root:123456@172.16.0.206:3306/aa"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app_type = {
    'development': DevelopmentConfig,
    # 'testing': TestConfig,
    # 'production': ProductionConfig,
    'default': DevelopmentConfig
}