import cv2
import numpy as np
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
# if screensExist:
#   shutil.rmtree(screens, ignore_errors=False, onerror=None)
# if os.path.exists('burtiere.txt'):
#   os.remove('burtiere.txt')


path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.tesseract_cmd = path_to_tesseract


# os.makedirs(screens)


# os.system("ffmpeg -loglevel quiet -headers \"referer: https://www.romaniatv.net/\" -i \"https://livestream.romaniatv.net/clients/romaniatv/playlist.m3u8\" -vf fps=1/5 -t 00:01:00 screens/output%06d.jpg")

# for filename in os.listdir(screens):

#     with Image(filename = os.path.join(screens, filename)) as img:
#         #print(img)
    
#         # crop image using crop() function
#         img.crop(0, 427, 720, 516)
    
#         # save resized image
#         img.save(filename = 'screens/cropped_' + filename)

# os.makedirs(crops)

# for src_file in Path(screens).glob('cropped_*.*'):
#     shutil.copy(src_file, crops)
#     os.remove(src_file)

for imageName in os.listdir (crops):
  inputPath = os.path.join(crops, imageName)
  img = cv2.imread(inputPath)

  img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
  # img = cv2.GaussianBlur(img, (5, 5), 0)
  img = cv2.bilateralFilter(img,9,75,75)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  kernel = np.ones((1, 1), np.uint8)
  img = cv2.dilate(img, kernel, iterations=1)
  img = cv2.erode(img, kernel, iterations=1)

  cv2.threshold(img,127,255,cv2.THRESH_BINARY)

  #cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

  #cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
  
  text = pytesseract.image_to_string(img, lang='ron')

  print(text)
  
  with open('burtiere1.txt', 'a', encoding='utf-8') as f:
   # f.write(text + ' : ' + imageName + '\n\n')
    f.write('\n\n===================\n\n')
    f.write(imageName)
    f.write('\n\n===================\n\n')
    f.write(text)
    f.write('\n\n-------------------\n\n')

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
