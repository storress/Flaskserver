from flask import Flask
from flask import request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/echo', methods=['POST'])
def echo():
    """
    receive data and sent it back

    :return: same json that was sent
    """
    return request.data

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
