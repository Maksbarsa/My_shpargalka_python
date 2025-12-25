class Human:
    a = "hogvards"
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Human):
    def __init__(self, name, university, age=2):
        super().__init__(name, age)   # вызов родительского конструктора
        self.university = university

obj = Student("john", "mgu")
print(f"{obj.name} {Human.a}")