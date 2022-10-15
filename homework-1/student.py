"""

TASK 2

Write a base class to represent a student. Below is a starter code.
Feel free to add any more new features to your class.
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student.

"""


class Student:

    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.subjects = dict()


# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subjects (add/remove new subject and its grade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)


class CFGStudent(Student):

    def __init__(self, name, age, student_id, specialization):
        super().__init__(name, age, student_id)
        self.specialization = specialization

    #     create new methods that manage student's subjects (add/remove new subject and its grade to the dict)
    def add_subject(self, subject, grade):
        self.subjects.update({subject: grade})
        print(subject, grade)

    def remove_subject(self, subject):
        self.subjects.pop(subject)
        print(self.subjects)

    #     create a method to view all subjects taken by a student
    def show_subject(self):
        print(list(self.subjects))

    #     create a method (and a new variable) to get student's overall mark (use average)
    def overall_mark(self):
        average_mark = sum(self.subjects.values()) / len(self.subjects)
        print(average_mark)                     # round to a whole number


student = CFGStudent(name='C', age=38, student_id=3, specialization='Software Engineer')
student.add_subject('Object-Orientated Programming', 89)
student.add_subject('Decorators', 86)
student.add_subject('Collections', 90)

student.remove_subject('Decorators')

student.show_subject()
student.overall_mark()