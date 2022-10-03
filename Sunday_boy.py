import webbrowser as wb
import pyautogui
import time
       
def on_robot():
    wb.open('http://192.168.43.172/LED=ON')
    time.sleep(8)
    pyautogui.hotkey('Ctrl', 'w')      
def off_robot():
    wb.open('http://192.168.43.172/LED=OFF')
    time.sleep(8)
    pyautogui.hotkey('Ctrl', 'w')
