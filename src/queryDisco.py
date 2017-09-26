import sys
import os
import json
from watson_developer_cloud import DiscoveryV1


uname ='grantsteinfeld@gmail.com'
pwd = 'Wj2lsS1afbY@y'
collection_id='764ca14b-a55a-4610-8bf7-d5f920d587bb'
configuration_id='f913174b-b194-40b4-86f0-6045dba88e5c'
environment_id='36b8a6fc-5472-4969-b6bf-623950781167'


discovery = DiscoveryV1(
  username=uname,
  password=pwd,
  version="2017-09-01"
)


qopts = {'query': '{query_string}', 'filter': '{filter_string}', ...}
my_query = discovery.query('{environment_id}', '{collection_id}', qopts)
print(json.dumps(my_query, indent=2))

#curl -u "{username}":"{password}"
# 'https://gateway.watsonplatform.net/discovery/api/v1/environments/{environment_id}/collections/{collection_id}*/query?version=2017-09-01&query=enriched_text.entities.text:IBM'
