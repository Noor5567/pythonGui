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
import string 
#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract
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
gui.hotkey('win')
sleep(2)
gui.write("firefox",interval=0.20)
gui.press("enter")
sleep(3)
gui.write("https://www.facebook.com/",interval=0.20)
gui.press("enter")
sleep (5)
gui.click(button='left')
sleep(3)
#logoutImage= Image.open('imgs\\firefox.png')
#logoutText = pytesseract.image_to_string(logoutImage,lang="eng")
#logoutText2=logoutText.strip()
#if "Firefox" in logoutText:
FindHomePage=gui.locateAllOnScreen('imgs\\HomaPage.jpg',confidence=0.75)
FindEmail=gui.locateAllOnScreen('imgs\\enterEmail.jpg',confidence=0.75)  #x=1175, y=266
FindPass=gui.locateAllOnScreen('imgs\\enterPassword.jpg',confidence=0.75)  #x=1135, y=341
FindLogin=gui.locateAllOnScreen('imgs\\login.jpg',confidence=0.75)
print(FindHomePage," ",FindEmail," ",FindPass," ",FindLogin)
    
#gui.press('enter')
#sleep(2)
#gui.moveTo(x=952, y=619)
#sleep(2)
#gui.click(button="left")
#FindRest=gui.locateCenterOnScreen('restPassPage.jpg',confidence=0.75)
#print(FindRest)