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

@app.route("/login", methods = ['POST'])
def login():
    log = request.form['login']
    passwd = request.form['password']
    cur = mysql.connection.cursor()
    cur.execute("SELECT id_user, login FROM Authentification WHERE login = "+log+" and password = "+passwd+";")
    output = cur.fetchall()
    users = []
    for row in output:
        dict = {'id_user':row[0], 'login':row[1]}
        users.append(dict)
    cur.close()
    return jsonify(users)

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

@app.route("/identity/<id_user>")
def userDetail(id_user):
    cur = mysql.connection.cursor()
    cur.execute("SELECT id_user,nom,prenom,naissance FROM Utilisateur WHERE Utilisateur.id_user = "+id_user+";")
    output = cur.fetchone()
    user = []
    user.append({'id_user':output[0], 'nom':output[1], 'prenom':output[2], 'naissance':output[3]})
    cur.close()
    return jsonify(user)