from flask import Blueprint

hello_world_bp = Blueprint('hello_world', __name__)


# defining the endpoint
@hello_world_bp.get('/')
def say_hello_world():
    return 'Hello, World!'


# defining the endpoint using the same bp, but this time it returns JSON instead of a string
@hello_world_bp.get('/hello/JSON')
def say_hello_world_json():
    return {
        'name': 'Ada Lovelace',
        'message': 'Hello!',
        'hobbies': ['fishing', 'swimming', 'watching tv']
    }


# defining intentionally broken endpoint
@hello_world_bp.get('/broken-endpoint-with-broken-server-code')
def broken_endpoint():
    response_body = {
        'name': 'Ada Lovelace',
        'message': 'Hello!',
        'hobbies': ['fishing', 'swimming', 'watching tv']
    }

    new_hobby = 'Surfing'
    response_body['hobbies'].append(new_hobby)

    return response_body
