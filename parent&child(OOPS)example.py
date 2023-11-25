# Define the class
class Parent:
    def __init__(self, name, age, occupation, sex):
        self.name = name
        self.age = age
        self.work = occupation
        self.sex = sex

    def info(self):
        gender_pronoun = "his" if self.sex.lower() == "male" else "her"
        print(
            f"My {self.gender()} is {self.name} and {gender_pronoun} age is {self.age} "
            f"and {gender_pronoun} occupation is {self.work}")

    def gender(self):
        return "Father's name" if self.sex.lower() == "male" else "Mother's name"


class Child_ren(Parent):
    def __init__(self, name, age, occupation, sex, children, child_gender):
        super().__init__(name, age, occupation, sex)
        self.child = children
        self.gender = child_gender

    def child_info(self):
        if self.gender.lower() == "male":
            print(f"{self.child} is son of {self.name}")

        else:
            print(f"{self.child} is daughter of {self.name}")


# Creating object of the defined class

father = Parent("M.Selvaraju", 56, "Quality Manager", "male")
mother = Parent("S.Mangayarkarasi", 50, "Teacher", "female")

son = Child_ren("M.Selvaraju", 56, "Quality Manager", "male", "Thienesh", "male")
girl = Child_ren("M.Selvaraju", 56, "Quality Manager", "male", "Sowmiya", "female")

# Calling a method of the object

father.info()
mother.info()
son.child_info()
girl.child_info()
