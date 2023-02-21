# Courses input and display
courseSum = int(input("Input the number of courses: "))
courseDict = {}

def courseFill(int):
    for i in range(courseSum):
        id = str(input("Type the course id: "))
        name = str(input("Type the course name: "))
        courseDict[i] = [id, name]

def displayCourse(int):
    for i in range(courseSum):
        print(courseDict[i])

courseFill(courseSum)
displayCourse(courseSum)

# Student input and display
studentSum = int(input("Input the numbers of students: "))
studentDict = {}

def studentFill(int):
    for i in range(studentSum):
        id = str(input("Type the student id: "))
        name = str(input("Type the student name: "))
        DoB =  str(input("Type the date of birth: "))
        # Giving marks
        for i in range(courseSum):
            temp = i + 1
            print("For the " + str(temp) +" course")
            mark = str(input("Type the mark: "))
            studentDict[i] = [id, name, DoB, mark]

def displayStudent(int):
    for i in range(studentSum):
        print(studentDict[i])

studentFill(studentSum)
displayStudent(studentSum)


