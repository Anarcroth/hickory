import requests

BASE_URL = "http://localhost:5000"
print(requests.get(BASE_URL).status_code)
print(requests.get(BASE_URL+"/user/1"))
print(requests.get(BASE_URL+"/route/6"))