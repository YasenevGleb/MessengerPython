import requests


while True:
    print("Hello,what`s ur name?")
    name=input()
    req=requests.post('http://127.0.0.1:5000/yourname',json={"name":name})
    if req.status_code==200:
        break


while True:
    text = input()
    requests.post(
        'http://127.0.0.1:5000/send',
        json={'text': text, 'name': name}
    )
