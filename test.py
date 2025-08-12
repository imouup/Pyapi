import json

import requests

re = requests.get('http://127.0.0.1:5001/lastUpdated')
js = json.loads(re.text)
print(js)

