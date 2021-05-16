import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import json
import os
from tqdm import tqdm
import cv2
import numpy as np

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


my_dict = {}

# Loading frames from directory
frames = os.listdir('./image_frames')

# Sorting frames according to their numbers
frames.sort(key=lambda x: int(x[5:-4]))

# printing total number of frames loaded
print("Number of frames :- " + str(len(frames)))

for frame in tqdm(frames):

    image=cv2.imread('./image_frames/'+frame)
    gray = get_grayscale(image)
    thresh = thresholding(gray)

    # Perform text extraction
    data = pytesseract.image_to_string(thresh, lang='eng')

    # replacing \n
    text_in_image = data.replace('\n', '')

    # Removing unwanted spaces
    text_in_image = text_in_image.strip()

    # removing unicode characters
    text_in_image = text_in_image.encode('ascii', 'ignore').decode()

    # appending output to dictionary (only those frames which contain text)
    if(len(text_in_image) != 0):
        my_dict[str(frame)] = text_in_image


# Saving output of dictionary to json file
with open('text.json', 'w') as outputFile:
    json.dump(my_dict, outputFile)
