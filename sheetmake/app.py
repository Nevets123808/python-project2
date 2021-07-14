from flask import Flask, Response, request, jsonify

app = Flask(__name__)

def falloutSkill(SPECIAL):
    skills = {
        "Small Guns": 35 + SPECIAL["A"],
        "Big Guns": 10 + SPECIAL["A"],
        "Energy Weapons": 10 + SPECIAL["A"],
        "Unarmed": 65 + (SPECIAL["S"] + SPECIAL["A"])//2,
        "Melee Weapons": 55 + (SPECIAL["S"] + SPECIAL["A"])//2,
        "Throwing": 40 + SPECIAL["A"],
        "First Aid": 30 + (SPECIAL["P"] + SPECIAL["I"])//2,
        "Doctor": 15 + (SPECIAL["P"] + SPECIAL["I"])//2,
        "Sneak": 20 + SPECIAL["A"],
        "LockPick": 20 + (SPECIAL["P"] + SPECIAL["A"])//2,
        "Steal": 20 + SPECIAL["A"],
        "Traps": 20 + (SPECIAL["P"]+SPECIAL["A"])//2,
        "Science": 25 + 2*SPECIAL["I"],
        "Repair": 20 + SPECIAL["I"],
        "Speech": 25 + 2*SPECIAL["C"],
        "Barter": 20 + 2*SPECIAL["C"],
        "Gambling": 20 + 3*SPECIAL["L"],
        "Outdoorsman": 5 + (SPECIAL["E"]+SPECIAL["I"])//2,
    }
    return skills

@app.route("/sheetmake", methods = ["POST"])
def makeSheet():
    data_received = request.get_json()
    skills = falloutSkill(data_received["SPECIAL"])
    tags = data_received["skillTag"].values()
    for tag in tags:
        skills[tag] += 20
    return jsonify(skills)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")