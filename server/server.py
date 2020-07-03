import socket
import cv2
import numpy as np
from vidgear.gears import NetGear


server = NetGear(address='192.168.0.6', port='35560', receive_mode = True)

while True:
    frame = server.recv()

    if frame is None:
        break

    adress = "Gumi-si Daehak-ro 61"
    font = cv2.FONT_HERSHEY_DUPLEX
    xCenterOfFrame = 10
    yBottomOfFrame = 200
    bottomLeftCornerOfText = (xCenterOfFrame, yBottomOfFrame)
    fontScale = 1
    fontColor = (0, 255, 0)
    lineType = 2

    cv2.putText(frame, adress, bottomLeftCornerOfText, font, fontScale, fontColor, lineType)
    
    winname = "Output Frame"
    cv2.namedWindow(winname, flags=cv2.WINDOW_GUI_NORMAL)
    cv2.moveWindow(winname, 100, 400) # move window to x, y
    cv2.setWindowProperty(winname, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_AUTOSIZE)
    cv2.resizeWindow(winname, 400, 225)

    
    cv2.imshow(winname, frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break


cv2.destroyAllWindows()


server.close()
