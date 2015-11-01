#! /usr/bin/python
"""
ppp.py
peggy.pi.pic
Take picture with Raspberry Pi camera and then display
    as 25 x 25 pixel image (16 shades) on Peggy2
"""

# http://picamera.readthedocs.org/en/release-1.9/recipes1.html#capturing-to-a-pil-image
import io
import time
import picamera
from PIL import Image

# Create the in-memory stream
stream = io.BytesIO()
with picamera.PiCamera() as camera:
    camera.hflip = True
    camera.vflip = True
    camera.start_preview()
    time.sleep(2)
    camera.capture(stream, format='bmp')
# "Rewind" the stream to the beginning so we can read its content
stream.seek(0)
image = Image.open(stream)

#crop square
image = image.crop((280,0,1000,720))
#convert to grey
image = image.convert('L')

# # test - show image
# image.show()

image.thumbnail((25,25))

# # save image to file as test
# imgout = open('/home/pi/temp.bmp', 'w')
# image.save(imgout)
# imgout.close()
#
pxls = list(image.getdata())

# look at pixel values in 25 x 25 array
for i in len(pxls):
    print pxls[i],
    if i % 25 == 24:
        print '\n'
