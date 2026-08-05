class Animal:
    def sound(self):
        print("Animals make sounds")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


class Cow(Animal):
    def sound(self):
        print("Cow moos")


dog = Dog()
cat = Cat()
cow = Cow()

dog.sound()
cat.sound()
cow.sound()