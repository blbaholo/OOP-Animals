class Animal:
    def __init__(self, name):
        self.__name = name

    def eat(self):
        return f"{self.__name} eats"

    def sound(self):
        return "sound..."


class Dog(Animal):
    def __init__(self, name="Rax"):
        super().__init__(name)

    def sound(self):
        return "Bark"


class Cat(Animal):
    def __init__(self, name="Stormy"):
        super().__init__(name)

    def sound(self):
        return "Meow"


class Home:
    def __init__(self):
        self.list_of_animals = []

    def adopt_pet(self, animal):
        if animal not in self.list_of_animals:
            self.list_of_animals.append(animal)
        else:
            raise ValueError("Can't adopt the same pet twice!")
        return len(self.list_of_animals)

    def make_all_sounds(self):
        list_of_animal_sound = [pet.sound() for pet in self.list_of_animals]
        animals_sounds = "\n".join(list_of_animal_sound)
        return animals_sounds


if __name__ == "__main__":
    home = Home()
    dog1 = Dog("Simba")
    dog2 = Dog("Jam")
    cat = Cat("Smokey")

    print(home.make_all_sounds())
    print(home.adopt_pet(dog1))
    print(home.make_all_sounds())

    print(home.adopt_pet(cat))
    print(home.make_all_sounds())

    print(home.adopt_pet(cat))
    print(home.make_all_sounds())
