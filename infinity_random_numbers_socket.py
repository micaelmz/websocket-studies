from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
from random import randint
import time
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')


def send_random_numbers():
    while True:
        data = randint(0, 9)
        socketio.emit('python_socket', {'message': str(data)})
        time.sleep(0.008)  # Envia um número aleatório a cada segundo


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('connect')
def test_connect():
    print('Client connected')


if __name__ == '__main__':
    t = threading.Thread(target=send_random_numbers)
    t.start()
    socketio.run(app, debug=True, port=44356)
