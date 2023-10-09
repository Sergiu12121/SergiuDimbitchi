from Student import Student
from Faculty import Faculty
from StudyField import StudyField

class TUMBoard:
    def __init__(self):
        self.faculties = []

    def find_faculty_by_email(self, email):
        for faculty in self.faculties:
            for student in faculty.enrolled_students:
                if student.email == email:
                    return faculty
        return None

    def faculty_operations(self):
        print("\nFaculty Operations:")
        print("cs. Create and assign a student to a faculty")
        print("gs. Graduate a student from a faculty")
        print("de. Display current enrolled students")
        print("dg. Display graduates")
        print("sbf. Check if a student belongs to a faculty")
        faculty_choice = input("Enter your choice: ")

        if faculty_choice == "cs":
            # Create and assign a student to a faculty
            first_name = input("Enter student's first name: ")
            last_name = input("Enter student's last name: ")
            email = input("Enter student's email: ")
            enrollment_date = input("Enter enrollment date (DD-MM-YYYY): ")
            date_of_birth = input("Enter date of birth (DD-MM-YYYY): ")

            print("Available Faculties:")
            for i, faculty in enumerate(self.faculties, start=1):
                print(f"{i}. {faculty.name} ({faculty.abbreviation})")

            faculty_index = int(input("Select a faculty (enter the number): ")) - 1

            if 0 <= faculty_index < len(self.faculties):
                student = Student(first_name, last_name, email, enrollment_date, date_of_birth)
                self.faculties[faculty_index].add_student(student)
                print(f"Student {student.first_name} {student.last_name} assigned to {self.faculties[faculty_index].name}")

        elif faculty_choice == "gs":
            # Graduate a student from a faculty
            email = input("Enter student's email: ")
            faculty = self.find_faculty_by_email(email)

            if faculty:
                student = next((s for s in faculty.enrolled_students if s.email == email), None)
                if student:
                    faculty.graduate_student(student)
                    print(f"Student {student.first_name} {student.last_name} graduated from {faculty.name}")
                else:
                    print("Student not found in the selected faculty.")
            else: 
                print("Faculty not found for the given email.")

        elif faculty_choice == "de":
            # Display current enrolled students
            print("Available Faculties:")
            for i, faculty in enumerate(self.faculties, start=1):
                print(f"{i}. {faculty.name} ({faculty.abbreviation})")
            faculty_index = int(input("Select a faculty (enter the number): ")) - 1
            if 0 <= faculty_index < len(self.faculties):
                faculty = self.faculties[faculty_index]
                enrolled_students = faculty.get_enrolled_students()
                for student in enrolled_students:
                    print(f"Enrolled at {faculty.name} on {student.enrollment_date}: {student.first_name} {student.last_name} ")
            else:
                print("Invalid faculty selection.")

        elif faculty_choice == "dg":
            # Display graduates
            graduated_students = faculty.get_graduated_students()
            for student in graduated_students:
                print(f"Graduated {faculty.name}: {student.first_name} {student.last_name}")

        elif faculty_choice == "sbf":
            # Check if a student belongs to a faculty
            email = input("Enter student's email: ")
            faculty = self.find_faculty_by_email(email)

            if faculty:
                print(f"Student with email {email} belongs to {faculty.name} ({faculty.abbreviation})")
            else:
                print("Student not found in any faculty.")

    def general_operations(self):
        print("\nGeneral Operations:")
        print("cf. Create a new faculty")
        print("wf. Search what faculty a student belongs to by email")
        print("uf. Display University faculties")
        print("allf. Display all faculties belonging to a field")
        general_choice = input("Enter your choice: ")

        if general_choice == "cf":
            # Create a new faculty
            name = input("Enter faculty name: ")
            abbreviation = input("Enter faculty abbreviation: ")
            print("Available Study Fields:")
            for field in StudyField:
                print(f"{field.value}. {field.name}")
            field_value = int(input("Select the study field (enter the number): "))

            study_field = StudyField(field_value)
            faculty = Faculty(name, abbreviation, study_field)
            self.faculties.append(faculty)
            print(f"Faculty {faculty.name} created and added to the University.")

        elif general_choice == "wf":
            # Search what faculty a student belongs to by email
            email = input("Enter student's email: ")
            faculty = self.find_faculty_by_email(email)

            if faculty:
                print(f"Student with email {email} belongs to {faculty.name} ({faculty.abbreviation})")
            else:
                print("Student not found in any faculty.")

        elif general_choice == "uf":
            # Display University faculties
            print("University Faculties:")
            for faculty in self.faculties:
                print(f"- {faculty.name} ({faculty.abbreviation})")

        elif general_choice == "allf":
            # Display all faculties belonging to a field
            for field in StudyField:
                print(f"{field.value}. {field.name}")
            field_value = int(input("Select the study field (enter the number): "))
            field = StudyField(field_value)

            matching_faculties = [faculty for faculty in self.faculties if faculty.study_field == field]
            if matching_faculties:
                print(f"Faculties belonging to {field.name}:")
                for faculty in matching_faculties:
                    print(f"- {faculty.name} ({faculty.abbreviation})")
            else:
                print(f"No faculties found for the selected ({field.name}).")

    def run(self):
        while True:
            print("\nTUM Board Operations:")
            print("fo. Faculty Operations")
            print("go. General Operations")
            print("e. Exit")
            choice = input("Enter your choice: ")

            if choice == "fo":
                self.faculty_operations()
            elif choice == "go":
                self.general_operations()
            elif choice == "e":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    board = TUMBoard()
    board.run()
