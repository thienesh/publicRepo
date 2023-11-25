import pyautogui

x, y = pyautogui.position()
print(f"Position of X and Y :{x} & {y}")

pyautogui.FAILSAFE = False
# Move the mouse to specific coordinates
pyautogui.moveTo(0, 0, duration=1)  # Move to (100, 100) over 1 second

# Move the mouse relative to the current position
pyautogui.move(x, y, duration=1)  # Move x pixels right and y pixels down over 1 second

pyautogui.click()
