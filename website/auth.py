from flask import Blueprint
#Creates login page and user authorization

auth = Blueprint('auth', __name__) #Define blueprint

@auth.route('/login')
def login():
    return

@auth.route('/logout')
def logout():
    return 

@auth.route('/create-account')
def create_account():
    return
