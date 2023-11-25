from selenium import webdriver

driver = webdriver.Edge(executable_path=r"C:\Users\Admin\PycharmProjects\publicRepo\msedgedriver.exe")
driver.maximize_window()
driver.get("https://www.facebook.com")

email = driver.find_element_by_id("email")
email.send_keys("9600366215")

password = driver.find_element_by_id("pass")
password.send_keys("8870322116")

login = driver.find_element_by_name("login")
login.click()
