#from random import *
#import pyautogui as gui
#n=["hi",'hello']
#v=['noor','rami']
#s=["hdhd","dhd"]
#while True:
 #gui.write(n[randint(0, len(n)-1)])
 #break
from PIL import Image
from pytesseract import pytesseract
import pyautogui as gui
from time import * 
import datetime
 #Define path to tessaract.exe
#path_to_tesseract = r'C: \\Program Files \\Tesseract-OCR \\tesseract.exe'
 #Point tessaract_cmd to tessaract.exe
#pytesseract.tesseract_cmd = path_to_tesseract
 #Open image with PIL
#img = Image.open('logout.jpg')
#Extract text from image
#text = pytesseract.image_to_string(img,lang="eng")
#text2=text.strip()
#print(text2 == "Log Out")
#pos=gui.position()
#print(pos)
#Define path to tessaract.exe
pos=gui.position()
print(pos)

#gui.moveTo(x=952, y=619)
#sleep(2)
#gui.click(button="left")
#FindRest=gui.locateCenterOnScreen('restPassPage.jpg',confidence=0.75)
#print(FindRest)