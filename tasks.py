class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name) 

    def LecturersGrades(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and grade <= 10:
             if course in lecturer.grades:
                lecturer.grades[course] += [grade]
             else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def StudentsGrades(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
reviewer = Reviewer('Some', 'Buddy')
reviewer.courses_attached += ['Python']

lecturer = Lecturer('Some', 'Buddy')
lecturer.courses_attached += ['Python']
 
reviewer.StudentsGrades(best_student, 'Python', 10)
reviewer.StudentsGrades(best_student, 'Python', 10)
reviewer.StudentsGrades(best_student, 'Python', 10)

best_student.LecturersGrades(lecturer, 'Python', 10)
best_student.LecturersGrades(lecturer, 'Python', 10)
best_student.LecturersGrades(lecturer, 'Python', 9.9)

 
print(best_student.grades)
print(lecturer.grades)