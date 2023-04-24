from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
from . import drinks
from .models import Drink, getDrink
import json

views = Blueprint('views', __name__)

# TODO: If the user refeshes after being signed in they will be redirected to the welcome page; they should be directed to the home page


@views.route('/')
def welcome():
    return render_template("welcome.html", user=current_user)


@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    thisDrink = ""
    if request.method == 'POST':
        val1 = request.form.get("temp")
        val2 = request.form.get("caf")
        val3 = request.form.get("sweet")
        thisDrink = getDrink(val1, val2, val3)
    return render_template("home.html", user=current_user, drink=thisDrink)
