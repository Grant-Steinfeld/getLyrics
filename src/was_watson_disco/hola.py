import sys
import os
import json
from watson_developer_cloud import DiscoveryV1

kreds = {
  "url": "https://gateway.watsonplatform.net/discovery/api",
  "username": "bf1712bc-0662-4a46-8d44-23177008419f",
  "password": "08ygudOQ4rbj"
}


discovery = DiscoveryV1(
  username= kreds['username'],
  password=kreds['password'],
  version='2017-10-16'
)



with open((os.path.join(os.getcwd(), '{path_element}', '{filename}' as fileinfo:
  add_doc = discovery.add_document('{environment_id}', '{collection_id}', file_info=fileinfo)
print(json.dumps(add_doc, indent=2))