from flask import Flask, json
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import URL
from sqlalchemy import create_engine

db = SQLAlchemy()

__db_host = os.getenv('DB_HOST')
__db_port = os.getenv('DB_PORT')
__db_user = os.getenv('DB_USER')
__db_pass = os.getenv('DB_PASS')
__db_name = os.getenv('DB_NAME')


__sqlalchemy_database_uri = URL.create(
    'mysql+pymysql://',
    username=__db_user,
    password=__db_pass,
    host=__db_host,
    port=__db_port,
    database=__db_name
)



def init_app(app: Flask):
    create_engine(__sqlalchemy_database_uri)
