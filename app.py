from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/sayHello", methods=["GET"])
def say_hello():
    return jsonify({"message": "Hello User"})

if __name__ == "__main__":
    # Use port 5000 for testing; change to 80 if running with sudo
    app.run(host="0.0.0.0", port=5000)
