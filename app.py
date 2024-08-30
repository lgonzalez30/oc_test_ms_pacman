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



port = int(os.environ.get('PORT', 5001))
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)