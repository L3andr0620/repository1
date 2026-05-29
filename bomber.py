import pyautogui
import time

print("Go to WhatsApp web and open the chat you wanna bomb. You have 5 s")
time.sleep(5)

for i in range(5):  # Number of messages you wanna send
    pyautogui.write("Hello!") # Message you wanna send
    pyautogui.press("enter")
    time.sleep(0.2)
