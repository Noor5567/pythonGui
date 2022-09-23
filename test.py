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
gui.hotkey('win')
sleep(2)
gui.write("chrome")
gui.press('enter')
sleep(2)
findPlusImage=gui.locateCenterOnScreen('plus.jpg',confidence=0.75)
if (findPlusImage is not None):
    gui.click(findPlusImage[0],findPlusImage[1])
    gui.write("https://www.facebook.com/")
    sleep(2)
    gui.press('enter')
    sleep(2)
FindHomePage=gui.locateAllOnScreen('HomaPage.jpg',confidence=0.75)
FindEmail=gui.locateCenterOnScreen('enterEmail.jpg',confidence=0.75)  #x=1175, y=266
FindPass=gui.locateCenterOnScreen('enterPassword.jpg',confidence=0.75)  #x=1135, y=341
FindLogin=gui.locateCenterOnScreen('login.jpg',confidence=0.75)
if(FindHomePage and FindEmail and FindPass and FindLogin is not None):
    gui.click(FindEmail[0],FindEmail[1])
    sleep(2)
    gui.write("ahmadsel218@gmail.com")
    sleep(3)
    gui.click(FindPass[0],FindPass[1])
    sleep(3)
    gui.write("5567")
    sleep(2)
    gui.click(FindLogin[0],FindLogin[1])
    sleep(20)
else:
    print("ERROR")
count=0
while True:
    Forgetpassimg=gui.locateCenterOnScreen("forgetPass.jpg",confidence=0.75)
    Forgetpassimg2=gui.locateCenterOnScreen("forgetpass2.jpg",confidence=0.75)
    if Forgetpassimg and Forgetpassimg2 is not None:
        print(Forgetpassimg," \\n") 
        print(Forgetpassimg2)
        break
    else:
        sleep(5)
        count+=1
        print(count)
    if(count==5):
        print("image not found")
        break
       


#gui.moveTo(x=952, y=619)
#sleep(2)
#gui.click(button="left")
#FindRest=gui.locateCenterOnScreen('restPassPage.jpg',confidence=0.75)
#print(FindRest)