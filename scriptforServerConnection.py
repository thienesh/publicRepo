import os
import time
from selenium import webdriver

u1 = ["rama", "ram", "krish"]
u2 = ["sama", "sam", "sudo"]

s1 = "amazon.com"
s2 = "amazon.com"
cmd1 = "ping " + s1
cmd2 = "ping " + s2
user = input("Enter the name:")

if user in u1:
    print("Allow to better performing server1:", s1)
    os.system(cmd1)
    driver = webdriver.Edge()
    driver.get("http://www.amazon.com")
    driver.fullscreen_window()
    time.sleep(7)
    print("Successfully connected to amazon server!!")
    driver.close()

elif user in u2:
    time.sleep(0.5)
    for i in range(1, 5):
        time.sleep(2)
        print(f"time taken:{i} seconds")
    print("Connection Established...Allow to medium performing server2:", s2)
    os.system(cmd2)
    driver = webdriver.Edge()
    driver.get("http://www.amazon.com")
    driver.fullscreen_window()
    time.sleep(7)
    print("Successfully connected to amazon server!!")
    driver.close()

else:
    print("Allow to better performing server1:", s1)
    os.system(cmd1)
    driver = webdriver.Edge()
    driver.get("http://www.amazon.com")
    driver.fullscreen_window()
    time.sleep(7)
    print("Successfully connected to amazon server!!")
    driver.close()
