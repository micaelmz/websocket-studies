from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import threading
import cv2
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')

def send_images_via_websocket():
    cap = cv2.VideoCapture(0)
    fps = 24
    while True:
        ret, frame = cap.read()

        if ret:
            #cv2.imshow('Webcam', frame)  # Exibe o frame capturado
            _, buffer = cv2.imencode('.jpg', frame)
            jpg_as_text = base64.b64encode(buffer)

            socketio.emit('python_socket', {'message': jpg_as_text.decode('utf-8')})

            key = cv2.waitKey(int(1000 / fps)) & 0xFF

            if key == ord('q'):
                break
        else:
            break

if __name__ == '__main__':
    t = threading.Thread(target=send_images_via_websocket)
    t.start()
    socketio.run(app, debug=False, port=9542)
