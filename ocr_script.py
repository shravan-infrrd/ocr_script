import pytesseract
import re
from PIL import Image
import spacy_lib
import time
#
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
#

from nesFun import isKeyWord, push, isEmpty, isPincode, printList, rearrageList, insertIntoDB
import pyreceipt


def check_keyword_limit(line, keyWords):
    counter = 0
    for word in keyWords:
        word = word.rstrip()
        if counter > 1:
            return True
        if word in line:
            counter += 1

    return False

def process_data(lines, keyWords):
    for line in lines:
        if check_keyword_limit(line, keyWords) == True:
            lines.remove(line)
            obj = spacy_lib.split_entity(line)
            lines += obj
            return lines
    
    return lines

def analyze(lines, keywords):
    i = 0
    slist = []
    while i < len(lines):
        print('-----LINE---->', lines[i])
        word = re.split(":|-|~|#", lines[i])
        print('====WORD====', word)
        if isKeyWord(keywords, word[0]):
            print('------IDENTIFIED KEYWORD--------')
            if (isEmpty(word[1])):
                i += 1
                while (i < len(lines)):
                    flag = False
                    word[1] += " " + lines[i]
                    str = lines[i].split(", ")
                    for fu in str:
                        if (isPincode(fu)):
                            flag = True
                            break

                    if flag:
                        break

                    i += 1
            push(slist, word)
        i += 1
    
    return slist

def mainFun(path):
    slist = []
    keyWords = []
    with open('keyword.txt', 'r') as fp:
        keyWords = (fp.readlines())

    filename = str(int(time.time())) + '.jpg'
    save_path = '/Users/shravanc/spacy_learning/dir_one/git/ocr_script/processed_images/'
    file_path = save_path + filename


    img = cv.imread('/Users/shravanc/Desktop/image_files/image_11.jpg',0)
    img = cv.medianBlur(img,5)
    ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
    cv.imwrite(file_path,th1)


    # lines = pyreceipt.call_tessaract(path)
    lines = pyreceipt.call_tessaract(file_path)


    print('*******************LINES*******************')
    print(lines)

    new_lines = process_data(lines, keyWords)
    print('*******************NEW LINES*******************')
    print(new_lines)

    if not new_lines:
        lines = new_lines

    slist = analyze(lines, keyWords)
 
    return {'data': slist}

