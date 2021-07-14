from flask import url_for
from flask_testing import TestCase
from app import app
class TestBase(TestCase):
    def create_app(self):
        return app

class test_specialgen(TestBase):
    def test_response(self):
        response = self.client.get(url_for("genspecial"))
        data = eval(response.data.decode("utf-8"))
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(data),7)