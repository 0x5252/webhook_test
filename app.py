"""
simple webhook using flask
"""

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():
    print("webhook called")
    data = request.get_json()
    print(data)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)
