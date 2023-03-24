from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def start(): 
    return render_template('start.html')
    
@app.route("/gestionUser")
def gestionUser(): 
    return render_template('gestionUser.html')

@app.route("/detailUser")
def detailUser(): 
    return render_template('detailUser.hmtl')