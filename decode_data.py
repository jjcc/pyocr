import numpy as np
import cv2
from PIL import Image
import pytesseract
from ocrhelper import preprocess

#scale = 4

def ocr_top10(img, scale = 4,gif = False):

    top10 = []
    (x,y,w,h) = ( 20,90,298,115)
    if gif:
        (x,y,w,h) = (16, 78, 239, 99)

    crop_img = img[y: y + h, x: x + w]

    img = preprocess(crop_img, 10)
    lut_bw = np.asarray( img)

    stepw = scale*w/5;
    setph = scale*h/2;

    num = 0
    for j in range(0, 2):
        offset = j
        for i in range (0,5):
            blockimg3 = lut_bw[offset + setph * j:offset + setph * (j + 1)-6, i + stepw * i: i + stepw * (i + 1) - 8]

            #added 5 column to left of cropped image
            image_add = np.full((blockimg3.shape[0], blockimg3.shape[1] + 10), 255,np.uint8)
            image_add[:, 7:-3] = blockimg3
            cv2.imwrite("data/bocr%d.jpg" % num, image_add)
            img = Image.fromarray(image_add)
            text = pytesseract.image_to_string(img)
            #print  text
            num += 1
            top10.append(text)
    return top10

if __name__=="__main__":
    file = 'IKForecast_under_10_17_Feb_2016-one-year-long-until-17-Feb.gif'
    #file  = 'input/IKForecast_BIOTECH_13_Jan_2017-30-days-long-until-13-Feb-sticky.jpg'
    is_gif = False
    if file.endswith('f'):
        is_gif = True

    if(is_gif):
        imgA = Image.open(file)
        imgB = imgA.convert('RGB')
        img = np.asarray(imgB)
    else:
        img = cv2.imread(file)

    ocr_res = ocr_top10(img,gif = is_gif)
    for block in ocr_res:
        print block, "\n<<<<"
