from flask import Flask
from flask import request

app = Flask(__name__)



@app.route('/')
def index():
    return 'index'


@app.route('/echo', methods=['POST'])
def echo():
    data = request.json
    return str(data)

if __name__=='__main__':
    app.debug = True
    app.run()