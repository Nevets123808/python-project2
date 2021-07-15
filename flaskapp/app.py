from flask import Flask, jsonify
from flask-sqlalchemy import SQLAlchemy
from os import getenv
import requests

app = Flask(__name__)

app.config("SQL_ALCHEMY_DATABASE_URI") = getenv("DATABASE_URI")
@app.route('/')
@app.route('/home')
def home():
    SPECIALresponse = requests.get("http://specialgen:5000/genspecial")
    SkillTagresponse = requests.get("http://skilltag:5000/skilltag")
    print(SPECIALresponse.json()["S"])
    chardict = {"SPECIAL": SPECIALresponse.json(), "skillTag": SkillTagresponse.json()}
    
    sheetmakeresponse = requests.post("http://sheetmake:5000/sheetmake", json = chardict)
    chardict["skills"] = sheetmakeresponse.json()
    return chardict

if __name__ == "__main__":
    app.run(debug= True, host = '0.0.0.0')