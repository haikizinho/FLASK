from flask import Flask, render_template

app = Flask("__name__")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html")


