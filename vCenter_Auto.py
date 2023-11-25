# Open vCenter and take screenshot of home page

# Import required packages.
import os
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

# Download chrome driver https://chromedriver.chromium.org/downloads using this URL
# Paste chrome driver's executable path from your machine
driver = webdriver.Edge()

# Give URL of vCenter
driver.get("https://192.168.1.233/ui")

driver.find_element(by=By.XPATH, value="//*[@id='details-button']").click()
driver.find_element(by=By.XPATH, value="//*[@id='proceed-link']").click()

# Give ID of a user
ID = driver.find_element(by=By.XPATH, value="//*[@id='username']").send_keys("Administrator@vsphere.local")

# Give password of a user
paswd = driver.find_element(by=By.XPATH, value="//*[@id='password']").send_keys("Jayathi$6S")

# Login
log = driver.find_element(by=By.XPATH, value="//*[@id='submit']").click()
time.sleep(10)

# Screenshot of screen
driver.fullscreen_window()
screenshot = driver.save_screenshot('team0.png')

# Pop-up saved screenshot
os.startfile('team0.png')