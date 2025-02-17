import os
import requests
from requests.auth import HTTPBasicAuth
import  urllib3


class DB:
    def __init__(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.db = {}
        self.connect_db()

    def connect_db(self):
        wd = os.path.dirname(__file__)
        with open(os.path.join(wd, '../data/db.properties'), 'r') as file:
            data = file.readlines()
        for d in data:
            key, value = d.split("=")
            self.db[key] = value.strip()
        pass

    # curl -u "user:password" 
    #  -H "Content-Type: application/json"
    #  -XGET "https://<host>:9200/texts/_doc/<id>" 
    def get_bookdata(self, index) -> dict:
        url = f"https://{self.db["host"]}:{self.db["port"]}/texts/_doc/{index}"

        # Make the GET request with authentication
        response = requests.get(
                url,
                auth=HTTPBasicAuth(self.db["user"], self.db["password"]),
                headers={"Content-Type": "application/json"},
                verify=False
        )
        book = response.json()
        return book

    def check_book(self, book) -> bool:
        # fields1 = ["_index", "_id", "_version", "_seq_no", "_primary_term", "found", "_source"]
        # fields2 = ["author", "title", "year", "language", "source", "text", "embeddings"]

        fields1 = ["_index", "_id", "_version", "_source"]
        fields2 = ["author", "title", "year", "language", "text", "embeddings"]
        error = ""

        for f in fields1:
            if not f in book:
                error += f + " not in db\n"
        if "_source" in book:
            for f in fields2:
                if not f in book["_source"]:
                    error += f + " not in _source\n"
        if error != "":
            print(error)
            return False
        return True

    def update_year(self, id, year):
        url = f"https://{self.db['host']}:{self.db['port']}/texts/_update/{id}"
        payload = {
            "doc": {
                "year": year
            }
        }

        response = requests.post(
            url, 
            auth=HTTPBasicAuth(self.db["user"], self.db["password"]), 
            json=payload, 
            headers={"Content-Type": "application/json"},
            verify=False  # Set to True if SSL is properly configured
        )

        if response.status_code == 200:
            # print("Update successful:", response.json())
            return True
        else:
            # print(f"Error {response.status_code}: {response.text}")
            return False











