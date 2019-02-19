from flask import Flask, request, render_template, Response
from flask_cors import CORS
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
        return render_template('index.html', data=redi_.get_messages())

    if request.method == 'POST':
        redi_.save_message(username=request.form['username'], message=request.form['message'])
        return render_template('index.html', data=redi_.get_messages())


@app.route('/health', methods=['GET'])
def health_check():
    return Response(status=200)


if __name__ == '__main__':
    app.run(host=config['APPSERVER']['HOST'], port=config['APPSERVER']['PORT'], debug=config['APPSERVER']['DEBUG'])
