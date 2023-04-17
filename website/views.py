from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
from . import drinks
from .models import Drink, getDrink
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    val1 = request.form.get("temp")
    val2 = request.form.get("caf")
    val3 = request.form.get("sweet")
    if request.method == 'POST': 
        pass
    return render_template("home.html", user=current_user, drink=getDrink(val1, val2, val3))

