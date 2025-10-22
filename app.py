import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/sayHello", methods=["GET"])
def say_hello():
    return jsonify({"message": "Hello User"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render provides PORT env variable
    app.run(host="0.0.0.0", port=port)
