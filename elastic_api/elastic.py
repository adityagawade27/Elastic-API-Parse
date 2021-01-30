import configparser
from urllib.parse import urlencode, quote_plus
import requests

class Elastic:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('.config')
        self.es_host = self.config['Default']['EL_HOST']
        self.es_port = self.config['Default']['EL_PORT']
        self.es_index = self.config['Default']['EL_INDEX']
        self.es_url = "http://{0}:{1}/{2}".format(
            self.es_host, self.es_port, self.es_index)

    # Add a document to elasticsearch
    def add_doc(self, data):
        add_url = "{0}/_doc".format(self.es_url)
        headers = {
            "Content-Type": "application/json"
        }
        requests.post(add_url, headers=headers, json=data)

    # Get a document based on Song name 
    def get_doc(self, title):
        json_query = {
            "query": {
                "match": {
                    "title": title
                }
            }
        }        
        url_query = urlencode(json_query, quote_via=quote_plus)

        get_url = "{0}/_search?json={1}".format(self.es_url, url_query)

        resp = request.get(get_url)

        if resp.status_code >= 200:
            print(resp.json())




