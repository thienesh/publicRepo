# program to print a list in reverse order with out using a inbuilt method
list1 = [1, 2, 3, 4, 5]
list1 = list1[::-1]
print(list1)

my_tuple = (1, 2, 3, 4, 5)
reversed_tuple = my_tuple[::-1]
print(reversed_tuple)  # Output: (5, 4, 3, 2, 1)

list1 = (1, 2, 3, 4, 5)
list1 = list(list1)
list1.reverse()
print(list1)
