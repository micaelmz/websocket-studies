from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
from random import randint
import time
import threading
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')


def send_random_numbers():
    while True:
        message = input('Digite uma mensagem: ')
        socketio.emit('python_socket', {'message': str(message)})



if __name__ == '__main__':
    t = threading.Thread(target=send_random_numbers)
    t.start()
    socketio.run(app, debug=False, port=44356)
    print()
