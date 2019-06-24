import urllib.request
import cv2
import time
import numpy as np
import os

url = ["http://192.168.0.103:8080/photoaf.jpg"]   # If we use multiple IP camera mobile
while True:
    for i in url:
        imgPath = urllib.request.urlopen(i)
        imgNp = np.array(bytearray(imgPath.read()), dtype=np.uint8)
        img = cv2.imdecode(imgNp, -1)
    cv2.imwrite('Maze3D.jpg', img)
    cv2.imshow("Maze", img)
    saved_path = 'D:/IP Test Camera'
    cv2.imwrite(os.path.join(saved_path, 'Maze3D.jpg'), img)
    if ord('q') == cv2.waitKey(1):                  # To quit application by pressing q
        exit(0)
    time.sleep(5)
