import time
db = [

]


def send_message(text, name):
    db.append({
        'text': text,
        'name': name,
        'time': time.time()
    })


def get_messages(after):
    filtered_db = []
    for message in db:
        if message['time'] > after:
            filtered_db.append(message)
    return filtered_db
