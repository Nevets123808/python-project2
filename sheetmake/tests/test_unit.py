from flask import url_for, jsonify
from flask_testing import TestCase
from app import app
class TestBase(TestCase):
    def create_app(self):
        return app

class test_skilltag(TestBase):
    def test_response(self):
        test_data = {"SPECIAL":{"S":5,"P":5,"E":5,"C":5,"I":5,"A":5,"L":5},"skillTag":{"tag1":"Small Guns","tag2":"Big Guns", "tag3":"Science"}}
        response = self.client.post(url_for("makeSheet"), json = test_data)
        self.assertEqual(200, response.status_code)
        response_skill_values = eval(response.data.decode("utf-8"))
        self.assertEqual( response_skill_values["Small Guns"], 60)