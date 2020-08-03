###########
# pytorch
############
import tensorflow as tf
from tensorflow import keras

#############
# other packages
#############
import numpy as np
import matplotlib.pyplot as plt
import sys

##############
# show the device list
###############
from tensorflow.python.client import device_lib
device_lib.list_local_devices()

##############
# show tensorflow version
###############
print('tensorflow version')
print(tf.__version__)

##############
# openCV 
##############
import cv2

cap = cv2.VideoCapture(0) # Web cam のインスタンス生成
if cap.isOpened() == False: 
    print("Error: No camera connected. exit()")
    sys.exit()

SRC_IMAGE_SIZE_W = 640  # VGA
SRC_IMAGE_SIZE_H = 480  # VGA
SRC_IMAGE_FRAME_RATE = 30

# 入力画像のサイズとフレームレートを設定
cap.set(cv2.CAP_PROP_FPS, SRC_IMAGE_FRAME_RATE) 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, SRC_IMAGE_SIZE_W) 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, SRC_IMAGE_SIZE_H)

ret, frame = cap.read()
cv2.namedWindow("CAMERA_INPUT_IMAGE", cv2.WINDOW_NORMAL)

# カメラからの入力画像の(width, height), channelを表示する
#cap_h, cap_w, cap_ch = frame.shape
frame_rate  = int(cap.get(5))
print('cameraH, cameraW, CH')
print(frame.shape)
print('frame_rate')
print(frame_rate)
frame_count = int(cap.get(7))
print('frame_count')
print(frame_count)

while(True):
    ret, frame = cap.read() # return 0 -255 value
    if ret == False: 
        break     
    cv2.imshow("CAMERA_INPUT_IMAGE", frame) # camera入力画像
    # Key入力処理
    key = cv2.waitKey(1) & 0xff
    if key == 27:
        break

cap.release()         
cv2.destroyAllWindows()

