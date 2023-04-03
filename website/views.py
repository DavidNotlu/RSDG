from flask import Blueprint

views = Blueprint('views', __name__) #Define blueprint to organize urls from main page of randomizer

@views.route('/')
def home():
    pass