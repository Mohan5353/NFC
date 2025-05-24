# app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

trigger = False

@app.route('/trigger', methods=['POST'])
def set_trigger():
    global trigger
    trigger = True
    return jsonify({"status": "trigger set"})

@app.route('/check', methods=['GET'])
def check_trigger():
    global trigger
    if trigger:
        trigger = False
        return jsonify({"trigger": True})
    else:
        return jsonify({"trigger": False})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
