import pyautogui as gui
from time import * 
from random import randint 
from PIL import Image
from pytesseract import pytesseract
import datetime
#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract
message=["Hi","Hello","Aloha"]
message2=["How Are You ?","Are You Available Today ?","Cannot Talk Right Now !"]
name="noor barakat"
email="ahmadsel218@gmail.com"
password="0795848996"
gmailLink="https://accounts.google.com/"
gui.alert("HI",timeout=2000)
gui.hotkey('win')
sleep(5)
gui.write("firefox",interval=0.20)
sleep(2)
gui.press("enter")
## START TO FIND PLUS IN BROWSER
findPlusImage=gui.locateCenterOnScreen('imgs\\plus.jpg',confidence=0.75)
findPlusImage2=gui.locateCenterOnScreen('imgs\\plusDark.jpg',confidence=0.75)
if (findPlusImage is not None):
 gui.click(findPlusImage[0],findPlusImage[1])
 gui.write("https://www.facebook.com/",interval=0.20)
 sleep(2)
 gui.press('enter')
 sleep(3)
 gui.click(button='left')
elif(findPlusImage2 is not None):
    gui.click(findPlusImage2[0],findPlusImage2[1])
    gui.write("https://www.facebook.com/",interval=0.20)
    sleep(2)
    gui.press('enter')
    sleep(3) 
    gui.click(button='left')
    sleep(2)## END TO FIND PLUS IN BROWSER
## START FIND HOME AND EMAIL AND PASSWORD AND LOGIN IMAGES
FindHomePage=gui.locateAllOnScreen('imgs\\HomaPage.jpg',confidence=0.75)
FindEmail=gui.locateAllOnScreen('imgs\\enterEmail.jpg',confidence=0.75)  #x=1175, y=266
FindPass=gui.locateAllOnScreen('imgs\\enterPassword.jpg',confidence=0.75)  #x=1135, y=341
FindLogin=gui.locateAllOnScreen('imgs\\login.jpg',confidence=0.75)
if(FindHomePage and FindEmail and FindPass and FindLogin is not None):
    gui.click(FindEmail[0],FindEmail[1])
    sleep(2)
    gui.click(FindEmail[0],FindEmail[1])
    sleep(2)
    gui.write(email,interval=0.20)
    sleep(3)
    gui.click(FindPass[0],FindPass[1])
    sleep(3)
    gui.write(password,interval=0.20)
    sleep(2)
    gui.click(FindLogin[0],FindLogin[1])
    sleep(10)
else:
    print("Canont Find The Homescreen or email or password or login images") ## END FIND HOME AND EMAIL AND PASSWORD AND LOGIN IMAGES
## START FORGET PASSWORD
count=0
while True:
    Forgetpassimg=gui.locateCenterOnScreen("imgs\\forgetPass.jpg",confidence=0.75)
    Forgetpassimg2=gui.locateCenterOnScreen("imgs\\forgetpass2.jpg",confidence=0.75)
    if Forgetpassimg and Forgetpassimg2 is not None:
        gui.click(Forgetpassimg2[0],Forgetpassimg2[1])
        sleep(2)
        break
    else:
        sleep(5)
        count+=1
    if(count==5):
        break
RestPass=gui.locateCenterOnScreen("imgs\\restPassPage.jpg",confidence=0.75)
if(RestPass is not None):
    emailImg = Image.open('imgs\\email.jpg')
    emailText= pytesseract.image_to_string(emailImg,lang="eng")
    emailText2=emailText.strip()
    if(emailText2==email):
        ConImg=gui.locateCenterOnScreen("imgs\\continue.jpg",confidence=0.75)
        gui.click(ConImg[0],ConImg[1])
        sleep(20)
        SecPage=gui.locateCenterOnScreen("imgs\\securityCodePage.jpg",confidence=0.75)
        if(SecPage is not None):
            enterCode=gui.locateCenterOnScreen("imgs\\enterCode.jpg",confidence=0.75)
            gui.click(enterCode[0],enterCode[1])
            sleep(10)
        else:
            gui.moveTo(x=846, y=366)
            gui.click(button='left', clicks=2, interval=0.25)
            gui.press('backspace')
            sleep(5) 
    findPlusImage=gui.locateCenterOnScreen('imgs\\plus.jpg',confidence=0.75)
    if (findPlusImage is not None):
     gui.click(findPlusImage[0],findPlusImage[1])
     gui.write(gmailLink,interval=0.20)
     sleep(2)
     gui.press('enter')
     sleep(10)
chooseAcc=gui.locateCenterOnScreen("imgs\\chooseAcc.jpg",confidence=0.75)
if(chooseAcc is not None):
    findEmail=gui.locateCenterOnScreen("imgs\\findEmail.jpg",confidence=0.75)
    if(findEmail is not None):
        gui.click(findEmail[0],findEmail[1])
        sleep(2)
        gui.press('backspace')
        gui.press('backspace')
        sleep(2)
        gui.write(password)
        sleep(2)
        Nextimage=gui.locateCenterOnScreen("imgs\\Next.jpg",confidence=0.75)
        if(Nextimage is not None):
            gui.click(Nextimage[0],Nextimage[1])
            sleep(2)
            optionImage=gui.locateCenterOnScreen("imgs\\option.jpg",confidence=0.75)
            if(optionImage is not None):
                gui.click(optionImage[0],optionImage[1])
                sleep(2)
                
## START FIND MESSANGER BUTTON AND SEARCH FOR THE NAME
findMessangerImage=gui.locateCenterOnScreen('imgs\\mes.jpg',confidence=0.75)
if(findMessangerImage is not None):
    gui.click(findMessangerImage[0],findMessangerImage[1])
    sleep(2)
    gui.moveTo(x=1721, y=195)
    sleep(2)
    gui.click(button='left')
    sleep(2)
    gui.write(name,interval=0.20)
    sleep(2)
    gui.moveTo(x=1739, y=241)
    sleep(2)
    gui.click(button='left')
    sleep(2)
else:
    print("none")## END FIND MESSANGER BUTTON AND SEARCH FOR THE NAME
## START CALL 
callImage=gui.locateCenterOnScreen('imgs\\call.jpg',confidence=0.75)
if(callImage is not None):
    gui.click(callImage[0],callImage[1])
cant_call=gui.locateAllOnScreen('imgs\\cant_call.jpg',confidence=0.75)
if (cant_call is not None):
    gui.moveTo(x=1595, y=139)
    sleep(2)
    gui.click(button='left')
    sleep(5)
    gui.moveTo(x=1689, y=1011)
    sleep(2)
    gui.write(message[randint(0, len(message)-1)]+" "+ name +" "+message2[randint(0, len(message2)-1)],interval=0.20)
    sleep(2)
    gui.press('enter')
else: 
    print("Cannot Call And Send Message") ##END CALL
# START SEARCH USER BUTTON AND LOGOUT BUTTON AND CLICK IT
userImage=gui.locateCenterOnScreen('imgs\\user.jpg',confidence=0.75)
logoutImage= Image.open('imgs\\logout.jpg')
logoutText = pytesseract.image_to_string(logoutImage,lang="eng")
logoutText2=logoutText.strip()
if (userImage is not None):
     gui.click(userImage[0],userImage[1])
     sleep(2)
     if(logoutText2 == "Log Out"):
         gui.moveTo(x=1721, y=491)
         sleep(2)
         gui.click(button='left')
     else:
         print("Cannot Log Out")
else:
     print("Image Not Found") # END SEARCH USER BUTTON AND LOGOUT BUTTON AND CLICK IT
#sleep(5)
#pos=gui.position()
#print(pos)


