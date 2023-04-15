
# Import required packages. • Note : Install Selenium package.
import os
from selenium.webdriver.common.by import By
from selenium import webdriver

# Download chrome driver https://chromedriver.chromium.org/downloads using this URL
# Paste chrome driver's executable path from your machine
driver = webdriver.Edge()

# Give URL of Bugzilla
driver.get("http://192.168.1.104/bugzilla")

# You can do Full screen with this syntax.
driver.fullscreen_window()

# Click on file a bug
bug = driver.find_element(by=By.XPATH,value="//*[@id='enter_bug']").click()

# Give ID of a user
ID = driver.find_element(by=By.XPATH, value="//*[@id='Bugzilla_login']").send_keys("jayathisoft.dipak@gmail.com")

# Give password of a user
paswd = driver.find_element(by=By.XPATH, value="//*[@id='Bugzilla_password']").send_keys("Jayathi$6S")

# Click on login
login = driver.find_element(by=By.XPATH, value="//*[@id='log_in']").click()

# Select the product i.e., RAID
product = driver.find_element(by=By.XPATH, value="//*[@id='choose_product']/tbody/tr[1]/th/a").click()

# Select the component i.e.,Controller Card
component = driver.find_element(by=By.XPATH, value="//*[@id='v5_component']").click()

# Select version i.e., 1.3x
version = driver.find_element(by=By.XPATH, value="//*[@id='version']/option[3]").click()

# Select Severity i.e., Normal
severity = driver.find_element(by=By.XPATH, value="//*[@id='v4_bug_severity']").click()

# Select the hardware i.e., Dell Server
hardware = driver.find_element(by=By.XPATH, value="//*[@id='v5_rep_platform']").click()

# Select Operating System i.e., Windows
OS = driver.find_element(by=By.XPATH, value="//*[@id='v2_op_sys']").click()

# Select category i.e., Build
category = driver.find_element(by=By.XPATH, value="//*[@id='v3_cf_category']").click()

# Add description i.e., Unable to expand virtual volume
discription = driver.find_element(by=By.XPATH, value="//*[@id='short_desc']").send_keys("Unable to expand virtual volume")

# You can take screenshot of your screen, So you can check all your input. (Optional)
driver.save_screenshot('raid_bug.png')

# Submit a bug
comment = driver.find_element(by=By.XPATH, value="//*[@id='commit']").click()

# Close driver / Web page
driver.close()

# Open saved screenshot (pop-up saved screenshot)
os.startfile('raid_bug.png')

print('Bug has been filed successfully !!!')