from flask import Flask
from flask import request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/echo', methods=['POST'])
def echo():
    data_file = request.json.get('file')
    data_net_info = request.json.get('network_info')
    data_speed_test = request.json.get('speed_test')

    return jsonify({'file': data_file,
                    'network_info': data_net_info,
                    'speed_test': data_speed_test})

if __name__ == '__main__':
    app.debug = True
    app.run()