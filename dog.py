# first install the external lib using pip (python -m pip install requests)
import requests

api_url = "http://shibe.online/api/shibes?count=1"

params = {"count": 10}
response = requests.get(api_url, params=params)

status_code = response.status_code
print(f"status code is {status_code}")

response_json = response.json()
print(f"response json {response_json}")