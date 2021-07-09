from flask import Flask, Response
from random import randint
def generateSpecial():
    values = [randint(1,10) for _ in range(7)]
    SPECIAL = ["S", "P", "E", "C", "I", "A", "L"]
    dict = {}
    for index, value in enumerate(values):
        dict[SPECIAL[index]] = value
    return dict
app = Flask(__name__)


@app.route("/genspecial")
def genspecial():
    return Response(str(generateSpecial()))

if __name__ == "__main__":
    app.run(debug= True, host = '0.0.0.0')