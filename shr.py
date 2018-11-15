import pytesseract
import re
from PIL import Image

# from extractTable import tableExtract
from nesFun import isKeyWord, push, isEmpty, isPincode, printList, rearrageList, insertIntoDB
import pyreceipt
# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

def mainFun(path):
    im = Image.open(path)
    keyWords = []
    companyNames = []
    # reading the keywords
    with open('keyword.txt', 'r') as fp:
        keyWords = (fp.readlines())
    # readling company names
    #text = pytesseract.image_to_string(im, lang='eng')
    #lines = []
    #for s in text.split("\n"):
    #    if s:
    #        lines.append(s)


    lines = pyreceipt.call_tessaract(path)
#    print("The list has been updated")
    i = 0
#    print(lines)
#    print('======================================')
    while i < len(lines):

#        print("----------------------------------------", i)
#        print(lines[i])
        word = re.split(":|-|~|#", lines[i])

#        print("*******************WORD**********************")
#        print(word)
        

        if isKeyWord(keyWords, word[0]):

            if (isEmpty(word[1])):
                i += 1

                while (i < len(lines)):
                    
                    flag = False
                    word[1] += " " + lines[i]
                    str = lines[i].split(", ")
#                    print('*************STR*********')
#                    print(str)
                    for fu in str:

                        if (isPincode(fu)):
                            flag = True
                            break

                    if flag:
                        break

                    i += 1
            push(word)
        i += 1
#        print('+++++++++++++++')
#        print(word)
#        print('+++++++++++++++')
    lines = rearrageList()
#    print('========***REORDER_LIST***======')
#    print(lines)
#    print('========***REORDER_LIST***======')

    i = 0
    for s in lines:
        if i == 0:
          gst = s
        # print(s)
        i += 1
#    print("===GST===", gst)
    # insertIntoDB(lines)
    # tableExtract(path, gst)


image_path = '/Users/shravanc/ocr/invoiceReader/src/Invoice.jpg'
image_path = '/Users/shravanc/spacy_learning/dir_one/license_illibois.jpg'
image_path = '/Users/shravanc/spacy_learning/dir_one/git/pyreceipt/screen_shot_2016-10-11_at_4.51.04_pm.jpg'
image_path = '/Users/shravanc/spacy_learning/dir_one/git/pyreceipt/27fe1111c5dd88dd76dd241cf1a5c997.jpg'
mainFun(image_path)
