from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/status")
def status():
    return jsonify({
        "step": 2,
        "help": False
    })

if __name__ == "__main__":
    app.run()
