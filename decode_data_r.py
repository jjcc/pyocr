import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
import pytesseract

from ocrhelper import preprocess








if __name__=="__main__":
    imgOrig = cv2.imread('input/IKForecast_BIOTECH_13_Jan_2017-30-days-long-until-13-Feb-sticky.jpg')
    # rect1 = [364, 60, 364, 20]
    # crop_img = imgOrig[rect1[1]: rect1[1] + rect1[3], rect1[0]: rect1[0] + rect1[2]]
    # img = preprocess(crop_img,100,True)
    # text = pytesseract.image_to_string(img)
    # print text

    (xl,yl,wl,hl) = (25,5,60,23)
    (xm, ym, wm, hm) = (225, 5, 75, 20)
    (xr, yr, wr, hr) = (310, 5, 30, 23)


    rect1 = [364,80,364,34] #hight should be 33.5
    crop_img2 = imgOrig[ rect1[1]: rect1[1]+rect1[3], rect1[0]: rect1[0]+rect1[2]]
    cv2.imwrite("data_r/crop_img2.jpg", crop_img2)


    # #img2 = preprocess(crop_img2,99)
    # #text = pytesseract.image_to_string(img2)
    # imgl = crop_img2.copy()[yl: yl+hl, xl: xl + wl]
    # img = preprocess(imgl, 60)
    # textl = pytesseract.image_to_string(img)
    # img2 = crop_img2.copy()[ym: ym+hm, xm: xm + wm]
    # img = preprocess(img2, 61)
    # textm = pytesseract.image_to_string(img)
    # img3 = crop_img2[yr: yr+hr, xr: xr + wr]
    # img = preprocess(img3, 62)
    # textr = pytesseract.image_to_string(img)
    #
    #
    # print "Text: %s, %s, %s"%(textl,textm,textr)

    x = rect1[0]
    y = rect1[1]
    w = rect1[2]
    height = rect1[3]
    yy = y
    num = 0
    for i in range(0, 10):
        crop_img2 = imgOrig[y:y + height, x:x + w]
        #img = preprocess(crop_img3,i)
        #text = pytesseract.image_to_string(img)
        #print "No.%d"%num
        #print text
        yy += height - 0.3
        y = int(yy)
        ########
        imgl = crop_img2.copy()[yl: yl + hl, xl: xl + wl]
        img = preprocess(imgl, i)
        textl = pytesseract.image_to_string(img)
        img2 = crop_img2.copy()[ym: ym + hm, xm: xm + wm]
        img = preprocess(img2, i+10)
        textm = pytesseract.image_to_string(img)
        img3 = crop_img2[yr: yr + hr, xr: xr + wr]
        img = preprocess(img3, i+20)
        textr = pytesseract.image_to_string(img)
        print "Text: %s, %s, %s" % (textl, textm, textr)


        num +=1
