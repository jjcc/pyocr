from PIL import Image, ImageDraw, ImageFont

fnt = ImageFont.truetype('font/arialbd.ttf', 12)

outdir = "images/gen/"

def generate_digit( dgt):
    '''
    :param dgt: a character need to generate
    :return:
    '''
    for i in xrange(20, 255):
        clr = (20, i, 20)
        img = Image.new('RGB', (19, 18), color=clr)
        d = ImageDraw.Draw(img)
        d.text((6, 3), dgt, font=fnt, fill=(255, 255, 255))
        fn = outdir + "%s_%d.png" %(dgt, i)
        img.save(fn)

for c in xrange(ord('0'), ord('9')+1):
    digit = chr(c)
    generate_digit(digit)