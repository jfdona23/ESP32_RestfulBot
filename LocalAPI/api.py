from flask import Flask, jsonify, abort, request
from time import time


response = {'response':'Please submit an order to the robot'}

app = Flask(__name__)


@app.route('/v1/inbound/', methods=['POST'])
def putOrder():
    if not request.json or not 'order' in request.json:
        abort(400)
    else:
        global response
        order = request.json['order']
        if order not in (
            'forward',
            'backward',
            'left',
            'right',
            'stop'
            ):
            abort(400)
        argument= request.json.get('argument', 0)
        response = {'cmd':order, 'arg':argument, 'hash':hash(time())}
        return jsonify({'status': 'received'}), 201

@app.route('/v1/outbound', methods=['GET'])
def getOrder():
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)