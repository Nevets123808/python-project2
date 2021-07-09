from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    SPECIALresponse = requests.get("http://specialgen:5000/genspecial")
    SkillTagresponse = requests.get("http://skilltag:5000/skilltag")
    chardict = {"SPECIAL": dict(SPECIALresponse.text), skillTag: dict(SKillTagresponse.text)}
    sheetmakeresponse = requests.post("http://sheetmake:5000/sheetmake")
    return chardict["special"]["S"]

if __name__ == "__main__":
    app.run(debug= True, host = '0.0.0.0')