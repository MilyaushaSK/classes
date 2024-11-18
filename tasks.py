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
        
    def average_rating(self):
        all_grades = []
        for  grade in self.grades.values():
            all_grades += grade
        return sum(all_grades)/len(all_grades) if all_grades else 0
    
        
    def __lt__(self, other): 
        return self.average_rating() < other.average_rating()


    def __str__(self):
        average_grade = self.average_rating()
        return f'Имя: {self.name} \nФамилия: {self.surname} \n' \
               f'Средняя оценка за домашние задания: {average_grade} \n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'\
               f'Завершенные курсы: {", ".join(self.finished_courses)}'
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rating(self):
        all_grades = []
        for  grade in self.grades.values():
            all_grades += grade
        return sum(all_grades)/len(all_grades) if all_grades else 0

    
    def __lt__(self, some_lecturer2):
        return self.average_rating() < some_lecturer2.average_rating()

    def __str__(self):
        average_grade = self.average_rating()
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {average_grade}' 

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
        
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']
some_student.add_courses('Введение в программирование')

some_student2 = Student('Milya', 'Shigap', 'your_gender')
some_student2.courses_in_progress += ['Python', 'Git']
some_student2.add_courses('Введение в программирование')

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python', 'Git']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

some_lecturer2 = Lecturer('Some2', 'Buddy2')
some_lecturer2.courses_attached += ['Python']
 
some_reviewer.StudentsGrades(some_student, 'Python', 10)
some_reviewer.StudentsGrades(some_student, 'Git', 9.8)

some_reviewer.StudentsGrades(some_student2, 'Python', 10)
some_reviewer.StudentsGrades(some_student2, 'Python', 9.9)

some_student.LecturersGrades(some_lecturer, 'Python', 10)
some_student.LecturersGrades(some_lecturer, 'Python', 9.8)

some_student.LecturersGrades(some_lecturer2, 'Python', 10)
some_student.LecturersGrades(some_lecturer2, 'Python', 9.7)

if (some_lecturer.__lt__(some_lecturer2)):
    print(some_lecturer2.name, some_lecturer2.surname)
else:
    print(some_lecturer.name, some_lecturer.surname)

if (some_student.__lt__(some_student2)):
    print(some_student2.name, some_student2.surname)
else:
    print(some_student.name, some_student.surname) 
    
print(some_reviewer)
print(some_lecturer)
print(some_student)
