from flask import Flask, jsonify, request
from flask_cors import CORS
from gpiozero import LED

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

@app.route('/switch', methods=['POST'])
def switch():
    json_request = request.get_json()
    pin_num = json_request.get('pin')
    pressed = json_request.get('pressed')

    pin = LED(pin_num)
    pin.off() if pressed else pin.on()

    return jsonify({
        'status': 'ok'
    })

app.run(host="0.0.0.0", port="5001", debug=False)
