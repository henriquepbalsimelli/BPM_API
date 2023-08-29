import os
from flask import Flask, json
from flask_sqlalchemy import SQLAlchemy
import logging
db = SQLAlchemy()

__db_host = os.getenv('DB_HOST')
__db_port = os.getenv('DB_PORT')
__db_user = os.getenv('DB_USER')
__db_pass = os.getenv('DB_PASS')
__db_name = os.getenv('DB_NAME')


def init_app(app: Flask):
    try:
        __sqlalchemy_database_uri='mysql://{user}:{password}@{server}:{port}/{database}'.format(user=__db_user, password=__db_pass, server=__db_host, port=__db_port, database='BPM')
        
        app.config['SQLALCHEMY_DATABASE_URI'] = __sqlalchemy_database_uri
        app.config['SQLALCHEMY_BINDS'] = {
            'BPM': __sqlalchemy_database_uri
        }
        app.config['SQLALCHEMY_ECHO'] = False
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        db.init_app(app)
    except Exception as error:
        logging.exception(error)