import requests
import time
while True:
    response = requests.get("http://127.0.0.1:5000/status")
    print("Time " + str(response.json()["time"]))
    print("Message count " + str(response.json()["db"]))
    print("Users count " + str(response.json()["name"]))
    time.sleep(5)
