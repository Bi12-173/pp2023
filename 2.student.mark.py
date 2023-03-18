class Course:
    def __init__(self, cID, cName):
        self.cID = cID
        self.cName = cName

#Creating list
courseList = []

#Getting course in4
courseSum = int(input("Input the number of courses: "))
def courseFill(self):
    for i in range(courseSum):
        id = str(input("Type the course id: "))
        name = str(input("Type the course name: "))
        courseList.append(Course(id, name))

#Print course
def displayCourse(self):
    for i in range(courseSum):
        print(courseList[i].cID + ' | ' + courseList[i].cName)

courseFill(courseSum)
displayCourse(courseSum)

class Student:
    def __init__(self, sID, sName, DoB, ):
        self.sID = sID
        self.sName = sName
        self.DoB = DoB
        self.mark = mark

    def mark(self, *args):
        self.mark

#Getting student in4
studentSum = int(input("Input the numbers of students: "))
studentList = []

def studentFill(self):
    for i in range(studentSum):
        id = str(input("Type the student id: "))
        name = str(input("Type the student name: "))
        DoB =  str(input("Type the date of birth: "))
        studentList.append(Student(id, name, DoB))

def displayStudent(self):
    for i in range(studentSum):
        print(studentList[i].sID + ' | ' + studentList[i].sName + ' | ' + studentList[i].DoB)
        # Giving marks
        for i in range(courseSum):
            temp = i + 1
            print("For the " + str(temp) + "th course type the mark:")
            mark = str(input())
            print(courseList[i].cName + ': ' + mark)

studentFill(studentSum)
displayStudent(studentSum)