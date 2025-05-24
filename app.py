# app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

latest_command = None

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
        # Log or handle command
        print(f"Received command: {command}")
        return jsonify({"status": "command received", "command": command}), 200
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
