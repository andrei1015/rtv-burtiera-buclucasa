import easyocr
reader = easyocr.Reader(['ro']) # this needs to run only once to load the model into memory
result = reader.readtext('test2.jpg')
print(result)
