class Faculty:
    def __init__(self, name, abbreviation, study_field):
        self.name = name
        self.abbreviation = abbreviation
        self.enrolled_students = []  
        self.graduated_students = []  
        self.study_field = study_field

    def add_student(self, student):
        self.enrolled_students.append(student)

    def graduate_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            self.graduated_students.append(student)

    def get_enrolled_students(self):
        return self.enrolled_students

    def get_graduated_students(self):
        return self.graduated_students
    