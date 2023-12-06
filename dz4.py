class GeeksPeople():
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone 
    def __str__(self):
        return f"Имя - {self.name}, электронная почта - {self.email}, номер телефона - {self.phone}"
class Student(GeeksPeople):
    def __init__(self,name, email, phone, student_id, group_where_study):
        GeeksPeople.__init__(self, name, email, phone)
        self.student_id = student_id
        self.group_where_study = group_where_study
    def study(self):
        return super().__str__() + f"ID - {self.student_id},  Группа - {self.group_where_study}"

# student = Student("nurai", "nurai@gmail.com", 90999384, 1,"12-2B")
# print(student)
# student.study()
class Teacher(GeeksPeople):
    def __init__(self,name, email, phone, teacher_id, group_where_teach):
        GeeksPeople.__init__(self, name, email, phone)
        self.teacher_id = teacher_id
        self.group_where_teach = group_where_teach
    def teach(self):
        return super().__str__() + f"ID - {self.teacher_id},  Группа - {self.group_where_teach}"
    
teacher = Teacher("qwer","qwee",12,1,"12-1B")
print(teacher)
teacher.teach()

class Admin(GeeksPeople):
    def __init__(self,name, email, phone, admin_id, create_group_1):
        GeeksPeople.__init__(self, name, email, phone)
        self.admin_id = admin_id
        self.create_group_1 = create_group_1
    def create_group(self):
        return super().__str__() + f"ID - {self.admin_id},  Группа - {self.create_group_1}"
    
admin = Admin("qwe","qwe",12,1,"12-2B")
print(admin)
admin.create_group()

class Mentor(Student, Teacher):
    def __init__(self,name, email, phone, student_id, group_where_study, teacher_id, group_where_teach):
        Student.__init__(self,name, email, phone, student_id, group_where_study)
        Teacher.__init__(self,name, email, phone, teacher_id, group_where_teach)
mentor = Mentor('qwer', 'qwert', 123456, 123456,12345,2345,23456)
print(mentor)
mentor.study()
mentor.teach()
