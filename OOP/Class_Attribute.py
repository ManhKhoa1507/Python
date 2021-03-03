class Animal:
    species = ""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass

class Dog(Animal):
    species = "Dog"

    def speak(self):
        return f"{self.name} is speaking"

class Cat(Animal):
    species = "Cat"

    def speak(self):
        return f"{self.name} is speaking"

if __name__ == '__main__':

    jim = Cat("Jim", 3)
    miles = Cat("Miles", 4)
    my_pet = [jim, miles]

    for i in my_pet:
        print(i.speak())
    

