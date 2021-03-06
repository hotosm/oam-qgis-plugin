from PIL import Image

class ThumbnailCreation:

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
                print(e, infile)

        return outfile
