from flask import Flask
from random import choices

def tagSkills(skills):
    tags = choices(skills, k=3)
    dict= {}
    for index in range(3):
        dict[f"tag{index+1}"] = tags[index]
    return dict

skills = ["Small Guns", "Big Guns", "Energy Weapons", "Unarmed", "Melee Weapons", "Throwing", "First Aid", "Doctor", "Sneak", "Lockpick", "Steal", "Traps", "Science", "Repair", "Speech", "Barter", "Gambling", "Outdoorsman"]

print(tagSkills(skills))