"""
CRUD application in Python
Cognifyz internship Advanced Level->Task 5
Objective: Implement file storage for tasks
to enable saving and loading from a text file.


text file name : studentData.txt 
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
        with open("studentData.txt","a") as studentData:
            studentData.write(str(student))
        
    def read(self):
        
        with open("studentData.txt","r") as studentData:
            data = studentData.read()
            if not data:
                print("No Student Data found")
            else:
                print(data)
       
    def update(self, rollnumber, name=None, addr=None, gpa=None):
        updated = False
        with open("studentData.txt", "r") as f:
            data = f.readlines()

        with open("studentData.txt", "w") as f:
            for line in data:
                
                if f"Roll Number: {rollnumber}" in line:
                    student_data = line.strip().split(", ")
                    
                    # Parse existing data
                    student_name = student_data[0].split(": ")[1]
                    student_rollNumber = student_data[1].split(": ")[1]
                    student_address = student_data[2].split(": ")[1]
                    student_gpa = student_data[3].split(": ")[1]
                    
                    # Update with new data if provided
                    if name:
                        student_name = name
                    if addr:
                        student_address = addr
                    if gpa:
                        student_gpa = gpa
                    
                    # Create updated student line
                    updated_student = f"Name: {student_name}, Roll Number: {student_rollNumber}, Address: {student_address}, GPA: {student_gpa}\n"
                    f.write(updated_student)
                    updated = True
                    print(f"Updated: {updated_student.strip()}")
                else:
                    f.write(line)  

        if not updated:
            print(f"Student with Roll Number {rollnumber} not found.")
    
    def delete(self, rollNumber):
    # Flag to check if a student was deleted
        deleted = False

       
        with open("studentData.txt", "r") as f:
            data = f.readlines()

       
        with open("studentData.txt", "w") as f:
            for line in data:
                
                if f"Roll Number: {rollNumber}" in line:
                    deleted = True
                    print(f"Deleted: {line.strip()}")
                    continue  
                f.write(line)  

        if not deleted:
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
