class Animal():
    def __init__(self,name,age,breed,weight):
        self.__name = name
        self.__age = age
        self.__breed = breed
        self.__weight = weight

    def communication(self):
        print(f"{self.__name()} made a noise")
# I did this -Yoram
    
    def eat(self,food):
        print(f"{self.__name()} ate food")
# I did this -Yoram
    
    def get_weight(self):
        return self.__weight

class Dog(Animal):
    def __init__(self, name, age, breed, weight):
        super().__init__(name, age, breed, weight)

    def lick(self):
        pass


class Cat(Animal):
    def __init__(self, name, age, breed, weight):
        super().__init__(name, age, breed, weight)

    def purr(self):
        pass

cat1= Cat("OMNI", 404, "omnipotent", "omnifinity")
print(cat1.get_weight())

# You should give functionality to the eat and communicate functions
