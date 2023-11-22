#Define the class
class parent:
    def __init__(self, name, age, occupation, sex):
        self.name = name
        self.age = age
        self.work = occupation
        self.sex = sex

    def info(self):
        gender_pronoun = "his" if self.sex.lower() == "male" else "her"
        print(f"My {self.gender()} is {self.name} and {gender_pronoun} age is {self.age} and {gender_pronoun} occupation is {self.work}")


    def gender(self):
        return "Father's name" if self.sex.lower() == "male" else "Mother's name"


#Creating object of the defined class

father = parent("M.Selvaraju",56,"Quality Manager","male")
mother = parent("S.Mangayarkarasi",50,"Teacher","female")

#Calling a method of the object

father.info()
mother.info()
