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

    # Присваеваем оценки лекторам за лекции 
    def lecturers_grades(self, lecturer, course, grade): 
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached 
            and course in self.courses_in_progress and grade <= 10):
             if course in lecturer.grades:
                lecturer.grades[course] += [grade]
             else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Вычисляем среднюю оценку за дз    
    def average_rating(self): 
        all_grades = []
        for  grade in self.grades.values():
            all_grades += grade
        return sum(all_grades)/len(all_grades) if all_grades else 0
    
    # Сравниваем между собой студентов по средней оценке за дз 
    def __lt__(self, other):  
        return self.average_rating() < other.average_rating()
   
    # Вычисляем среднюю оценку по курсу
    def get_grade(self, course_name): 
        if course_name in self.grades:
             return sum(self.grades[course_name]) / len(self.grades[course_name])
        
    def __str__(self):
        average_grade = self.average_rating()
        return (f'Имя: {self.name} \nФамилия: {self.surname} \n' 
               f'Средняя оценка за домашние задания: {average_grade} \n' 
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'
               f'Завершенные курсы: {", ".join(self.finished_courses)}')


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    # Вычисляем среднюю оценку за лекции
    def average_rating(self): 
        all_grades = []
        for  grade in self.grades.values():
            all_grades += grade
        return sum(all_grades)/len(all_grades) if all_grades else 0

    # Сравниваем между собой лекторов по средней оценке за лекции
    def __lt__(self, other_lecturer): 
        return self.average_rating() < other_lecturer.average_rating()
    
    # Вычисляем среднюю оценку по курсу
    def get_grade(self, course_name): 
        if course_name in self.grades:
             return sum(self.grades[course_name]) / len(self.grades[course_name])

    def __str__(self):
        average_grade = self.average_rating()
        return f'Имя: {self.name} \nФамилия: {self.surname} \n' \
               f'Средняя оценка за лекции: {average_grade}' 


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    # Присваеваем оценки студентам за дз
    def students_grades(self, student, course, grade): 
        if (isinstance(student, Student) and course in self.courses_attached 
            and course in student.courses_in_progress and grade <= 10):
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

other_student = Student('Milya', 'Shigap', 'your_gender')
other_student.courses_in_progress += ['Python', 'Git']
other_student.add_courses('Введение в программирование')

some_reviewer = Reviewer('Azat', 'Alimov')
some_reviewer.courses_attached += ['Python', 'Git']

other_reviewer = Reviewer('Almira', 'Sharapova')
other_reviewer.courses_attached += ['Python', 'Full-stack']

some_lecturer = Lecturer('Ildar', 'Galiev')
some_lecturer.courses_attached += ['Python']

other_lecturer = Lecturer('Ruslan', 'Polyakov')
other_lecturer.courses_attached += ['Python']

some_reviewer.students_grades(some_student, 'Python', 10)
some_reviewer.students_grades(some_student, 'Git', 9.8)

some_reviewer.students_grades(other_student, 'Python', 10)
some_reviewer.students_grades(other_student, 'Python', 9.9)

some_student.lecturers_grades(some_lecturer, 'Python', 10)
some_student.lecturers_grades(some_lecturer, 'Python', 9.8)

some_student.lecturers_grades(other_lecturer, 'Python', 10)
some_student.lecturers_grades(other_lecturer, 'Python', 9.7)

student_list = [some_student, other_student]
lector_list = [some_lecturer, other_lecturer]

# Вычисляем средную оценку за дз студентов по конкретному курсу
def course_rating(student_list, course):
    total_grade = 0
    total_students = 0 
    for student in student_list:
        grade = student.get_grade(course)
        total_grade += grade
        total_students += 1
    return total_grade / total_students  

# Вычисляем среднюю оценку за лекции всех лекторов в рамках курса
def lecture_rating(lector_list, course):
    total_grade = 0
    total_lectors = 0 
    for lector in lector_list:
        grade = lector.get_grade(course)
        total_grade += grade
        total_lectors += 1
    return total_grade / total_lectors

# Вызываем метод __str__
print(some_reviewer)
print(other_reviewer)
print(some_lecturer)
print(other_lecturer)
print(some_student)
print(other_student)

# Вызываем метод для сравнивнения лекторов по средней оценке
if some_lecturer.__lt__(other_lecturer): 
    print(f'У {other_lecturer.name} {other_lecturer.surname} средняя оценка за лекции больше,'
          f'чем у {some_lecturer.name} {some_lecturer.surname}')
else:
    print(f'У {some_lecturer.name} {some_lecturer.surname} средняя оценка за лекции больше,'
          f'чем у {other_lecturer.name} {other_lecturer.surname}')

# Вызываем метод для сравнивнения студентов по средней оценке
if some_student.__lt__(other_student):
    print(f'У {other_student.name} {other_student.surname} средняя оценка за дз больше,' 
          f'чем у {some_student.name} {some_student.surname}.')
else:
    print(f'У {some_student.name} {some_student.surname} средняя оценка за дз больше,' 
          f'чем у {other_student.name} {other_student.surname}.') 

# Вызываем функцию course_rating 
print(f'Средняя оценка за дз по всем студентам в рамках конкретного курса: ' 
      f'{course_rating(student_list, "Python")}')

# Вызываем функцию lecture_rating
print(f'Cредняя оценка за лекции всех лекторов в рамках курса: '
      f'{lecture_rating(lector_list, "Python")}')