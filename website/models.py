from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# Defines User 
# TODO: Create random drink instead of "note" to generate the drink
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
