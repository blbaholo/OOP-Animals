import pytest
from animals_dir.animals import Dog, Cat, Home


def test_eat_method_for_dog_instance_argument_given():
    dog = Dog("Jam")
    assert dog.eat() == "Jam eats", "Incorrect output returned from eat method with given argument."


def test_eat_method_for_dog_instance_no_argument_given():
    dog = Dog()
    assert dog.eat() == "Rax eats", "Incorrect output returned from eat method with no argument given."


def test_sound_method_for_dog_instance():
    dog = Dog()
    assert dog.sound() == "Bark", "Sound method returned incorrect output for dog instance."


def test_sound_method_for_dog_instance_with_wrong_sound():
    dog = Dog()
    assert dog.sound() != "Meow", "Sound method doesn't return (Bark) for dog instance."

def test_eat_method_for_cat_instance_no_argument_given():
    cat = Cat()
    assert cat.eat() == "Stormy eats", "Incorrect output returned from eat method with no argument given."


def test_eat_method_for_cat_instance_argument_given():
    cat = Cat("Peanut")
    assert cat.eat() == "Peanut eats",  "Incorrect output returned from eat method with given argument."


def test_sound_method_for_cat_instance():
    cat = Cat()
    assert cat.sound() == "Meow", "Sound method returned incorrect output for cat instance."


def test_sound_method_for_cat_instance_with_wrong_sound():
    cat = Cat()
    assert cat.sound() != "Bark", "Sound method doesn't return (Meow) for cat instance."


def test_adopt_pet_method():
    dog = Dog()
    home = Home()
    assert home.adopt_pet(dog) == 1, "Adopt pet method returned incorrect number of pets adopted"
    cat = Cat()
    assert home.adopt_pet(cat) == 2, "Adopt pet method returned incorrect number of pets adopted"


def test_adopt_pet_method_raised_exception():
    dog = Dog()
    home = Home()
    with pytest.raises(ValueError, match="Can't adopt the same pet twice!"):
        home.adopt_pet(dog)
        home.adopt_pet(dog)


def test_make_all_sound_method():
    home = Home()
    dog = Dog()
    cat = Cat()
    home.adopt_pet(dog)
    home.adopt_pet(cat)
    assert home.make_all_sounds() == "Bark\nMeow", "Make all sound method returned incorrect sound for pets adopted."
