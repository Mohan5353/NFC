from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

COMMAND_FILE = "latest_command.json"

def save_command(command):
    with open(COMMAND_FILE, "w") as f:
        json.dump({"command": command}, f)

def load_command():
    if os.path.exists(COMMAND_FILE):
        with open(COMMAND_FILE, "r") as f:
            return json.load(f).get("command")
    return None

def clear_command():
    if os.path.exists(COMMAND_FILE):
        os.remove(COMMAND_FILE)

@app.route('/trigger', methods=['POST'])
def trigger():
    try:
        # Try to parse as real JSON
        data = request.get_json(force=True)
    except:
        # Fallback: parse from raw_body parameter
        raw_body = request.form.get("raw_body")
        if raw_body:
            data = json.loads(raw_body)
        else:
            return jsonify({"error": "Invalid JSON and no raw_body"}), 400

    command = data.get("command")
    if command:
        print(f"Received command: {command}")
        save_command(command)
        return jsonify({"status": "command received", "command": command}), 200
    else:
        return jsonify({"error": "No command provided"}), 400

@app.route('/check', methods=['GET'])
def check_command():
    command = load_command()
    if command:
        clear_command()  # Optional: clear after check
        return jsonify({"command": command})
    else:
        return jsonify({"command": None})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
