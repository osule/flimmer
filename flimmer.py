from flask import Flask, render_template, request
from lib.pusher import subscription

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/message", methods=["POST"])
def message():
    subscription.send(request.form.to_dict())
    return "", 200


if __name__ == "__main__":
    app.run(debug=True)
