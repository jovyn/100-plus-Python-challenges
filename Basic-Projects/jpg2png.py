'''
Write a python script that converts the JPG images from one folder and converts them to PNG.
Store all the PNGs in another given folder. Both folder names should be passed at runtime.
Eg:
#JpgtoPngConverter.py  Folder_JPG/ Folder_PNG/

'''

import sys
import os
import argparse
from pathlib import Path
from PIL import Image

parser = argparse.ArgumentParser(prog='python jpg2png.py', usage='%(prog)s -in [JPG_Dir] -out [PNG_Dir]' ,description='Script to convert JPG to PNG')
parser.add_argument('input', metavar='in', type=str, help='Input directory location')
parser.add_argument('output', metavar='out', type=str, help='Output directory location')
#help_msg = parser.print_help()

def ConvertJPG2PNG(jpg_dir, png_dir):
    #print(jpg_dir + "--" + png_dir )
    x = Path(jpg_dir)
    jpgs = list(x.glob('*.jpg'))  # Select all jpgs from the folder
    #print(jpgs)
    for jpg in jpgs:
        try:
            img = Image.open(Path(jpg))    #Open all jpgs

        except IOError:
            print("Cannot Load image")
            sys.exit(1)
        jpg_cleanname = os.path.splitext(os.path.basename(jpg))[0]
        outpath = str(png_dir) + str(jpg_cleanname) + ".png"  #Save with same name + .png extension
        img.save(outpath,'png')  #Save as PNG
        print(f"Converted and Saved {outpath}")


if len(sys.argv) == 5:
    dir_in = sys.argv[2]
    dir_out = sys.argv[4]
    ConvertJPG2PNG(dir_in, dir_out)


else:
    print("Improper Syntax !!!!!!!")
    parser.print_usage()
    sys.exit(1)



