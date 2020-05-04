from flask import Blueprint, jsonify

# Create the blueprint
mod = Blueprint('apis', __name__)

# Home endpoint
@mod.route('/')
def home_api():
    return jsonify({'message': 'hello world!'})

# About endpoint
@mod.route('/about')
def about():
    return jsonify({'message':'Python flask \'Blueprints\' hello world'})
