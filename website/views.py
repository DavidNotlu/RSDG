from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Drink
from .functions import getDrink
from . import db, drinks
import json


views = Blueprint('views', __name__)
thisDrink = ""


@views.route('/', methods=['GET', 'POST'])
def welcome():
    if current_user.is_authenticated:
        thisDrink = ""
        return render_template("home.html", user=current_user, drink=thisDrink)
    else:
        return render_template("welcome.html")


@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        val1 = request.form.get("temp")
        val2 = request.form.get("caf")
        val3 = request.form.get("sweet")
        global thisDrink
        thisDrink = getDrink(val1, val2, val3)

    return render_template("home.html", user=current_user, drink=thisDrink)


@views.route('/my_drinks', methods=['GET', 'POST'])
@login_required
def my_drinks():
    if request.method == 'POST':
        rating = request.form.get('rating')  # Gets the note from the HTML

        # providing the schema for the note
        new_drink = Drink(
            data=rating, user_id=current_user.id, image=thisDrink)
        db.session.add(new_drink)  # adding the note to the database
        db.session.commit()
        flash('Drink added!', category='success')
        return render_template("my_drinks_read_only.html", user=current_user, name=thisDrink)

    return render_template("my_drinks.html", user=current_user, name=thisDrink)


@views.route('/my_drinks_read_only', methods=['GET', 'POST'])
@login_required
def my_drinks_read_only():
    return render_template("my_drinks_read_only.html", user=current_user)


@views.route('/delete-drink', methods=['POST'])
def delete_drink():
    drink = json.loads(request.data)
    drinkId = drink['drinkId']
    drink = Drink.query.get(drinkId)
    if drink:
        if drink.user_id == current_user.id:
            db.session.delete(drink)
            db.session.commit()

    return jsonify({})
