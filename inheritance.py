class Animal():
    animal_type = "ANY"
    animal_food = "ANY"

    def __init__(self) -> None:
        print("ANIMAL CREATED")

    def what_kind_of_animal(self):
        print(self.animal_type)

    def what_kind_of_food(self):
        print(self.animal_food)

class Dog(Animal):
    def __init__(self) -> None:
        # super().__init__(self)
        self.animal_type = "DOG"
        self.animal_food = "MEAT"

x = Dog()
x.what_kind_of_animal()
x.what_kind_of_food()