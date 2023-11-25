a, b = 1, 1
count = 0
n = int(input("Enter:"))
print("Fibonacci series..")
while count < n:
    print(a)
    sum1 = a + b
    a = b
    b = sum1
    count += 1
