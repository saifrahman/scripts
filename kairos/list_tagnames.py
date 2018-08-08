#!/usr/bin/env python3

import requests
import json

kairosdb_server = "http://localhost:8080"


response = requests.get(kairosdb_server + "/api/v1/tagnames")
print("Status code: %d" % response.status_code)
print("JSON response:")
print(response.json())
