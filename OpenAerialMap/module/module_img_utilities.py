from __future__ import print_function
from builtins import object
from PIL import Image

class ThumbnailCreation(object):

    def __init__(self):
        pass

    @staticmethod
    def createThumbnail(imgFileAbsPath):

        THUMBNAIL_PIX_NUM = 640

        infile = imgFileAbsPath
        outfile = imgFileAbsPath + ".thumb.png"

        if infile != outfile:
            try:
                im = Image.open(infile)
                w, h = im.size
                longer = w if w > h else h
                resizeRatio = float(THUMBNAIL_PIX_NUM) / longer
                size = (int(w * resizeRatio), int(h * resizeRatio))
                # im = im.thumbnail(size)
                im = im.resize(size)
                im.save(outfile, "PNG")
            except Exception as e:
                # fix_print_with_import
                print((e, infile))

        return outfile
