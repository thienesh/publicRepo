def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


try:
    result = div(10, 0)
    print("Results:", result)

except ValueError as e:
    print("Error:", str(e))
   