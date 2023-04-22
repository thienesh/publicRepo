import os
import time
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

elif user in u2:
    time.sleep(0.5)
    for i in range(1,5):
        time.sleep(2)
        print(f"time taken:{i} seconds")
    print("Connection Established...Allow to medium performing server2:", s2)
    os.system(cmd2)

else:
    print("Allow to better performing server1:", s1)
    os.system(cmd1)
