class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printinfo(self):
        return f"ID: {self.id}\nName: {self.name}\n"


class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    def printinfo(self):
        return super().printinfo() + f"Title: {self.title}\n"


class Employee(Person):
    def __init__(self, id, name, department):
        super().__init__(id, name)
        self.department = department

    def printinfo(self):
        return super().printinfo() + f"Department: {self.department}\n"


class TestPerson:
    def test_printinfo(self):
        person = Person(1, "John")
        assert person.printinfo() == "ID: 1\nName: John\n"


class TestManager:
    def test_printinfo(self):
        manager = Manager(2, "Jane", "HR Manager")
        assert manager.printinfo() == "ID: 2\nName: Jane\nTitle: HR Manager\n"


class TestEmployee:
    def test_printinfo(self):
        employee = Employee(3, "Doe", "Engineering")
        assert employee.printinfo() == "ID: 3\nName: Doe\nDepartment: Engineering\n"


# Add more test classes here if needed
