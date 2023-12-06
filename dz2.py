class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
    def introduce_myself(self):
        print(f"Имя - {self.fullname}, возраст - {self.age}, женат {self.is_married}")
person = Person('ytrewq', 50, 'yes')
person.introduce_myself()
class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience):
        Person.__init__(self, fullname, age, is_married)
        self.experience = experience
        self.salary = 30000

    def sum_salary(self):
        for i in range(self.experience):
            self.salary += 3000
        print(f"{self.fullname}, ваша зарплата {self.salary}")
result = Teacher('qwerty', 20, 'no', 3)
result.sum_salary()
