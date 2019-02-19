from flask import Flask
from flask_cors import CORS
from flask import jsonify
from flask import request
from redis_operations import RedisOperations
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST', 'GET'])
def chat():
    redi_ = RedisOperations()
    if request.method == 'GET':
        return jsonify(result=redi_.get_messages())

    if request.method == 'POST':
        return jsonify(result=redi_.save_message(username=request.json['username'],
                                                 message=request.json['message']))


if __name__ == '__main__':
    app.run(host=config['APPSERVER']['HOST'], port=config['APPSERVER']['PORT'], debug=config['APPSERVER']['DEBUG'])
