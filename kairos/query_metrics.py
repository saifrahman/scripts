#!/usr/bin/env python3

import requests
import json

kairosdb_server = "http://localhost:8080"

query = {
   "start_absolute": 0,
   "metrics": [
       {
           "tags": {
               "project": "artume",
           },
           "name": "test_metrics",
           "limit": 10000
       }
   ]
}
response = requests.post(kairosdb_server + "/api/v1/datapoints/query", data=json.dumps(query))
print("Status code: %d" % response.status_code)
print("JSON response:")
print(response.json())
