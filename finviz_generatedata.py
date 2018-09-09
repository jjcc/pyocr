from PIL import Image, ImageDraw, ImageFont

fnt = ImageFont.truetype('font/arialbd.ttf', 12)

outdir = "images/gen/"

for i in xrange(20,255):
    clr =  (20,i,20)
    img = Image.new('RGB', (19, 18), color=clr)
    d = ImageDraw.Draw(img)
    d.text((6, 3), "6", font=fnt, fill=(255, 255, 255))
    fn = outdir + "6_%d.png"%i
    img.save(fn)