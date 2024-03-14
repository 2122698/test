from flask import Flask, jsonify, request, make_response, render_template, send_from_directory, Response
from flask_cors import CORS
import json
import logging
from werkzeug.utils import secure_filename
# from controller.admin_handler import admin_operations, default_admin
# from controller.usermanagement import check_user, user_api

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['Access-Control-Allow-Credentials'] = True
logger = logging.getLogger(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, world!'})
    

if __name__ == '__main__':
    try:
        app.run(
            host="0.0.0.0",
            debug=True,
            port=8080
        )
    except Exception as ex:
        logger.error(f" Exception while running app.py {ex}")