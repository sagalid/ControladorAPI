import requests
import json

api_url = "http://localhost:58000/api/v1/ticket"
headers = {"content-type": "application/json"}

body_json = {
    "username": "admin",
    "password": "admin123!"
}
resp = requests.post(api_url, json.dumps(body_json), headers=headers, verify=False)

response_json = resp.json()
serviceTicket = response_json["response"]["serviceTicket"]
print("El ticket del servicio es: " + serviceTicket)
