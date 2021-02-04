import os
import unittest
from pymongo import MongoClient
from datetime import datetime
from flask import Flask

app = Flask(__name__)


def __init__(self, name=None, host='127.0.0.1', port=27017, clients=None):

    self.clients = dict()

    # Init default values
    self.last_client = None
    self.last_db = None
    self.last_collection = None
    self.runner = []

    if clients:
        for name, client in clients.items():
            self.addClient(client, name)
    elif name:
        self.addClient(MongoClient(host, port), name)


scholarship = {
    "scholarship_name": "Create-A-Greeting-Card Scholarship",
    "scholarship_sponsor": "The Gallery Collection",
    "category": "College",
    "scholarship_amount": "10,000",
    "scholarship_url":
        "https://www.gallerycollection.com/greeting-cards-scholarship.htm",
    "scholarship_deadline": "2021-03-09",
    "date_winner_announced": "2021-05-17",
    "note": "Submit original photo, artwork or computer graphics for the front of a greeting card.",
    "dates": {
        "date_applied": "2000-01-01",
        "date_awarded": "2000-01-01",
        "date_rejected": "2000-01-01",
        "date_declined": "2000-01-01"
        },
    "application_status": "Information",
    "scholarship_status": "Active",
    "created_by": "alivia@example.com",
    "create_date": datetime.now()
    }

datafilter = [
    {
     "scholarship_name": "Hunter Garner Scholarship (Video)",
     "scholarship_sponsor": "Project Yellow Light",
     "category": "College",
     "scholarship_amount": "8,000",
     "scholarship_url": "https://projectyellowlight.com/",
     "scholarship_deadline": "2021-04-01",
     "date_winner_announced": "2021-05-30",
     "note": "create a PSA to encourage your friends to avoid distracted driving",
     "dates": {
        "date_applied": "2000-01-01",
        "date_awarded": "2000-01-01",
        "date_rejected": "2000-01-01",
        "date_declined": "2000-01-01"
        },
     "application_status": "Information",
     "scholarship_status": "Active",
     "created_by": "alivia@example.com",
     "create_date": datetime.now()
    },
    {
     "scholarship_name": "Create-A-Greeting-Card Scholarship",
     "scholarship_sponsor": "The Gallery Collection",
     "category": "College",
     "scholarship_amount": "10,000",
     "scholarship_url":
     "https://www.gallerycollection.com/greeting-cards-scholarship.htm",
     "scholarship_deadline": "2021-03-09",
     "date_winner_announced": "2021-05-17",
     "note": "Submit original photo, artwork or computer graphics for the front of a greeting card.",
     "dates": {
        "date_applied": "2020-07-09",
        "date_awarded": "2000-01-01",
        "date_rejected": "2000-01-01",
        "date_declined": "2000-01-01"
        },
     "application_status": "Information",
     "scholarship_status": "Active",
     "created_by": "alivia@example.com",
     "create_date": datetime.now()
    },
    {
     "scholarship_name": "Hunter Garner Scholarship (Billboard)",
     "scholarship_sponsor": "Project Yellow Light",
     "category": "College",
     "scholarship_amount": "2,000",
     "scholarship_url": "https://projectyellowlight.com/",
     "scholarship_deadline": "2021-05-01",
     "date_winner_announced": "2021-05-30",
     "note": "create a PSA to encourage your friends to avoid distracted driving",
     "dates": {
        "date_applied": "2020-07-09",
        "date_awarded": "2000-01-01",
        "date_rejected": "2000-01-01",
        "date_declined": "2000-01-01"
        },
     "application_status": "Applied",
     "scholarship_status": "Active",
     "created_by": "alivia@example.com",
     "create_date": datetime.now()
    },
    {
     "scholarship_name": "Hunter Garner Scholarship (Radio Ad)",
     "scholarship_sponsor": "Project Yellow Light",
     "category": "College",
     "scholarship_amount": "2,000",
     "scholarship_url": "https://projectyellowlight.com/",
     "scholarship_deadline": "2021-04-01",
     "date_winner_announced": "2021-05-30",
     "note": "create a PSA to encourage your friends to avoid distracted driving",
     "dates": {
        "date_applied": "2000-01-01",
        "date_awarded": "2000-01-01",
        "date_rejected": "2000-01-01",
        "date_declined": "2000-01-01"
        },
     "application_status": "Information",
     "scholarship_status": "Active",
     "created_by": "alivia@example.com",
     "create_date": datetime.now()
    }
]


class TestAppSearch(unittest.TestCase):
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

    # test search
    def test_search(self):
        self.scholarship_coll.delete_one()
        self.scholarship_coll.insert(datafilter)
        self.scholarship_coll.create_index([("$**", 'text')])
        scholarships = self.scholarship_coll.find(
            {"$text": {"$search": "Hunter"}})
        count = scholarships.count()
        self.assertEqual(count, 3)


if __name__ == '__main__':
    unittest.main()
