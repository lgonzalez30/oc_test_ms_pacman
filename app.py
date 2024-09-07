# app.py

# Required imports
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
# Initialize Flask app  
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)



@app.route('/v1/alive', methods=['GET'])
def alive():
    return  jsonify({'message': 'OK', 'status': True}), 200


@app.route('/v1/tasks', methods=['GET'])
def tasks():
    return jsonify([{'nombre': 'task 1', 'hora': '10:30:00','done': True}, {'nombre': 'task 2', 'hora': '10:40:00', 'done':False}]), 200

port = int(os.environ.get('PORT', 5001))
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)
    
    
    

