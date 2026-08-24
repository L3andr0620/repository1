import pyautogui
import time

print("[INFO] Initializing UI load test. Switch to the target application window. 5-second delay active")
time.sleep(5)

# Simulate rapid user input to test UI input-field resilience and rate-limiting
for i in range(5):  
    pyautogui.write("System Load Test - Automated Input Message") 
    pyautogui.press("enter")
    time.sleep(0.2)
