import urllib2
from bs4 import BeautifulSoup
import time
import random


# file = "https://iknowfirst.com/wp-content/uploads/2016/12/IKForecast_Top_10_small_cap_05_Dec_2016-7-days-long-until-Dec-12.jpg"
# match = re.search("[\w|_|-]+\.\w+$",file)
# if match:
#     fn = match.group(0)
#     match = re.search("_(\d\d)_(\p{L}+)_(20\d\d)",fn)
#     if match:
#         g = match.group()
#         mr = fn[match.end():]
#
#     print fn


opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')]

# for i in range(95,105):
#     url = "https://iknowfirst.com/page/%d"%i
#     html = opener.open(url)
#     sl = random.randint(1,5);
#
#     bsObj = BeautifulSoup(html,"html.parser")
#     images = bsObj.select(".wp-image-37141")
#     print ">>>:", i
#     time.sleep(5)
#     for img in images:
#
#         print(img.attrs['src'])


imgData = opener.open('https://iknowfirst.com/wp-content/uploads/2016/12/IKForecast_Top_10_small_cap_05_Dec_2016-7-days-long-until-Dec-12.jpg').read()
output = open("downloaded.jpg",'wb')
output.write(imgData)
output.close()