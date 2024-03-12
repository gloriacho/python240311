# class1.py

#defintion of class
class Person:
    def __init__(self) -> None:
        self.name = "default name"

    def print(self):
        print("My name is {0}".format(self.name))

p1 = Person()
p2 = Person()

p1.name = "EJ"
p1.print()
p2.print()