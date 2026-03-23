from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/student-details', methods=['GET'])
def get_details():
    return jsonify({
        "name": "Ch.Mounika",
        "roll_number": "223",
        "register_number": "2023BCS0023"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)