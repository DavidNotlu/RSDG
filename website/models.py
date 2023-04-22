from . import db
import random
from .import drinks
from flask_login import UserMixin
from sqlalchemy.sql import func

random_val = ["1", "2"]


def getDrink(val1, val2, val3):
    if (val1 == "1"):
        drink = random.choice(random.choice(drinks.hot_drink))
        if (val2 == '1'):
            drink = random.choice(random.choice(drinks.hot_caf))
        elif (val2 == '2'):
            drink = random.choice(random.choice(drinks.hot_decaf))
        if (val3 == "1"):
            syrup = random.choice(drinks.hot_syrup)
            return drink + " with " + syrup + " Syrup"
    elif (val1 == "2"):
        drink = random.choice(random.choice(drinks.iced_drink))
        if (val2 == "1"):
            drink = random.choice(random.choice(drinks.iced_caf))
        elif (val2 == "2"):
            drink = random.choice(random.choice(drinks.iced_decaf))
            return drink
        if (val3 == "1"):
            syrup = random.choice(drinks.iced_syrup)
            return drink + " with " + syrup
    else:
        val1 = random.choice(random_val)
        val2 = random.choice(random_val)
        val3 = random.choice(random_val)
        drink = getDrink(val1, val2, val3)

    return drink

# Drink database, this implementation can change as we go


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    # rating is for the star rating that may or may be present
    rating = db.Column(db.Integer)
    note = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # image will be a string that is the path to the image
    image = db.Column(db.String(1000))

    def __init__(self, article, name):
        self.article = article
        self.name = name

    def get(self):
        return self.article, self.name

# Defines User
# TODO: Create random drink instead of "note" to generate the drink


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    drinks = db.relationship('Drink')
