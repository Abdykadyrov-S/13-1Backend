class GeeksPeople:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self): # __str__ == print
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}"

geeks = GeeksPeople("Aktan", "aktan@gmail.com", "0771244745")
print(geeks)

class Student(GeeksPeople):
    def __init__(self, name, email, phone, student_id, group_where_study):
        GeeksPeople.__init__(self, name, email, phone)
        self.student_id = student_id
        self.group_where_study = group_where_study

    def study(self):
        print(f"{self.name} is studying in group {self.group_where_study}")


class Teacher(GeeksPeople):
    def __init__(self, name, email, phone, teacher_id, group_where_teach):
        GeeksPeople.__init__(self, name, email, phone)
        self.teacher_id = teacher_id
        self.group_where_teach = group_where_teach

    def teach(self):
        print(f"{self.name} is teaching in group {self.group_where_teach}")


class Admin(GeeksPeople):
    def __init__(self, name, email, phone, admin_id):
        GeeksPeople.__init__(self, name, email, phone)
        self.admin_id = admin_id

    def create_group(self, group_name):
        print(f"Admin {self.name} created a new group: {group_name}")


class Mentor(Student, Teacher):
    def __init__(self, name, email, phone, student_id, group_where_study, teacher_id, group_where_teach):
        Student.__init__(self, name, email, phone, student_id, group_where_study)
        Teacher.__init__(self, name, email, phone, teacher_id, group_where_teach)


student1 = Student("Abu", "Abu@email.com", "123-456-7890", "S001", "11-1")
teacher1 = Teacher("Nurbo", "Nurbo@email.com", "987-654-3210", "T001", "13-2")
admin1 = Admin("Aktan", "Aktan@email.com", "555-555-5555", "14-1")

mentor1 = Mentor("Nurai", "Nurai@email.com", "111-222-3333", "S002", "13-1", "T002", "GroupD")

student1.study()
teacher1.teach()
admin1.create_group("14-1")

mentor1.study()
mentor1.teach()

print("Hello World ")
