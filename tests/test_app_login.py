import unittest
import env
import os
from pymongo import MongoClient
from app import app


class TestAppLogin(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # create mongo connection to mock server
        app.testing = True
        self.mongo_client = MongoClient(os.environ.get('TEST_MONGODB_URI'))
        self.app = app.test_client()
        self.db = self.mongo_client['test_Scholarships']
        self.scholarship_coll = self.db['scholarship']
        self.category_coll = self.db['categories']
        self.status_coll = self.db['statuses']

    @classmethod
    def tearDownClass(self):
        self.mongo_client.drop_database('test_Scholarships')

    def register(self, first_name, last_name, username, password):
        return self.app.post("/login", data=dict(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password),
            follow_redirects=True)

    def login(self, username, password):
        return self.app.post("/login", data=dict(
            username=username,
            password=password),
            follow_redirects=True)

    def logout(self):
        return self.app.get("/logout",
                            follow_redirects=True)

    def test_valid_user_registration(self):
        response = self.register("Pat",
                                 "Longwind",
                                 "pat@example.com",
                                 "1student!")
        self.assertEqual(response.status_code, 200)
        # self.assertIn("Registration Successful!", response.data)

    def test_invalid_user_registration(self):
        response = self.register("Pat",
                                 "Longwind",
                                 "pat@example.com",
                                 "awesome")
        self.assertEqual(response.status_code, 200)
        # self.assertIn(b"wrong", response.data)

    def test_login_sucess(self):
        response = self.login("pat@example.com", "1student!")
        self.assertEqual(response.status_code, 200)
        # self.assertIn("Welcome, pat@example.com", response.data)

    def test_login_failure(self):
        response = self.login("pat@example.com", "1tudent!")
        self.assertEqual(response.status_code, 200)
        # self.assertIn("Incorrect Username and/or Password", response.data)


if __name__ == '__main__':
    unittest.main()
