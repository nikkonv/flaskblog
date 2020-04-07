import os 

class Config:
    SECRET_KEY = '6075aa775d03746e78358597aa23176e1e9c7a2f7125720f91f23250de8ece34'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('USER_EMAIL')
    MAIL_USERNAME = os.getenv('USER_PASS')