import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
import pytesseract

img0 = cv2.imread('data_r/lut_bw15.jpg')
img = Image.fromarray(img0)
text = pytesseract.image_to_string(img)

print "result: " + text



imgx = cv2.imread('data_r/lut_bw22.jpg')
imgv = cv2.imread('data_r/lut_bw21.jpg')

t1 = cv2.imread('data_r/lut_bw21.jpg')
t2 = cv2.imread('data_r/lut_bw22.jpg')
t3 = cv2.imread('data_r/lut_bw23.jpg')
t4 = cv2.imread('data_r/lut_bw24.jpg')
t5 = cv2.imread('data_r/lut_bw25.jpg')
t6 = cv2.imread('data_r/lut_bw26.jpg')
t7 = cv2.imread('data_r/lut_bw27.jpg')
t8 = cv2.imread('data_r/lut_bw28.jpg')
t9 = cv2.imread('data_r/lut_bw29.jpg')

tgt = [t1,t2,t3,t4,t5,t6,t7,t8,t9]

num = 1
for t in tgt:
    print "target:%d"%num
    res1 = cv2.matchTemplate(t,imgx,cv2.TM_CCOEFF_NORMED)
    res2 = cv2.matchTemplate(t,imgv,cv2.TM_CCOEFF_NORMED)
    print "matching x:" , res1[0][0]
    print "matching v:" , res2[0][0]
    num +=1
threshold = 0.8