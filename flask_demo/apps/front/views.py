from flask import Blueprint

blue_front = Blueprint('blue_front',__name__)

@blue_front.route('/')
def hello_world():
    return 'hello_worlds'

