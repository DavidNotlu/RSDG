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

# TODO: These need to be rewritten to work with the drink generator not "Note"

    #if request.method == 'GET': 
    
    return render_template("home.html", user=current_user, drink=getDrink())


