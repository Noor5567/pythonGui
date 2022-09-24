""" from PIL import Image
from pytesseract import pytesseract
import pyautogui as gui
from time import * 
path_to_tesseract = r'C: \\Program Files \\Tesseract-OCR \\tesseract.exe'
pytesseract.tesseract_cmd = path_to_tesseract
emailImg = Image.open('email.jpg')
text= pytesseract.image_to_string(emailImg,lang="eng")
text2=text.strip()
v="ahmadsel218@gmail.com"
print(text2==v) """

""" import webbrowser
webbrowser.open('http://www.python.org')
 """
""" 
SecPage=gui.locateCenterOnScreen("imgs \\securityCodePage.jpg",confidence=0.75)
if(SecPage is not None):
    enterCode=gui.locateCenterOnScreen("imgs \\enterCode.jpg",confidence=0.75)
    if(enterCode is not None):
     gui.click(enterCode[0],enterCode[1])
     gui.sleep(10)
    else:
     gui.moveTo(x=846, y=366)
     gui.click(button='left', clicks=2, interval=0.25)
     gui.press('backspace')  """
import pyautogui as gui
from time import * 
def plus_function():
    findPlusImage=gui.locateCenterOnScreen('imgs\\plus.jpg',confidence=0.75)
    if (findPlusImage is not None):
     gui.click(findPlusImage[0],findPlusImage[1])
     gui.write("https://www.facebook.com/",interval=0.20)
     sleep(2)
     gui.press('enter')
     sleep(10) ## END TO FIND PLUS IN BROWSER
plus_function()