l1 = []
l2 = []
for i in range(1, 1001):
    l1.append(i)
print(l1)

# To print the last number
print(f"[{l1[-1]}]")

# To print the length of the numbers
length = len(l1)
print(length)

# To print the index of numbers
len1 = len(l1)
print(list(range(len1)))

# To print the alternative numbers in range
for i in range(1, 1001, 100):
    l2.append(i)
print(l2)
