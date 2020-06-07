# -*- coding: utf-8 -*-
import time

from datetime import datetime

from flask import Flask, request

import COVID19Py
covid19 = COVID19Py.COVID19()

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

messages = [
    {'username': 'Jack', 'text': 'Hello', 'timestamp': time.time()},
    {'username': 'Bot', 'text': 'Для вызова бота наберите /corona', 'timestamp': time.time()},
]

users = {
    'Jack': '123456',
    'Jack2': '123456',
}


@app.route('/')
def hello_world():
    return 'Сервер ОК,<a href="/status"> Статус сервера</a> '


@app.route('/status')
def status():
    count_message = len(messages)
    count_users = len(users)

    return {
        'status': True,
        'name': 'UltraMess',
        'Time': datetime.now().strftime('%H:%M:%S %d/%m/%y'),
        'current_time_seconds': time.time(),
        'Всего сообщений на сервере: ': count_message,
        'Всего пользователей на сервере ': count_users,
    }


@app.route('/send_message')
def send_message():
    print(request.json)
    username = request.json['username']
    password = request.json['password']
    text = request.json['text']

    if username in users:
        if users[username] != password:
            return {'ok': False}
    else:
        users[username] = password

    messages.append({'username': username, 'text': text, 'timestamp': time.time()})
    if text == '/corona':
        latest = covid19.getLatest()
        latest_conf = latest['confirmed']
        latest_RU = covid19.getLocationByCountryCode("RU")
        confirmed_RU = (latest_RU[0]['latest']['confirmed'])
        message_bot = f'Всего зараженных в мире {latest_conf} человек, в т.ч. числе в России {confirmed_RU} человек ' \
                      f'Берегите себя! Оставайтесь дома!'

        messages.append({'username': 'Bot', 'text': message_bot, 'timestamp': time.time()})
    return {
        'ok': True,
    }


@app.route('/get_messages')
def get_message():
    after = float(request.args['after'])
    result = []

    for message in messages:
        if message['timestamp'] > after:
            result.append(message)
    return {
        'messages': result,
    }


app.run()
