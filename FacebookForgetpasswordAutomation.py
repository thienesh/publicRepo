from selenium import webdriver

driver = webdriver.Edge(executable_path=r"C:\Users\Admin\PycharmProjects\publicRepo\msedgedriver.exe")
driver.maximize_window()
driver.get("https://www.facebook.com")

for_link = driver.find_elements_by_link_text("Forgotten password?")
if for_link:
    for_link[0].click()
else:
    print("Element with link text 'Forgotten password?' not found")

email = driver.find_element_by_id("identify_email")
email.send_keys("9600366215")

search = driver.find_element_by_id("did_submit")
search.click()
