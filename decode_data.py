import numpy as np
import cv2
from PIL import Image
import pytesseract
from ocrhelper import preprocess

#scale = 4

def ocr_top10(img, scale = 4):

    top10 = []
    (x,y,w,h) = ( 20,90,298,115)
    crop_img = img[y: y + h, x: x + w]

    img = preprocess(crop_img, 10)
    lut_bw = np.asarray( img)

    stepw = scale*w/5;
    setph = scale*h/2;

    num = 0
    for j in range(0, 2):
        offset = j
        for i in range (0,5):
            blockimg3 = lut_bw[offset + setph * j:offset + setph * (j + 1), i + stepw * i: i + stepw * (i + 1) - 4]
            #cv2.imwrite("data/bocr%d.jpg" % num, blockimg3)
            img = Image.fromarray(blockimg3)
            text = pytesseract.image_to_string(img)
            print  text
            num += 1
            top10.append(text)
    return top10

if __name__=="__main__":

    img = cv2.imread('input/IKForecast_BIOTECH_13_Jan_2017-30-days-long-until-13-Feb-sticky.jpg')

    ocr_res = ocr_top10(img)
    for block in ocr_res:
        print block
