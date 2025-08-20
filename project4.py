student_grade={ } 
#dictionary

def add_student(name,grade):
    student_grade[name]=grade
    print(f"{name} with a {grade}")
    print(f"{name} updated with a {grade}")

def update_student(name,grade):
    if name in student_grade:
        student_grade[name]=grade
        print(f"{name} added with a {grade}")
    else:
        print(f"{name} entered is not present")
def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f"{name} has been deleted ")
    else:
        print(f"{name} entered is not present")
def view_student():
    if student_grade:
        for name,grade in student_grade.items():
            print(f"{name}:{grade}")
    else:
        print("No student found")
while True:
        print("1.Add student\n2.update student\n3.Delete student\n4.View Student\n5.Exit")
        stu_del=int(input("Enter the choice="))
        if stu_del==1:
            name=input("Enter the name of the student:")
            grade=int(input("Enter the marks of the student:"))
            add_student(name,grade)
        elif stu_del==2:
            name=input("Enter the name of the student:")
            grade=int(input("Enter the marks of the student:"))
            update_student(name,grade)
        elif stu_del==3:
            name=input("Enter the name of the student:")
            grade=int(input("Enter the marks of the student:"))
            delete_student(name)
        elif stu_del==4:
            view_student()
        elif stu_del==5:
            print("End of the program")
             
        else:
            print("Over")
        