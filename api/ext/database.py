from flask import Flask, json
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

__db_host = os.getenv('DB_HOST')
__db_port = os.getenv('DB_PORT')
__db_user = os.getenv('DB_USER')
__db_pass = os.getenv('DB_PASS')
__db_name = os.getenv('DB_NAME')

__sqlalchemy_database_uri = 'mysql+pymysql://' + __db_user + ':' + __db_pass + '@' + __db_host + ':' + __db_port + '/' + __db_name


def init_app(app: Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = __sqlalchemy_database_uri
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100, 'pool_recycle': 90, 'json_serializer': json.dumps}

    db.init_app(app)
