import sqlite3
from public import app
from flask import g


DATABASE = 'db/matchinfo.db'


def connect_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = convert_row_to_dictionary
    return db