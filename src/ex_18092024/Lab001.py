#API Testing
import jsonpath
import requests
import json
import pprint
import jsonpath as jp

url = "https://reqres.in/api/users?page=2"

response  = requests.get(url)

json_response = json.loads(response.content)
print(json_response)
jsonPath = jsonpath.jsonpath(json_response,"data")
print(jsonPath)