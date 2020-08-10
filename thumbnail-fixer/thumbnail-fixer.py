#!/usr/bin/env python3

from PIL import Image
import os

src_dir = os.path.getcwd() + "/images"
dest_dir = os.path.getcwd() + "/images-fixed"

def get_filelist(path):
    filelist = []
    for root, directories, files in os.walk(path):
        for f in files:
            if f[0] == ".":
                pass
            else:
                filelist.append((os.path.join(root,f),f))
    return filelist

def fix(image):
    with Image.open(image) as img:
        #rotate
        img = img.rotate(-90)
        #resize
        img = img.resize((128,128))
        #convert
        img = img.convert("RGB")
        #return fixed image
        return img

if __name__ == "__main__":
    imagelist = get_filelist(src_dir)
    #image[0] = path+name; image[1] = name only
    for image in imagelist:
        #save new to dest_dir
        fix(image[0]).save(dest_dir+image[1], "JPEG")
