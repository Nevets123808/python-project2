from flask import Flask, Response, jsonify
from random import sample

app = Flask(__name__)

def tagSkills(skills):
    tags = sample(skills, k=3)
    dict= {}
    for index in range(3):
        dict[f"tag{index+1}"] = tags[index]
    return dict

@app.route('/skilltag')
def skilltag():
    skills = ["Small Guns", "Big Guns", "Energy Weapons", "Unarmed", "Melee Weapons", "Throwing", "First Aid", "Doctor", "Sneak", "Lockpick", "Steal", "Traps", "Science", "Repair", "Speech", "Barter", "Gambling", "Outdoorsman"]
    return jsonify(tagSkills(skills))

if __name__ == "__main__":
    app.run(debug= True, host = '0.0.0.0')