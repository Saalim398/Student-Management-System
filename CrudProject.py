"""
CRUD application in Python
Cognifyz internship Intermediate Level->Task 1
Objective: Implement Create, Read, Update, and
Delete operations using arrays or lists for data
storage.
"""

import time


# Splash screen for better look of application
def splash_screen():
    ss = ["W", "E", "L", "C", "O", "M", "E"]
    for s in ss:
        print(s, end="")
        time.sleep(0.1)


"""
Created a student class model having method parameters as studentName , rollNumber, address ,gpa
"""


class Student:
    def __init__(self, studentName, rollNumber, address, gpa):
        self.studentName = studentName
        self.rollNumber = rollNumber
        self.address = address
        self.gpa = gpa

    def __str__(self):
        return f"Name: {self.studentName}, Roll Number: {self.rollNumber}, Address: {self.address}, GPA: {self.gpa}"
    
        


"""

StudentCRUD class has 4 methods createStudent, read, update, delete
The StudentCRUD class is responsible for creating, reading, updating, and deleting Student objects. 
It holds a list of Student instances (self.students) and operates on them.
The Student class is focused on representing individual student data (like name, roll number, etc.).
The StudentCRUD class is focused on managing a collection of Student instances, 
providing functionality to manipulate this collection (CRUD operations).
"""


class StudentCRUD:
    def __init__(self):
        self.students = []  # student list to hold student data

    def createStudent(self, name, rollnumber, addr, gpa):
        student = Student(name, rollnumber, addr, gpa)
        self.students.append(student)

        print(f"{student}")
        
        
        
    def read(self):
        if not self.students:
            print("No students found.")
        else:
            for student in self.students:
                print(student)
            
     
        

    def update(self, rollnumber, name=None, addr=None, gpa=None):
        for student in self.students:
            if student.rollNumber == rollnumber:
                if name:
                    student.studentName = name
                if addr:
                    student.address = addr
                if gpa:
                    student.gpa = gpa
                print(f"Updated: {student}")
                return
        print(f"Student with Roll Number {rollnumber} not found.")

    def delete(self, rollNumber):
        for student in self.students:
            if student.rollNumber == rollNumber:
                self.students.remove(student)
                print(f"Deleted: {student}")
                return
        print(f"Student with Roll Number {rollNumber} not found.")


def main():
    scrud = StudentCRUD()

    while True:
        print("\nSelect\n1 to exit\n2 to create a new student\n3 to update an existing student\n4 to read student "
              "details\n5 to delete student\n")
        try:
            option = int(input("Enter option: "))
        except ValueError:
            print("User input is not an integer, Try Again")
            continue

        if option == 1:
            break
        elif option == 2:
            print("\n\t\t\t\tEnter student details\n")
            student_name = input("Enter Student name: ")
            try:
                student_rollNumber = int(input("Enter student roll number: "))
            except ValueError:
                print("User input is not an integer, Try again")
                continue
            student_address = input("Enter student address: ")
            try:
                student_GPA = float(input("Enter GPA: "))
            except ValueError:
                print("User input is not a valid GPA, Try again")
                continue

            scrud.createStudent(student_name, student_rollNumber, student_address, student_GPA)

        elif option == 3:
            try:
                student_rollNumber = int(input("\nEnter Student's roll number to update: "))
            except ValueError:
                print("User input is not an integer, Try again")
                continue

            student_name = input("Enter Student name: ")
            student_address = input("Enter student address: ")
            try:
                student_GPA = float(input("Enter GPA: "))
            except ValueError:
                print("User input is not a valid GPA, Try again")
                continue

            scrud.update(student_rollNumber, student_name, student_address, student_GPA)

        elif option == 4:
            print("Reading all students data")
            scrud.read()

        elif option == 5:
            try:
                deleteStudent = int(input("Enter student's Roll Number to delete: "))
            except ValueError:
                print("User input is not an integer, Try Again")
                continue
            scrud.delete(deleteStudent)
        else:
            print("Wrong input, Try Again")


if __name__ == '__main__':
    splash_screen()
    time.sleep(0.1)
    main()
