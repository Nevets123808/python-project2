from flask import Flask
from random import randint
def generateSpecial():
    return [randint(1,10) for _ in range(7)]

app = Flask(__name__)


@app.route("/genspecial")
def genspecial():
    return generateSpecial

if __name__ == "__main__":
    print(generateSpecial())