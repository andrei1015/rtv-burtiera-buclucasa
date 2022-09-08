# import cv2
from wand.image import Image
from wand.display import display
from pytesseract import pytesseract
import os
from pathlib import Path
import shutil

screens = 'screens/'
crops = 'screens/crops/'

screensExist = os.path.exists(screens)
cropsExist = os.path.exists(crops)

# REFRESH DIRS DELETE OR SOMETHING

if not screensExist:
  os.makedirs(screens)


os.system("ffmpeg -headers \"referer: https://www.romaniatv.net/\" -i \"https://livestream.romaniatv.net/clients/romaniatv/playlist.m3u8\" -vf fps=1/5 -t 00:01:00 screens/output%05d.jpg")

for filename in os.listdir(screens):

    with Image(filename = os.path.join(screens, filename)) as img:
        #print(img)
    
        # crop image using crop() function
        img.crop(0, 427, 720, 516)
    
        # save resized image
        img.save(filename = 'screens/cropped_' + filename)

if not cropsExist:
  os.makedirs(crops)

for src_file in Path(screens).glob('cropped_*.jpg'):
    shutil.copy(src_file, crops)

# path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# pytesseract.tesseract_cmd = path_to_tesseract

# # img = cv2.imread("test2.jpg")

# text = pytesseract.image_to_string("screens/output00000021.jpg", lang='ron')
# # im1.show()
# print(text)
