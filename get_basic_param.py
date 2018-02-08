import numpy as np
import cv2
from PIL import Image
import pytesseract
from ocrhelper import get_green_area

#file = 'IKForecast_top_10_Tech_14_Feb_2017-3-days-long-until-17-Feb.gif'
file = 'IKForecast_under_10_17_Feb_2016-one-year-long-until-17-Feb.gif'

if file.endswith('f'):
    imgA = Image.open(file)
    imgB = imgA.convert('RGB')


    img = np.asarray(imgB)
    cv2.imwrite("test.jpg",img)
else:
    img = cv2.imread(file)


param = get_green_area(img)

print param