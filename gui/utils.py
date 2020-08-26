import os
import uuid

FONT_SIZES = [7, 8, 9, 10, 11, 12, 13, 14,
              18, 24, 36, 48, 64, 72, 96, 144, 288]
IMAGE_EXTENSIONS = ['.jpg', '.png', '.bmp']
HTML_EXTENSIONS = ['.htm', '.html']


def hexuuid():
    return uuid.uuid4().hex


def splitext(p):
    return os.path.splitext(p)[1].lower()
