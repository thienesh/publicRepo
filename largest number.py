a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
c = int(input("Enter the number:"))

largest_number = ""

if a > b:
    largest_number = a
elif b > c:
    largest_number = b
elif c > a:
    largest_number = c

print("So the largest number is ", largest_number)
