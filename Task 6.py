class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturer_list = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average = 0
        Lecturer.lecturer_list.append(self)

    def __average_grade(self):
        quantity = 0
        total = 0
        for key, value in self.grades.items():
            quantity += len(value)
            for g in range(len(value)):
                total += value[g]
        average = round(float(total / quantity), 1)
        self.average = average

    def __str__(self):
        self.__average_grade()
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за лекции: {self.average}'


    def __lt__(self, other):
        self.__average_grade()
        other.__average_grade()
        if other.average < self.average:
            print(f'{self.name} {self.surname} лучше подает материал, чем {other.name} {other.surname}!')
        elif other.average == self.average:
            print(f'{self.name} {self.surname} и {other.name} {other.surname} одинаково хорошо подают материал!')
        else:
            print(f'{self.name} {self.surname} хуже подает материал, чем {other.name} {other.surname}!')


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname}'


class Student:
    student_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average = 0
        Student.student_list.append(self)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades and 1 <= grade <= 10:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __average_grade(self):
        quantity = 0
        total = 0
        for key, value in self.grades.items():
            quantity += len(value)
            for g in range(len(value)):
                total += value[g]
        average = round(float(total / quantity), 1)
        self.average = average

    def __str__(self):
        self.__average_grade()
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за домашние задания:{self.average} \n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        self.__average_grade()
        other.__average_grade()
        if other.average < self.average:
            print(f'{self.name} {self.surname} лучше учится, чем {other.name} {other.surname}!')
        elif other.average == self.average:
            print(f'{self.name} {self.surname} и {other.name} {other.surname} учатся одинаково!')
        else:
            print(f'{self.name} {self.surname} хуже учится, чем {other.name} {other.surname}!')


reviewer1 = Reviewer('Bill', 'Dumb')
reviewer2 = Reviewer('Greg', 'Binary')
lector1 = Lecturer('Bob', 'Oak')
lector2 = Lecturer('Den', 'Bazinga')
student1 = Student('Alexey', 'Yung', 'male')
student2 = Student('Aleksey', 'Iung', 'male')

reviewer1.courses_attached += ['python']
reviewer1.courses_attached += ['git']
reviewer2.courses_attached += ['python']
reviewer2.courses_attached += ['git']

student1.courses_in_progress += ['python']
student1.courses_in_progress += ['git']
student1.finished_courses += ['Введение в программирование']
student2.courses_in_progress += ['python']
student2.courses_in_progress += ['git']
student2.finished_courses += ['Введение в программирование']

lector1.courses_attached += ['python']
lector2.courses_attached += ['git']

student1.rate_lecturer(lector1, 'python', 9)
student1.rate_lecturer(lector2, 'git', 6)
student2.rate_lecturer(lector1, 'python', 10)
student2.rate_lecturer(lector2, 'git', 7)

reviewer1.rate_hw(student1, 'python', 5)
reviewer1.rate_hw(student1, 'git', 5)
reviewer1.rate_hw(student2, 'python', 4)
reviewer1.rate_hw(student2, 'git', 4)
reviewer2.rate_hw(student1, 'python', 5)
reviewer2.rate_hw(student1, 'git', 4)
reviewer2.rate_hw(student2, 'python', 3)
reviewer2.rate_hw(student2, 'git', 4)

def print__str():
    print(student1)
    print()
    print(lector1)
    print()
    print(reviewer1)
    print()
    print(student2)
    print()
    print(lector2)
    print()
    print(reviewer2)
    print()
    lector1.__lt__(lector2)
    print()
    student2.__lt__(student1)
    print()


def st_course_average_grade(student_list, course_name):
    sum1 = []
    sum2 = 0
    for i in student_list:
        for course, values in i.grades.items():
            if course == course_name:
                sum1 += values
    for g in sum1:
        sum2 += g
    print(f'Средний балл студентов по курсу {course_name}: {sum2 / len(sum1)}.')


def lect_course_average_grade(lector_list, course_name):
    sum1 = []
    sum2 = 0
    for i in lector_list:
        for course, values in i.grades.items():
            if course == course_name:
                sum1 += values
    for g in sum1:
        sum2 += g
    print(f'Средний балл преподавателей по курсу {course_name}: {sum2 / len(sum1)}.')

print__str()
st_course_average_grade([student1, student2], 'python')
lect_course_average_grade([lector1, lector2], 'python')


