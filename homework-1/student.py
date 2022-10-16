"""
TASK 2

Write a base class to represent a student. Below is a starter code.
Feel free to add any more new features to your class.
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student.

class CFGStudent(<should inherit from Student>)
    create new methods that manage student's subjects (add/remove new subject and its grade to the dict)
    create a method to view all subjects taken by a student
    create a method (and a new variable) to get student's overall mark (use average)

"""


class Student:

    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.subjects = dict()


class CFGStudent(Student):

    def __init__(self, name, age, student_id, specialization):
        super().__init__(name, age, student_id)
        self.specialization = specialization

    def add_subject(self, subject, grade):
        self.subjects.update({subject: grade})
        print(f"The subject {subject} has been added to {self.name}'s account")

    def remove_subject(self, subject):
        self.subjects.pop(subject)
        print(f"The subject {subject} has been removed from {self.name}'s account.")

    def show_subject(self):
        print(f"{self.name} is taking the following subjects:", list(self.subjects))

    def overall_mark(self):
        average_mark = sum(self.subjects.values()) / len(self.subjects)
        print(f"{self.name}'s overall mark: {average_mark:.0f}")
        return average_mark


student_42 = CFGStudent(name='C', age=38, student_id=42, specialization='Software Engineer')
student_42.add_subject('Object-Orientated Programming', 95)
student_42.add_subject('Decorators', 86)
student_42.add_subject('Collections', 90)
student_42.remove_subject('Decorators')
student_42.show_subject()
student_42.overall_mark()
