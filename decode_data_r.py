import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
import pytesseract

from ocrhelper import preprocess








if __name__=="__main__":

    file = 'IKForecast_under_10_17_Feb_2016-one-year-long-until-17-Feb.gif'
    #file  = 'input/IKForecast_BIOTECH_13_Jan_2017-30-days-long-until-13-Feb-sticky.jpg'
    is_gif = False
    if file.endswith('f'):
        is_gif = True

    if(is_gif):
        imgA = Image.open(file)
        imgB = imgA.convert('RGB')
        imgOrig = np.asarray(imgB)
        rect1 = [292,70,290,29]
        (xl, yl, wl, hl) = (16, 5, 45, 20)
        (xm, ym, wm, hm) = (180, 8, 54, 13)
        (xr, yr, wr, hr) = (251, 5, 26, 20)
    else:
        imgOrig = cv2.imread(file)
        rect1 = [364, 80, 364, 34]  # hight should be 33.5
        (xl,yl,wl,hl) = (25,5,60,23)
        (xm, ym, wm, hm) = (225, 5, 75, 20)
        (xr, yr, wr, hr) = (310, 5, 30, 23)

    # rect1 = [364, 60, 364, 20]
    # crop_img = imgOrig[rect1[1]: rect1[1] + rect1[3], rect1[0]: rect1[0] + rect1[2]]
    # img = preprocess(crop_img,100,True)
    # text = pytesseract.image_to_string(img)
    # print text

    # (xl,yl,wl,hl) = (25,5,60,23)
    # (xm, ym, wm, hm) = (225, 5, 75, 20)
    # (xr, yr, wr, hr) = (310, 5, 30, 23)



    #[292,70,290,29
    crop_img2 = imgOrig[ rect1[1]: rect1[1]+rect1[3], rect1[0]: rect1[0]+rect1[2]]
    cv2.imwrite("data_r/crop_img2.jpg", crop_img2)



    imgv = cv2.imread('data_r/lut_gr21.jpg',cv2.IMREAD_GRAYSCALE)

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
        adjust = 0.3
        if is_gif:
            adjust = 0.25
        yy += height - adjust
        y = int(yy)
        ########
        imgl = crop_img2.copy()[yl: yl + hl, xl: xl + wl]
        img = preprocess(imgl, i,bw=False)
        textl = pytesseract.image_to_string(img)
        img2 = crop_img2.copy()[ym: ym + hm, xm: xm + wm]
        img = preprocess(img2, i+10)
        textm = pytesseract.image_to_string(img)
        img3 = crop_img2[yr: yr + hr, xr: xr + wr]
        img = preprocess(img3, i+20,bw=False)

        #textr = pytesseract.image_to_string(img)
        imgA = np.asarray(img)
        #gray to gray is best, bw to gray 2nd, bw to bw worst
        resx = cv2.matchTemplate(imgA, imgv, cv2.TM_CCOEFF_NORMED)
        scorex =  resx[0][0]
        print "Text: %s, %s, %s" % (textl, textm, scorex)


        num +=1
