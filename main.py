from flask import Flask, jsonify, request
from flask_cors import CORS
from gpiozero import LED

app = Flask(__name__)
CORS(app)

pins = {
    # Stick
    'LEFT': LED(18),
    'UP': LED(23),
    'RIGHT': LED(24),
    'DOWN': LED(25),
    # Action Buttons
    'B1': LED(17), # Button 1
    'B2': LED(27),
    'B3': LED(22),
    # Start & Coin
    'COIN': LED(5),
    'START': LED(6)
}

for key in pins:
    pins[key].on()

@app.route('/switch', methods=['POST'])
def switch():
    json_request = request.get_json()
    pin_num = json_request.get('pin')
    pressed = json_request.get('pressed')

    pin = pins[pin_num]
    pin.off() if pressed else pin.on()

    return jsonify({
        'status': 'ok'
    })

app.run(host="0.0.0.0", port="5001", debug=False)
