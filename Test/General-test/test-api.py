import time
from flask import Flask, render_template, flash, redirect, request, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    data = request.get_json()
    print(data)
    username = data["username"]
    email = data["email"]

    return jsonify({"username": username, "email": email, "Recieved": "YES"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
