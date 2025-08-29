from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Pattern to check
pattern = re.compile(r'^FileChecker_\d+$')

@app.route("/check", methods=["POST"])
def check_file_pattern():
    data = request.get_json()
    if not data or "input_string" not in data:
        return jsonify({"error": "Please provide 'input_string' in JSON body"}), 400
    
    input_string = data["input_string"]
    
    if pattern.fullmatch(input_string):
        return jsonify({"input_string": input_string, "matches": True})
    else:
        return jsonify({"input_string": input_string, "matches": False})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
