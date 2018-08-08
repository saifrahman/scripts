#!/usr/bin/env python3

import requests
import json
import gzip
import time

kairosdb_server = "http://localhost:8080"

# Simple test [without compression]
data = [
    {
        "name": "test_metrics",
        "datapoints": [
            [int(round(time.time() * 1000)), 80],
            [int(round(time.time() * 1000))+1, 40.2],
            [int(round(time.time() * 1000))+2, 63.1]
        ],
        "tags": {
            "project": "artume"
        }
    }
]

response = requests.post(kairosdb_server + "/api/v1/datapoints", json.dumps(data))
print("Simple test [without compression]: \t%d (status code)" % response.status_code )

# Complex test [gzipping before send to KairosDB]
data = [
    {
        "name": "metrics_gzip",
        "datapoints": [
            [1359788400000, 10],
            [1359788300000, 11.223],
            [1359788410000, 24.09]
        ],
        "tags": {
            "project": "test_gzip",
        }
    }
]
gzipped = gzip.compress(bytes(json.dumps(data), 'UTF-8'))

headers = {'content-type': 'application/gzip'}
#response = requests.post(kairosdb_server + "/api/v1/datapoints", gzipped, headers=headers)
#print("Complex test [with compression]: \t%d (status code)" % response.status_code)
