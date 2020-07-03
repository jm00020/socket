import socket
import cv2
import numpy as np
from vidgear.gears import NetGear


#define netgear client with `receive_mode = True` and default settings
server = NetGear(address='127.0.0.1', port='35560', receive_mode = True)

# infinite loop
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

# close output window
cv2.destroyAllWindows()


# safely close client
server.close()


# HOST = '127.0.0.1'
# PORT = 5180

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


# server_socket.bind((HOST, PORT))

# server_socket.listen()

# client_socket, addr = server_socket.accept()

# print('Connected by', addr)

# while True:

#     data = client_socket.recv(4096)

#     frame= np.array(data)
#     print(frame)
#     cv2.imshow('test', frame)

#     # client_socket.sendall(data)

# client_socket.close()
# server_socket.close()
