from mss import mss
import cv2
import numpy as np
from pymouse import PyMouse
import time

m = PyMouse()
mon = {'top': 190, 'left': 217, 'width': 480, 'height': 530}
sct = mss()
dtr = cv2.SimpleBlobDetector_create()
while True:
    img = np.array(sct.grab(mon))
    img = cv2.imshow('sct', img)
    if cv2.waitKey(33) == ord('a'):
        break
t_start = time.time()
print('start!')


while time.time() - t_start < 40:
    img = np.array(sct.grab(mon))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kpts = dtr.detect(img)
    try:
        pt = (kpts[0].pt[0] + mon['left'], kpts[0].pt[1] + mon['top'])
        m.move(*list(map(lambda x: int(x), pt)))
    except IndexError:
        pass
