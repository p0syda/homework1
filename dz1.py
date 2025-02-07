class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        if not self.grades:
            return 0
        total = sum(sum(grades) for grades in self.grades.values())
        count = sum(len(grades) for grades in self.grades.values())
        return total / count

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Создание экземпляра студента
best_student = Student('Maxim', 'Ayukin', 'Male')
best_student.courses_in_progress += ['Python']

# Создание экземпляра лектора
cool_lecturer = Lecturer('Egor', 'Budancev')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.grades['Python'] = [10, 10, 10]

# Создание экземпляра эксперта
cool_reviewer = Reviewer('Egor', 'Budancev')
cool_reviewer.courses_attached += ['Python']

# Выставление оценок студенту
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

# Вывод средней оценки лектора
print(f"Средняя оценка лектора {cool_lecturer.name} {cool_lecturer.surname}: {cool_lecturer.average_grade()}")

# Вывод оценок студента
print(f"Оценки студента {best_student.name} {best_student.surname} по курсу Python: {best_student.grades}")