import os
import glob
from PIL import Image

def thumbnail_fig(format):
    fig_files = glob.glob('./images/*.'+format)
    for fig_file in fig_files:
        img = Image.open(fig_file)
        img.thumbnail((160, 160))
        print(img.format, img.size, img.mode)
        img.save(fig_file.replace('images', 'tn'))

if __name__ == '__main__':
    thumbnail_fig('png')
    thumbnail_fig('jpg')