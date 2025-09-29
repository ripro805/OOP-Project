class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)
        
    @classmethod
    def get_student_by_id(cls, student_id):
        for student in cls.student_list:
            if student._student_id == student_id: 
                return student
        return None


class Student:
    def __init__(self, student_id, name, department, is_enrolled=False):
        self._student_id = student_id
        self._name = name
        self._department = department
        self._is_enrolled = is_enrolled
        StudentDatabase.add_student(self)

    def enroll_student(self):
        if self._is_enrolled:
            print(f"Student {self._student_id} is already enrolled.")
        else:
            self._is_enrolled = True
            print(f"Student {self._student_id} enrolled successfully.")

    def drop_student(self):
        if not self._is_enrolled:
            print(f"Student {self._student_id} is not enrolled.")
        else:
            self._is_enrolled = False
            print(f"Student {self._student_id} dropped successfully.")

    def view_student_info(self):
        status = "Enrolled" if self._is_enrolled else "Not Enrolled"
        print(f"ID: {self._student_id}, Name: {self._name}, "
              f"Department: {self._department}, Status: {status}")


def menu():
    while True:
        print("\n===== Student Database Menu =====")
        print("1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            if not StudentDatabase.student_list:
                print("No students available.")
            else:
                for s in StudentDatabase.student_list:
                    s.view_student_info()

        elif choice == "2":
            sid = input("Enter Student ID to enroll: ")
            student = StudentDatabase.get_student_by_id(sid)
            if student:
                student.enroll_student()
            else:
                print("Invalid Student ID.")

        elif choice == "3":
            sid = input("Enter Student ID to drop: ")
            student = StudentDatabase.get_student_by_id(sid)
            if student:
                student.drop_student()
            else:
                print("Invalid Student ID.")

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


s1 = Student("101", "Alice", "CSE")
s2 = Student("102", "Bob", "EEE", True)
s3 = Student("103", "Charlie", "BBA")

menu()
