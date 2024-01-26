

import requests
import json

url ='https://www.bbc.co.uk/news/england.json'
r = requests.get(url)
print(f"Status_code: {r.status_code}")

response_dict =r.json()
y = response_dict['content']['groups'][0]['items']
cy = response_dict['content']['groups'][0]['items'][0]['headlines']

readible_file ='Data/readable_bbc_data.json'


for x in cy:
    print(cy['headline'])