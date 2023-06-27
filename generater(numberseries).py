n = int(input("Enter the number: "))


def gen_num(n):
    for i in range(1, n):
        yield i


x = gen_num(n)
# print(x)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

for times in range(1, n):
    print(next(x))
