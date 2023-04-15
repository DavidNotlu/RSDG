from . import db
import random
from .import drinks
from flask_login import UserMixin
from sqlalchemy.sql import func

random_val = ["1", "2"]
def getDrink(val1, val2, val3):
        if(val1 == "1"):
            rdrink = random.choice(random.choice(drinks.hot_drink))
            if(val2 == "1"):
                 drink = random.choice(random.choice(drinks.hot_caf))
            elif(val2 == "2"):
                 drink = random.choice(random.choice(drinks.hot_decaf))
            if(val3 == "1"):
                 syrup = random.choice(drinks.hot_syrup)
                 drink = syrup + " " + rdrink
            else:
                 drink = random.choice(random.choice(drinks.hot_drink))
        elif(val1 == "2"):
             drink = random.choice(random.choice(drinks.iced_drink))
        else:
             v1 = random.choice(random_val)
             v2 = random.choice(random_val)
             v3 = random.choice(random_val)
             getDrink(v1, v2, v3)
        print(drink)
        return drink

class Drink():
    def __init__(self, article, name):
        self.article = article
        name = name = name
        drink.append(self)
    def get(self):
        return self.article, self.name
    
# Defines User 
# TODO: Create random drink instead of "note" to generate the drink
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    
