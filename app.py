# app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

latest_command = None

@app.route('/trigger', methods=['POST'])
def set_command():
    global latest_command
    data = request.get_json()
    command = data.get("command")
    if command:
        latest_command = command
        return jsonify({"status": "command received", "command": command})
    else:
        return jsonify({"error": "No command provided"}), 400

@app.route('/check', methods=['GET'])
def check_command():
    global latest_command
    if latest_command:
        return jsonify({"command": latest_command})
        latest_command = None
    else:
        return jsonify({"command": None})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
