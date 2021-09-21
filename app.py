from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello this is Heroku !!"

app.run(host="127.0.0.1", port="9595" ,debug=True)
