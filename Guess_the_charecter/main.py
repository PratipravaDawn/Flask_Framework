from flask import Flask, render_template
import requests

app = Flask(__name__)


def genderize(name):
    responce = requests.get(f"https://api.genderize.io/?name={name}")
    gender = responce.json()
    return gender["gender"]


def ageify(name):
    responce = requests.get(f"https://api.agify.io?name={name}")
    gender = responce.json()
    return gender["age"]


@app.route("/")
def home():
    return "write guess"


@app.route("/guess/")
def guess():
    return "write your name"


@app.route("/guess/<name>")
def realshit(name):
    name = name.lowercase
    real_gender = genderize(name)
    real_age = ageify(name)
    real_name = name.title()
    return render_template("name.html", n=real_name, g=real_gender, a=real_age)

if __name__ == "__main__":
    app.run(debug=True)