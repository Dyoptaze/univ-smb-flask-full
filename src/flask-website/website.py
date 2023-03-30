from flask import Flask, request, flash, url_for, redirect, render_template
import requests, json

app = Flask(__name__)

@app.route("/")
def start():
    return render_template('start.html')

@app.route("/gestionUser")
def gestionUser():
    response = requests.get('http://localhost:5000/identity')
    data = response.json()
    return render_template("gestionUser.html", users=data)

@app.route("/detailUser/<id_user>")
def detailUser():
    response = requests.get('https://localhost:5000/identity/', id=id_user)
    data = response.json()
    return render_template ("detailUser.html", user=data)
