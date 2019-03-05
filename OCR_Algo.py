import pytesseract  ####reading string from image (OCR library)
import  numpy as np ##numpy for shape
import cv2   #Computer vision library
import os    ##for remove image file which we edit during procedure
pytesseract.pytesseract.tesseract_cmd='C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
###you need to install ocr and give path in program
try:
    image='licence.jpg'
    print('Editing image for better OCR result..........')
    img = cv2.imread(image)  ###reading image
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    new_image = 'edited' + '_' + image  ###new image which we save during procedure
    cv2.imwrite(new_image, img)  ###Save a new edited image
    read = pytesseract.image_to_string(new_image)  ####reading from new generated image
    print(read)  ##print resuult

except Exception as e:
    print('please provide proper name of the image')
    print(e)
