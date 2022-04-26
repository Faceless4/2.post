import requests
import time
import json

from config import url

n=int(input())
d1 = {
    "ident": "1234",
    "timestamp": time.time()
}
request=[d1]
for i in range(10):
# params = '[{"ident":"1234", "timestamp":' + str(time.time()) + '}]'
    params = json.dumps(request)
    requests.post(url, data=params)
    time.sleep(n)
print(params)

