import re
import requests

# endpoint = "http://httpbin.org/#/Status_codes/200/"
endpoint = "http://httpbin.org/anything"

get_responce =  requests.get(endpoint,json={"query":"Hello world "})   # HTTP request
print(get_responce.text)  # print raw test responce 

# HTTP Request  -> HTML
# REST API HTTP Request -> json 

print(get_responce.json())
print(get_responce.status_code)