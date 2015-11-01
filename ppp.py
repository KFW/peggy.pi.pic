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

# # print function for test purposes
# def printpxl(pxllist):
#     # # look at pixel values in 25 x 25 array
#     i = 0
#     for p in pxllist:
#         print p,
#         if i % 25 == 24:
#             print '\n'
#         i += 1

def main():
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
    image.thumbnail((25,25))
    pxls = list(image.getdata())

    ## print for test purposes
    # printpxl(pxls)

    # convert pixels to 16 levels from 256
    # scale the range in order to maximize contrast
    maxpxl = max(pxls)
    minpxl = min(pxls)
    deltapxl = maxpxl - minpxl

    for i, p in enumerate(pxls):
        scaledpxl = (pxls[i] - minpxl) * 255 / deltapxl
        pxls[i] = scaledpxl//16

    # #print for testing purposes
    # printpxl(pxls)
    #
    # image.putdata(pxls, scale = 16) #scale by 16 for regular display
    # # save image to file as test
    # imgout = open('/home/pi/temp.bmp', 'w')
    # image.save(imgout)
    # imgout.close()

if __name__ == '__main__':
    main()
