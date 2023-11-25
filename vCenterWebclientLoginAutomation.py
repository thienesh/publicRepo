from selenium import webdriver

driver = webdriver.Edge(executable_path=r"C:\Users\Admin\PycharmProjects\publicRepo\msedgedriver.exe")
driver.maximize_window()
driver.get("https://192.168.1.199")

Advanced = driver.find_element_by_id("details-button")
Advanced.click()

ignore_continue = driver.find_element_by_partial_link_text("Continue")
ignore_continue.click()

launch_vsphere = driver.find_element_by_partial_link_text("(HTML5)")
launch_vsphere.click()

username = driver.find_element_by_id("username").send_keys("Administrator@vsphere.local")
password = driver.find_element_by_id("password").send_keys("Jayathi$6S")
login = driver.find_element_by_id("submit")
login.click()
