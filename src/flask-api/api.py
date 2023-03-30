from flask import Flask, request, flash, url_for, redirect, render_template, jsonify
from flask_mysqldb import MySQL
from flask_mysql_connector import MySQL as mysql

app = Flask(__name__)

app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "duvertma"
app.config['MYSQL_DB'] = "identity"

mysql = MySQL(app)

@app.route("/")
def hello():
    return "Hello, API!"

@app.route("/login")
def login():
    return "Hello, API!"

@app.route("/identity")
def identity():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id_user, login FROM Authentification;")
    output = cur.fetchall()
    users = []
    for row in output:
        dict = {'id_user':row[0], 'login':row[1]}
        users.append(dict)
    cur.close()
    return jsonify(users)

@app.route("/identity/<id>")
def userDetail(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Utilisateur WHERE id_user = id;")
    output = cur.fetchall()
    users = []
    for row in output:
        dict = {'id_user':row[0], 'login':row[1]}
        users.append(dict)
    cur.close()
    return jsonify(users)