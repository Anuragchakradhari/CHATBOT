import pyautogui
import pyperclip
import time

# Step 1: Click on the icon
pyautogui.click(854, 1188)
time.sleep(2)  # Wait for the window to open

# Step 2: Click and drag to select text
pyautogui.moveTo(1114 , 286)
pyautogui.mouseDown()
pyautogui.moveTo(1879, 1013, duration=0.5)
pyautogui.mouseUp()
time.sleep(0.5)

# Step 3: Copy selected text
pyautogui.hotkey('ctrl', 'c')
pyautogui.click()
time.sleep(0.5)

# Step 4: Get copied text
copied_text = pyperclip.paste()
print("Copied text:", copied_text)
