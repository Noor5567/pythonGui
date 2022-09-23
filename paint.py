import pyautogui as gui
from time import * 
gui.hotkey("win")
gui.write("paint")
gui.press("enter")
sleep(5)
distance = 200
while distance > 0:
        gui.drag(distance, 0, duration=0.5)     move right
        distance -= 5
        gui.drag(0, distance, duration=0.5)     move down
        gui.drag(-distance, 0, duration=0.5)    move left
        distance -= 5
        gui.drag(0, -distance, duration=0.5)    move up