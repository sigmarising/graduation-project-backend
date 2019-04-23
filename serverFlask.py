import os
import json
import settings
from flask import Flask, request, jsonify, abort

# Path settings
SERVER_PATH = os.path.abspath(os.path.dirname(__file__))
STATIC_PATH = os.path.abspath(os.path.join(SERVER_PATH, 'static'))

# Flask app settings
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/api/v1/charSummary', methods=['GET', 'PUT', 'POST', 'DELETE'])
def api_v1_char_summary():
    if request.method == 'GET':
        summary_path = os.path.abspath(os.path.join(STATIC_PATH, 'data/character_summary'))
        output = {}
        for file in os.listdir(summary_path):
            file_path = os.path.abspath(os.path.join(summary_path, file))
            with open(file_path, 'r', encoding='utf-8') as f:
                output[file.split('.')[0]] = json.load(f)
        return jsonify(output)
    else:
        abort(400)


if __name__ == '__main__':
    print(STATIC_PATH)
    app.run(debug=settings.DEBUG)
