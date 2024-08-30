from functools import wraps
from flask import  request, jsonify, g



def image_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        # if user is not logged in, redirect to login page    
        if not request.files['upload']:
            return jsonify({"success": False, "message": "No Imagen"}), 400
        return f(*args, **kwargs)
    return wrap




