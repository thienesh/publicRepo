class actors:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


    def my_fun(self):
        if self.sex.lower() == "female":
            print(f"The actor who came here is {self.name}")
            print(f"Her age is {self.age}")
            print("She is an top actress")
        else:
            print(f"The actor who came here is {self.name}")
            print(f"His age is {self.age}")
            print("He is an brilliant actor")


class nominee(actors):
    def __init__(self, name, age, sex, award_category):
        super().__init__(name, age, sex)
        self.award_category = award_category


    def selected(self):
        if self.sex.lower() == "female":
            print(f"Let's welcome actress {self.name} ")
            print(f"She is nominated for the {self.award_category} Award.")
        else:
            print(f"Let's welcome actor {self.name}")
            print(f"He is nominated for the {self.award_category} Award.")
        print(f"THANK YOU!! {self.name}")


actor1 = actors("Surya", 40, "Male")
actor2 = actors("Nayanthara", 38, "Female")
actor3 = actors("Karthi", 39, "Male")
actor4 = actors("Trisha", 42, "Female")
print("Nominees Arrived!! \n")
actor1.my_fun()
actor2.my_fun()
actor3.my_fun()
actor4.my_fun()
print("\nAnd let's see the best actor for following category\n")
print("Male Category")
nominee1 = nominee("Surya", 40, "Male", "Best Male Actor")
nominee2 = nominee("Trisha", 42, "Female", "Best Female Actress")
nominee3 = nominee("Karthi", 39, "Male", "Best Male Actor")
nominee4 = nominee("Nayanthara", 38, "Female", "Best Female Actress")

nominee1.selected()
print("\nFemale Category")
nominee2.selected()
print("\nThank you SIIMMA!! for conducting the award function.")