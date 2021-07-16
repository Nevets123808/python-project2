from flask import url_for, jsonify
from flask_testing import TestCase
import requests_mock

from app import app, db, characters
class TestBase(TestCase):
    def create_app(self):
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"
        app.config["SECRET_KEY"] = "agjiwagjkl"
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        return app
    
    def setUp(self):
        db.create_all()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()


class test_skilltag(TestBase):
    def test_response(self):
        with requests_mock.Mocker() as mocker:
            mocker.get("http://specialgen:5000/genspecial", json = {"S":5,"P":5,"E":5,"C":5,"I":5,"A":5,"L":5})
            mocker.get("http://skilltag:5000/skilltag", json = {"tag1":"Small Guns","tag2":"Big Guns", "tag3":"Science"})
            mocker.post("http://sheetmake:5000/sheetmake", json = {"Small Guns": 60,
        "Big Guns": 35,
        "Energy Weapons": 15,
        "Unarmed": 70,
        "Melee Weapons": 60,
        "Throwing": 45,
        "First Aid": 35,
        "Doctor": 20,
        "Sneak": 25,
        "LockPick": 25,
        "Steal": 25,
        "Traps": 25,
        "Science": 55,
        "Repair": 25,
        "Speech": 35,
        "Barter": 30,
        "Gambling": 35,
        "Outdoorsman": 10,})
            response = self.client.get(url_for("home"))
            self.assertEqual(200,response.status_code)
            # self.assertIn(b'"Small Guns":60', response.data)