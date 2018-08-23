import numpy as np
import cv2
from PIL import Image
import pytesseract
#from ocrhelper import preprocess


#failed attempt

def get_cropped(image, area):
    (x, y, w, h) = area
    new_img = image[y: y + h, x: x + w]
    return new_img


def split(image,row,column, area):
    width = area[2]
    height = area[3]
    unitw = width/column # 19 px
    unith = height/row

    all_imgs = []
    for j in range(0, 2):
        #offset = j
        for i in range (0,21):
            blockimg = image[unith * j:unith * (j + 1), unitw * i: unitw * (i + 1)]
            #cv2.imwrite("images/unit%d_%d.png" %(i,j), blockimg)
            all_imgs.append( blockimg)
    return all_imgs

#####################
rows = 9
columns = 21
lefttopwh = (200, 65, 399, 162)

file = "images/grp_image.ashx.png"
filecrop = "images/cropped.png"
img = cv2.imread(file)
crop_img = get_cropped(img,lefttopwh)
#cv2.imwrite(filecrop, crop_img)

image_array = split(crop_img,rows,columns,lefttopwh)

(i,j) = (20,0)
pick_one = image_array[j*columns + i]
file_picked = "images/picked.png"
#cv2.imwrite(file_picked,pick_one)
img = Image.fromarray(pick_one).resize((38,36))
text = pytesseract.image_to_string(img,boxes=True,config='-psm 10 -oem 3 -c tessedit_char_whitelist=0123456789')
print "result" + text
print "end"