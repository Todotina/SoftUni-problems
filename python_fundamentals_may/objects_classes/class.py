class Class:
    __students_count = 22

    def __init__(self, name: str):
        self.name = name
        self.students = []
        self.grades = []
        self.students_count = 0

    def add_student(self, name: str, grade: float):
        if Class.__students_count > self.students_count:
            self.students.append(name)
            self.grades.append(grade)
            self.students_count += 1

    def get_avg_grade(self):
        return f"{sum(self.grades) / len(self.grades):.2f}"

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {sum(self.grades)/len(self.grades):.2f}"

a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)