import cv2
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
if screensExist:
  shutil.rmtree(screens, ignore_errors=False, onerror=None)
  os.remove('burtiere.txt')


path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.tesseract_cmd = path_to_tesseract


os.makedirs(screens)


os.system("ffmpeg -loglevel quiet -headers \"referer: https://www.romaniatv.net/\" -i \"https://livestream.romaniatv.net/clients/romaniatv/playlist.m3u8\" -vf fps=1/5 -t 00:05:00 screens/output%06d.jpg")

for filename in os.listdir(screens):

    with Image(filename = os.path.join(screens, filename)) as img:
        #print(img)
    
        # crop image using crop() function
        img.crop(0, 427, 720, 516)
    
        # save resized image
        img.save(filename = 'screens/cropped_' + filename)

os.makedirs(crops)

for src_file in Path(screens).glob('cropped_*.*'):
    shutil.copy(src_file, crops)
    os.remove(src_file)

for imageName in os.listdir (crops):
  inputPath = os.path.join(crops, imageName)
  img = cv2.imread(inputPath)
  text = pytesseract.image_to_string(img, lang='ron')

  print(text)
  
  with open('burtiere.txt', 'a', encoding='utf-8') as f:
    f.write(text + ' : ' + imageName + '\n\n')

# for image in os.listdir(crops):
#         print(os.path.join(crops, image))
#         inputPath = os.path.join(crops, image)
#         cropped_file = open(inputPath)
#         text = pytesseract.image_to_string(cropped_file, lang='ron')

#         with open('burtiere.txt', 'w') as f:
#           f.write(text + ' : ' + cropped_file)

# for cropped_file in Path(crops).glob('*.*'):
#   #img = cv2.imread("test2.jpg")
#   print(cropped_file)
#   text = pytesseract.image_to_string(cropped_file, lang='ron')

#   with open('burtiere.txt', 'w') as f:
#     f.write(text + ' : ' + cropped_file)
