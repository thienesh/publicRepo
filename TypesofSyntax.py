'''
In Python, syntax refers to the set of rules that define how programs written in the language should be structured. Here are some of the most commonly used syntax elements in Python:

1. Comments: Comments are used to explain the code and make it more readable for others. In Python, comments start with the hash symbol (#).

2. Variables: In Python, variables are used to store data. A variable is defined by assigning a value to it using the equal (=) sign.

3. Data Types: Python supports various data types such as integers, floats, strings, Boolean values, lists, tuples, and dictionaries.

4. Operators: Operators are used to perform operations on variables and values. Python supports arithmetic, comparison, logical, and bitwise operators.

5. Control Structures: Python supports control structures such as if-else statements, while and for loops, and break and continue statements.

6. Functions: Functions are blocks of code that can be called multiple times in a program. In Python, functions are defined using the def keyword.

7. Classes: Classes are used to create objects in Python. They consist of attributes (data) and methods (functions).

Here is an example of Python code that uses several of these syntax elements:
'''


# Define a function
def add_numbers(a, b):
    sum = a + b
    return sum


# Define a variable
x = 5

# Use an if statement
if x > 3:
    print("x is greater than 3")

# Create a list
my_list = [1, 2, 3, 4]

# Use a for loop
for num in my_list:
    print(num)


# Define a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, my name is " + self.name)


# Create an object of the Person class
person1 = Person("John", 25)

# Call a method of the object
person1.say_hello()
