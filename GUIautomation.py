import pyautogui

# Get the current mouse position
x, y = pyautogui.position()
print(f"Mouse position: x={x}, y={y}")

# Click the left mouse button at a specific location
pyautogui.click(x, y)
