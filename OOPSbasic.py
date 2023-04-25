class Maths:
    def __init__(self, add, sub, mul):
        self.add = add
        self.sub = sub
        self.mul = mul

    def add_fun(self):
        print("Addition of numbers: ", self.add + 5)

    def sub_fun(self):
        print("Subtraction of numbers:", self.sub - 3)

    def mul_fun(self):
        print("Multiplication of numbers:", self.mul * 10)


calc1 = Maths(1, 5, 3)
calc2 = Maths(2, 6, 5)

calc1.sub_fun()
calc1.add_fun()
calc1.mul_fun()

calc2.add_fun()
calc2.sub_fun()
calc2.mul_fun()
