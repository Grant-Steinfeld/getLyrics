import sys
import os
import json
from watson_developer_cloud import DiscoveryV1

discovery = DiscoveryV1(
  username="{username}",
  password="{password}",
  version="2017-09-01"
)

with open((os.path.join(os.getcwd(), '{path_element}', '{filename}' as fileinfo:
  add_doc = discovery.add_document('{environment_id}', '{collection_id}', file_info=fileinfo)
print(json.dumps(add_doc, indent=2))