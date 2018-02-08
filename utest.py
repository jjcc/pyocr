import re
import urllib2
from ocrhelper import get_file_info
import time
import random
from bs4 import BeautifulSoup

#opener = urllib2.build_opener()
#opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')]

# for i in range(95,105):
#     url = "https://iknowfirst.com/page/%d"%i
#     html = opener.open(url)
#     sl = random.randint(1,5);
#
#     bsObj = BeautifulSoup(html,"html.parser")
#     images = bsObj.select(".wp-image-37141")
#     print ">>>:", i
#     time.sleep(sl)
#     for img in images:
#         f = img.attrs['src']
#         print f


file = "https://iknowfirst.com/wp-content/uploads/2016/12/IKForecast_Top_10_small_cap_05_Dec_2016-7-days-long-until-Dec-12.jpg"

count = 0
with open("input/imagelist2.txt") as fo:
    for line in fo:
        #print line
        (fn, all,category,mfront, mrear,length,unit,tomon,todate, format) = get_file_info(line)
        #print count
        print "%d,result: %s,C:%s , Len: %s, Unit: %s, to month: %s, to date: %s, format:%s"%(count,all,category, length,unit,tomon,todate,format)
        count +=1