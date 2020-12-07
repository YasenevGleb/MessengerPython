import time
from datetime import datetime

from flask import Flask, request, abort

app = Flask(__name__)
load_time = datetime.now()

db = []
names=[]

@app.route("/")
def hello():
    return "Hello, there! <a href='/status'>Статистика</a>"


@app.route("/status")
def status():
    return {
        "db": len(db),
        "time": datetime.now().strftime('%H:%M:%S %d/%m/%Y'),
        "name": len(names)
    }

@app.route("/yourname",methods=['POST'])
def checknames():
    name=request.json.get('name')
    if name not in names:
        names.append(name)
        return  {'ok': True}
    else: return abort(400)



@app.route("/send", methods=['POST'])
def send_message():
    if not isinstance(request.json, dict):
        return abort(400)

    text = request.json.get('text')
    name = request.json.get('name')
    if not isinstance(text, str) or not isinstance(name, str):
        return abort(400)
    if text == '' or name == '':
        return abort(400)

    db.append({
        'text': text,
        'name': name,
        'time': time.time()
    })
    return {'ok': True}


@app.route("/messages")
def get_messages():
    if 'after' in request.args:
        try:
            after = float(request.args['after'])
        except:
            print('error')
            return abort(400)
    else:
        after = 0

    filtered_db = []
    for message in db:
        if message['time'] > after:
            filtered_db.append(message)
            if len(filtered_db) >= 100:
                break

    return {'messages': filtered_db}


app.run()
