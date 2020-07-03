import cv2
import numpy as np
import socket
from vidgear.gears import VideoGear
from vidgear.gears import NetGear

import js2py

stream = VideoGear(source='test.mp4')
stream.start()
client = NetGear(address='202.31.203.45', port='35560')
count = 0
stream.read()
while True:
    try:
        frame = stream.read()
        if frame is None:
            break

        frame = cv2.resize(frame, dsize=(400,225))

        if count %3 == 0:
            client.send(frame)
        count += 1
    except KeyboardInterrupt:
        break

stream.stop()
for i in range(60):
    frame = cv2.imread('test.PNG', cv2.IMREAD_GRAYSCALE)
    frame -= 150
    frame = cv2.resize(frame, dsize=(400,225))
    client.send(frame)

client.close()
