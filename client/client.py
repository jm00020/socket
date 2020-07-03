import cv2
import numpy as np
import socket
from vidgear.gears import VideoGear
from vidgear.gears import NetGear



stream = VideoGear(source='test.mp4').start()
client = NetGear(address='202.31.203.45', port='35560')

while True:
    try:
        frame = stream.read()

        if frame is None:
            break
        
        client.send(frame)

    except KeyboardInterrupt:
        break

stream.stop()
client.close()


