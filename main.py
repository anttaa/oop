class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
        sum_grades = 0
        cnt_grades = 0
        for l in self.grades.values():
            sum_grades += sum(l)
            cnt_grades += len(l)
        return sum_grades / cnt_grades if cnt_grades > 0 else 0

    def __str__(self):
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за домашние задания: {self.average_rating()} \n' \
               f'Курсы в процессе изучения: {"".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы:  {"".join(self.finished_courses)}\n'

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_rating() == other.average_rating()

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_rating() <= other.average_rating()

    def __le__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_rating() < other.average_rating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rating(self):
        sum_grades = 0
        cnt_grades = 0
        for l in self.grades.values():
            sum_grades += sum(l)
            cnt_grades += len(l)
        return sum_grades / cnt_grades if cnt_grades > 0 else 0

    def __str__(self):
        return f'{super().__str__()}' \
               f'Средняя оценка за лекции: {self.average_rating()}\n'

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Student!')
            return
        return self.average_rating() == other.average_rating()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Student!')
            return
        return self.average_rating() <= other.average_rating()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Student!')
            return
        return self.average_rating() < other.average_rating()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def average_rating_students(lst, course):
    sum_grades = 0
    cnt_grades = 0
    for stud in lst:
        if isinstance(stud, Student) and course in stud.grades:
            sum_grades += sum(stud.grades[course])
            cnt_grades += len(stud.grades[course])
    return sum_grades / cnt_grades if cnt_grades > 0 else 0


def average_rating_lecturer(lst, course):
    sum_grades = 0
    cnt_grades = 0
    for lect in lst:
        if isinstance(lect, Lecturer) and course in lect.grades:
            sum_grades += sum(lect.grades[course])
            cnt_grades += len(lect.grades[course])
    return sum_grades / cnt_grades if cnt_grades > 0 else 0


if __name__ == '__main__':
    # Студенты
    studs = [Student('Артем', 'Акулов', 'мужской')]
    studs[0].courses_in_progress += ['Python']
    studs[0].finished_courses += ['Java']

    studs.append(Student('Ольга', 'Матвеева', 'женский'))
    studs[1].courses_in_progress += ['Python']
    studs[1].finished_courses += ['Oracle']

    studs.append(Student('Павел', 'Новиков', 'мужской'))
    studs[2].courses_in_progress += ['C++']
    studs[2].finished_courses += ['Oracle']

    # Лекторы
    lects = [Lecturer('Михаил', 'Хритов')]
    lects[0].courses_attached += ['Python']

    lects.append(Lecturer('Егор', 'Кузьмин'))
    lects[1].courses_attached += ['Python', 'C++']

    # Эксперты
    rev_1 = Reviewer('Александр', 'Соловкин')
    rev_1.courses_attached += ['Python']
    rev_1.rate_hw(studs[0], 'Python', 10)
    rev_1.rate_hw(studs[0], 'Python', 7)
    rev_1.rate_hw(studs[1], 'Python', 6)
    rev_1.rate_hw(studs[1], 'Python', 8)

    rev_2 = Reviewer('Ангелина', 'Ушакова')
    rev_2.courses_attached += ['Python', 'C++']
    rev_2.rate_hw(studs[2], 'C++', 9)
    rev_2.rate_hw(studs[2], 'C++', 8)

    studs[0].rate_hw(lects[0], 'Python', 10)
    studs[0].rate_hw(lects[1], 'Python', 8)
    studs[1].rate_hw(lects[0], 'Python', 9)
    studs[1].rate_hw(lects[1], 'Python', 8)
    studs[2].rate_hw(lects[1], 'C++', 10)
    studs[2].rate_hw(lects[1], 'C++', 8)

    print('Студенты:')
    print(studs[0])
    print(studs[1])
    print(studs[2])
    print('Лекторы:')
    print(lects[0])
    print(lects[1])
    print('Эксперты:')
    print(rev_1)
    print(rev_2)

    print('Средняя оценка за домашние задания по всем студентам: ', average_rating_students(studs, 'Python'))
    print('Средняя оценка за лекции всех лекторов: ', average_rating_lecturer(lects, 'Python'))
