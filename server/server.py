import socket
import cv2
import numpy as np
from vidgear.gears import NetGear



server = NetGear(address='127.0.0.1', port='35560', receive_mode = True)


while True:
    frame = server.recv()

    if frame is None:
        break

    cv2.namedWindow('Output Frame',cv2.WINDOW_GUI_NORMAL)
    cv2.setWindowProperty('Output Frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.moveWindow('Output Frame', 100,400)
    cv2.resizeWindow('Output Frame', 400, 255)
    cv2.imshow("Output Frame", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()


server.close()

