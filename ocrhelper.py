import numpy as np
import cv2
from PIL import Image
import re

ListaV = [0] * 256
# initialize LUT
for i in range(0, 256):
    value = i * 255 / 150
    if (value > 255):
        ListaV[i] = 255
    else:
        ListaV[i] = value


def preprocess(image,idx,scale=4, invert = False, bw = True ):
    if invert:
        image = 255 - image
    image = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
    ListaVnp = np.array(ListaV)
    lut_L = cv2.LUT(image, ListaVnp)
    lut_L = lut_L.astype(np.uint8)
    file = "data_r/lut_gr%d.jpg"%idx
    #cv2.imwrite(file, lut_L)

    if bw == False:
        return Image.fromarray(lut_L) # return gray image
    _, lut_bw = cv2.threshold(lut_L, 160, 255, cv2.THRESH_BINARY)
    file = "data_r/lut_bw%d.jpg"%idx
    #cv2.imwrite(file, lut_bw)
    img = Image.fromarray(lut_bw)
    return img


def get_green_area(img):
    '''
    Initially retrieve the coordinates of the top right green area of "I Know first"
    :param img: the image
    :return: top left x, y and width , height
    '''
    shifted = cv2.pyrMeanShiftFiltering(img, 60, 100,1,2)

    #cv2.imwrite("shifted.jpg",shifted)
    # define range of blue color in HSV
    lower_green = np.array([0,210,0])
    upper_green = np.array([15,255,15])
    #get only green color area
    mask = cv2.inRange(shifted, lower_green, upper_green)
    #remove noise
    kernel = np.ones((5,5),np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    im2, contours, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    contours = sorted(contours, key = cv2.contourArea, reverse = True)[:1]
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 200:
            x, y, w, h = cv2.boundingRect(cnt)
    return (x,y,w,h)



def get_file_info( file):
    match = re.search("[\w|_|-]+\.\w+$",file)
    if match:
        fn = match.group(0)
        match = re.search("_(\d+)_*(\w+)_(20\d\d)",fn)
        if match:
            g = match.group()
            mr = fn[match.end():] #How long ,until when

            match =  re.search("(\d+|\w+)-(\w+)[-|\w]*-[U|u]ntil-(\w+)-(\d+).*\.(\w+)",mr)
            if(match):
                length = match.group(1)
                unit = match.group(2)
                tomon = match.group(3)
                todate = match.group(4)
                format = match.group(5)

            return (fn, g, mr, length,unit,tomon,todate,format)
        print fn
    return