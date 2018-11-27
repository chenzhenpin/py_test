#!/usr/bin/env python
from flask import Flask, render_template, Response
from threading import Thread
# emulated camera
from camera import VideoCamera

# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

myapp = Flask(__name__)


@myapp.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@myapp.route('/video_feed')
def video_feed():

    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
# def cv_img(app,cam):
#    with app.app_context():
#        cam.img()
# def Thread_img(camer):
#     thr = Thread(target=video_feed, args=[myapp,camer])
#     thr.start()




if __name__ == '__main__':
    myapp.run(host='0.0.0.0', debug=True, threaded=True)
