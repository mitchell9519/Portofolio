import requests
import json

url ='https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status_code: {r.status_code}")

response_dict =r.json()
readible_file ='Data/readable_hn_data.json'

with open(readible_file,'w') as file_object:
    json.dump(response_dict,file_object,indent=4)

