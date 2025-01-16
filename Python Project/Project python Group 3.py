from tkinter import *

#1
print("Welcome to Humber")


#2
def checkpassword(x):

    
    if len(x) < 10:
        print("Incorrect, should contain at least 10 letter")
        return False
    if not any(char.isupper() for char in x):
        print('Password should have at leats one uppercase letter')
        return False
    if not any(char.isdigit() for char in x):
        print('Password should contain two or three numbers ')
        return False
    special_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?/'
    if not any(char in special_chars for char in x):
        print("Password should contain at least 1 special chars")
        return False
    return True
        
       
def password1(max_attempts=3):
    attemps = 0
    while attemps < max_attempts:
        enter_password= input("Please enter your password: ")
        if checkpassword(enter_password):
            print("Correct Password")
            return True
        else:
            print("Invalid password. Please try again")
        attemps += 1

password1()

credit_hours = {"Math": 4, "Science": 5, "Language": 4, "Drama": 3, "Music": 2, "Biology": 4}

#Step 3: Enter Number of Students

def student_count(max_attempts=3):
    attempts = [0]
    student_number = [None]

    def validate_input():
        number = numberField.get().strip()
        if number.isdigit() and 1 <= int(number) <= 50:
            student_number[0] = int(number)
            studentNumber.destroy()
        else:
            attempts[0] += 1
            if attempts[0] >= max_attempts:
                studentNumber.destroy()

    studentNumber = Tk()
    studentNumber.title("Enter Number of Student")
    studentNumber.geometry("250x150")

    Label(studentNumber, text="Enter Number of Student (1-50):").pack(pady=5)
    numberField = Entry(studentNumber, width=30)
    numberField.pack(pady=5)

    error_label = Label(studentNumber, text="", fg="red")
    error_label.pack()

    Button(studentNumber, text="Submit", command=validate_input).pack(pady=10)

    studentNumber.mainloop()
    return student_number[0]

student_number = student_count()

print('Number of students: '+ str(student_number)) 

#Step 4: Enter Student Names

def student_names(student_number):

    students = {} 
    name_fields = [] 
    
    studentNames = Tk()
    studentNames.title('Input Student Names')

    
    max_students_per_column = 10
    column = 0

    for j in range(student_number):

        
        row = (j%max_students_per_column)*2
        
        vert = 120*(row%11)
        hori = 200*((student_number//10)+1)
        studentNames.geometry(f"{hori}x{vert}")

        namesLabel = Label(studentNames, text='Enter name for student ' + str(j + 1) + ": ")
        namesLabel.grid(row=row, column=column, padx=5, pady=5)

        namesField = Entry(studentNames,width=30)
        namesField.grid(row=row+1, column=column, padx=5, pady=5)
        name_fields.append(namesField)

        if (j+1)%max_students_per_column == 0:
            column += 1

    def Names():
        for i in range(student_number):
            name = name_fields[i].get().strip()
            if name:
                students[name] = {}
            
        studentNames.destroy()

    button_names = Button(studentNames, width=20, text='Input', command=Names)
    button_names.grid(row=student_number*2, column=0,padx=5, pady=10)

    studentNames.mainloop()
    return students

students = student_names(student_number)
print(students) #

#Step 5: Enter Grades

def enter_grades(current_student):

    if current_student >= len(students):
        return

    student_name = list(students.keys())[current_student]

    studentsGrade = Tk()
    studentsGrade.title('Enter grades for Students')
    studentsGrade.geometry('310x270')

    gradeTitleLabel = Label(studentsGrade, text='Enter grades for '+(student_name))
    gradeTitleLabel.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

    subjects = list(credit_hours.keys())
    fields = {}
    row = 1

    for subject in subjects:
        label = Label(studentsGrade, text=(subject)+' (0-100): ')
        label.grid(row=row, column=0, padx=5, pady=5)
        entry_field = Entry(studentsGrade, width=20)
        entry_field.grid(row=row, column=1, padx=5, pady=5)
        fields[subject] = entry_field
        row += 1

    def submit_grades():
        for subject, field in fields.items():
            grade_input = field.get().strip()
            if grade_input.isdigit() and 0 <= int(grade_input) <= 100:
                students[student_name][subject] = int(grade_input)
            else:
                students[student_name][subject] = 'Invalid'
        studentsGrade.destroy()
        enter_grades(current_student + 1)

    button_submit = Button(studentsGrade, width=20, text='Submit', command=submit_grades)
    button_submit.grid(row=row, column=0, padx=5, pady=10, columnspan=2)

    studentsGrade.mainloop()

#Start entering grades for the first student
enter_grades(0)

print(students) #For test Library

def calculate_gpa(students):
    student_gpa = {}
    for student, grades in students.items():
        total_weighted_score = 0
        total_credit_hours = 0
        for subject, grade in grades.items():
            if str(grade).isdigit() and 0 <= int(grade) <= 100:
                grade = int(grade)
                total_weighted_score += grade * credit_hours[subject]
                total_credit_hours += credit_hours[subject]

        if total_credit_hours > 0:
            gpa = total_weighted_score / total_credit_hours
        else:
            gpa = 0
        student_gpa[student] = round(gpa, 2)
    return student_gpa

def assign_schools(student_gpa):
    student_schools = {}
    for student, gpa in student_gpa.items():
        if 90 <= gpa <= 100:
            student_schools[student] = "School of Engineering"
        elif 80 <= gpa < 90:
            student_schools[student] = "School of Business"
        elif 70 <= gpa < 80:
            student_schools[student] = "Law School"
        else:
            student_schools[student] = "Not accepted"
    return student_schools

def report(student_schools, student_gpa):
    schools = ["School of Engineering", "School of Business", "Law School"]
    number_students = {sch: 0 for sch in schools}
    total_number_students_accepted = 0

    for sch in student_schools.values():
        if sch in schools:
            number_students[sch] += 1
            total_number_students_accepted += 1

    total_number_not_accepted = sum(1 for x in student_schools.values() if x == "Not accepted")

    if len(student_gpa) > 0:
        avg_gpa = sum(student_gpa.values()) / len(student_gpa)
    else:
        avg_gpa = 0

    #Report 1
    with open("Report1.txt", "w") as file:
        file.write(" Report 1: Student and their assigned school \n")
        for student, school in student_schools.items():
            file.write(f"{student}: {school}\n")
            
    #Report 2
    with open("Report2.txt", "w") as file:
        file.write(" Report 2: Accepted students \n")    
        file.write(f"Total Accepted students: {total_number_students_accepted} \n")
        for sch in schools:
            file.write(f"{sch}: {number_students[sch]}\n") 
            
    #Report 3
    with open("Report3.txt", "w") as file:
        file.write(" Report 3: Number of students not accepted \n")
        file.write(f"Not accepted: {total_number_not_accepted} \n")
            
    #Report 4
    with open("Report4.txt", "w") as file:
        file.write(" Report 4: Average GPA of the students \n")
        file.write(f"Average GPA: {avg_gpa:.2f} \n")

student_gpa = calculate_gpa(students)  
student_schools = assign_schools(student_gpa) 
report(student_schools, student_gpa)  

print(student_gpa) #Check gpa
print(student_schools) #Check schools
