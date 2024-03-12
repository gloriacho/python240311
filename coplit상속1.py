class Person:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def printinfo(self):
        print(f"Info (name: {self.name}, number: {self.number})")

    def printpersondata(self):
        print(f"Info (name: {self.name}, number: {self.number})")


class Manager(Person):
    def __init__(self, name, number, title):
        super().__init__(name, number)
        self.title = title


class Employee(Person):
    def __init__(self, name, number, skill):
        super().__init__(name, number)
        self.skill = skill


# Test 1: Creating a Person
person1 = Person("Alice", "123-456-7890")
person1.printinfo()

# Test 2: Creating a Manager
manager1 = Manager("Bob", "987-654-3210", "Senior Manager")
manager1.printinfo()
print(f"Manager title: {manager1.title}")

# Test 3: Creating an Employee
employee1 = Employee("Charlie", "555-123-4567", "Python Developer")
employee1.printinfo()
print(f"Employee skill: {employee1.skill}")

# Test 4: Creating another Person
person2 = Person("Eve", "111-222-3333")
person2.printinfo()

# Test 5: Creating another Manager
manager2 = Manager("Frank", "444-555-6666", "Product Manager")
manager2.printinfo()
print(f"Manager title: {manager2.title}")

# Test 6: Creating another Employee
employee2 = Employee("Grace", "777-888-9999", "Java Developer")
employee2.printinfo()
print(f"Employee skill: {employee2.skill}")

# Test 7: Check if person1 and person2 have the same name
print(f"Same name for person1 and person2: {person1.name == person2.name}")

# Test 8: Check if manager1 and manager2 have different titles
print(f"Different titles for manager1 and manager2: {manager1.title != manager2.title}")

# Test 9: Check if employee1 and employee2 have different skills
print(f"Different skills for employee1 and employee2: {employee1.skill != employee2.skill}")

# Test 10: Creating a Person with no number
person3 = Person("Hank", "")
person3.printinfo()
