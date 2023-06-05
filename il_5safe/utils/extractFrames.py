import sys
import argparse
import os.path

import cv2
# print(cv2.__version__)

def extractImages(pathIn, pathOut, quality):

    count = 0
    video = cv2.VideoCapture(pathIn)
    success,image = video.read()
    fps = video.get(cv2.CAP_PROP_FPS)
    print('frames per second =', fps)
    while success:
        video.set(cv2.CAP_PROP_POS_FRAMES, count)
        success, image = video.read()

        print (f'Read new frame, number {count}: {success}')
        fileName = os.path.join(pathOut , "frame%d.jpg" % count)
        cv2.imwrite( fileName, image, [int(cv2.IMWRITE_JPEG_QUALITY), int(quality)])     # save frame as JPEG file
        count += 1

if __name__=="__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video")
    a.add_argument("--pathOut", help="path to images")
    a.add_argument("-q", "--quality", required=True, help="Quality level (from 0 to 100)")
    args = a.parse_args()
    print(args)
    extractImages(args.pathIn, args.pathOut, args.quality)
