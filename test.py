import json

import requests

re = requests.get('http://127.0.0.1:5000/scut/jwnotice?name=jw&pageSize=75')
js = json.loads(re.text)
print(js)

