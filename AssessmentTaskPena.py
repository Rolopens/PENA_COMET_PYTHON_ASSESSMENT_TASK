class Student:
    def __init__ (self, name, ID):
        self.name = name
        self.ID = ID
        self.courses = []

    def edit(self, newName):
        self.name = newName

    def addCourse(self, courseAdded):    
        self.courses.append(courseAdded)

    

class Course:
    def __init__(self, courseCode, unit, grade):
        self.courseCode = courseCode
        self.unit = unit
        self.grade = grade

    def editCourse(self, newCName, newUnit):
        self.courseCode = newCName
        self.unit = newUnit

        


def studentsMenu():
    terminate1 = 0
    while(terminate1 == 0):
        print("Student Menu")
        print("1 - Add Student")
        print("2 - Edit Info")
        print("3 - Delete Student")
        print("0 - Return to main Menu")
        choice1 = int(input("Input Choice: "))
        print("\n")

        if(choice1 == 0):
            terminate1 = 1
            
        elif(choice1 == 1):
            isLongEnough = 0
            studentName = input("Enter Name: ")
            while(isLongEnough == 0):
                studentID = int(input("Enter ID: "))
                if(studentID >= 10000000 and studentID <= 99999999):
                    isLongEnough = 1
                else:
                    print("Invalid Input! Re-Enter ID!!")
            for x in range (0, len(listOfStudents)):
                if (listOfStudents[x].ID == studentID):
                    x = 0
                    studentID = int(input("Invalid ID number! Re-Enter ID: "))
            listOfStudents.append(Student(studentName, studentID))
            print("Succesfully added " + studentName + " !!\n")
            
        elif(choice1 == 2):
            found = 0
            studentID = int(input("Enter ID to edit student name: "))
            for x in range(0, len(listOfStudents)):
                if (listOfStudents[x].ID == studentID):
                    found = 1
                    studentName = input("Enter new name: \n")
                    listOfStudents[x].name = studentName

            if (found != 1):
                print("No such student was found\n")
                
        elif(choice1 == 3):
            studentID = int(input("Enter ID to delete student: "))
            found = 0
            for x in range(0, len(listOfStudents)):
                if (listOfStudents[x].ID == studentID):
                    found = 1
                    print("Student " + listOfStudents[x].name +" has been deleted\n")
                    listOfStudents.remove(listOfStudents[x])

            if (found != 1):
                print("No such student was found\n")

        ###testing purpose choice
        elif(choice1 == 4):
            for i in range(0, len(listOfStudents)):
                print(listOfStudents[i].name +"\n")
                
           

def courseMenu():
    terminate2 = 0
    while(terminate2 == 0):
        print("Course Menu")
        print("1 - Add Course")
        print("2 - Edit Course")
        print("3 - Delete Course")
        print("0 - Return to main Menu")
        choice2 = int(input("Input Choice: "))
        print("\n")

        if(choice2 == 0):
            terminate2 = 1
            
        elif(choice2 == 1):
            isLongEnough = 0
            while(isLongEnough == 0):
                courseName = input("Enter Course Code: ")
                if(len(courseName) == 7):
                    isLongEnough = 1
                else:
                    print("Name is too short or too long! Re-Enter Course Code!!\n")
                    
            for x in range (0, len(listOfCourses)):
                if (listOfCourses[x].courseCode == courseName):
                    x = 0
                    courseName = input("Invalid Course Code! Re-Enter Course Code: ")

                    
            courseUnit = float(input("Enter the unit of course: "))
            newCourse = Course(courseName, courseUnit, 0)
            listOfCourses.append(newCourse)
            print("Succesfully added " + courseName + " !!\n")
            
        elif(choice2 == 2):
            courseName = input("Enter Course Code you want to edit: ")
            found = 0
            for x in range(0, len(listOfCourses)):
                if (listOfCourses[x].courseCode == courseName):
                    found = 1
                    courseUnit = float(input("Enter New unit of course: \n"))
                    listOfCourses[x].unit = courseUnit

            if (found != 1):
                print("No such Course was found\n")
            
        elif(choice2 == 3):
            courseName = input("Enter Course Code to delete desired course: ")
            found = 0
            for x in range(0, len(listOfCourses)):
                if (listOfCourses[x].courseCode == courseName):
                    found = 1
                    print("Student " + listOfCourses[x].courseCode +" has been deleted\n")
                    listOfCourses.remove(listOfCourses[x])

            if (found != 1):
                print("No such Course was found\n")
                             
        ###testing purpose choice
        elif(choice2 == 4):
            for i in range(0, len(listOfCourses)):
                print(listOfCourses[i].courseCode +"\n")
        
            
def enrollmentMenu():
    terminate3 = 0
    while(terminate3 == 0):
        print("Enrollment Menu")
        print("1 - Enroll a Student")
        print("2 - Drop a Student")
        print("3 - Set grades of a student")
        print("4 - View report card of a student")
        print("0 - Return to main menu")
        choice3 = int(input("Input Choice: "))
        print("\n")

        if(choice3 == 0):
            terminate3 = 1
            
        elif(choice3 == 1):
            ###enrolling a student in a course
            found = 0
            found1 = 0
            found2 = 0
            if(len(listOfCourses) != 0):
                studentID = int(input("Enter ID of Student that will be enrolled: "))
                print("\nList of Available Courses: ")
                for i in range(0, len(listOfCourses)):
                    print(listOfCourses[i].courseCode +"\n")
                    courseName = input("Enter name of desired course: ")
                    for x in range(0, len(listOfStudents)):
                        if (listOfStudents[x].ID == studentID):
                            found = 1
                            for i in range(0, len(listOfCourses)):
                                if(listOfCourses[i].courseCode == courseName):
                                    found1 = 1
                                    for j in range(0, len(listOfStudents[x].courses)):
                                        if (listOfStudents[x].courses[j].courseCode == courseName):
                                            found2 = 1
                                    if(found2!=1):
                                        print("Course "+ courseName+ " has been added\n")
                                        listOfStudents[x].addCourse(Course(listOfCourses[i].courseCode, listOfCourses[i].unit, listOfCourses[i].grade))
                                    else:
                                        print("Student already has this course\n")
                    if (found1 != 1):
                        print("Course was not found\n")
                if (found != 1):
                    print("Student was not found\n")
            else:
                print("Cannot enroll any students if there are no courses available!\n")

            print("\n")
            
        elif(choice3 == 2):
            ###dropping a course of a student
            found = 0
            found1 = 0
            found2 = 0
            if(len(listOfStudents) != 0):
                studentID = int(input("Enter ID of Student that will drop a course: "))
                for x in range(0, len(listOfStudents)):
                    if (listOfStudents[x].ID == studentID):
                        found = 1
                        if(len(listOfStudents[x].courses) != 0):
                            found2 = 1
                            print("\nList of Courses: ")
                            for i in range (0, len(listOfStudents[x].courses)):
                                print(listOfStudents[x].courses[i].courseCode)
                            dropCourse = input("Enter course you want to drop: ")
                            for i in range (0, len(listOfStudents[x].courses)):
                                if (listOfStudents[x].courses[i].courseCode == dropCourse):
                                    found1 = 1
                                    print("Course "+ listOfStudents[x].courses[i].courseCode +" has been dropped\n")
                                    listOfStudents[x].courses.remove(listOfStudents[x].courses[i])
                            if (found1 != 1):
                                print("Course entered is not being taken up by student\n")
                        if(found2 != 1):
                            print("Student has no courses to drop\n")   
                if(found != 1):
                    print("No student exists\n")  
            else:
                print("Cannot drop students from courses if there are no students\n")
            print("\n")
        elif(choice3 == 3):
            ###setting the grades of a student
            found = 0
            found1 = 0
            found2 = 0
            if(len(listOfStudents) != 0):
                studentID = int(input("Enter ID of Student that will have his/her grades fixed: "))
                for x in range(0, len(listOfStudents)):
                    if(listOfStudents[x].ID == studentID):
                        found = 1
                        if (len(listOfStudents[x].courses) != 0):
                            found1 = 1
                            for i in range(0, len(listOfStudents[x].courses)):
                                tempGrade = float(input("Enter Grade for the course " + listOfStudents[x].courses[i].courseCode+": "))
                                while (found2 == 0):
                                    if(tempGrade >=0 and tempGrade <=4):
                                        listOfStudents[x].courses[i].grade = tempGrade
                                        found2 = 1
                                    else:
                                        print("Invalid Grade! Input grade between 0 and 4")
                                        tempGrade = float(input("Enter Grade for the course " + listOfStudents[x].courses[i].courseCode+": "))
                        if (found1 != 1):
                            print("Studen is not enrolled on any courses\n")
                    if(found != 1):
                        print("No Student Exisits\n")
               
            else:
                print("There are no students in the database\n")
            print("\n")
        elif(choice3 == 4):
            ###checking of grades
            found = 0
            found1 = 0
            if(len(listOfStudents)!=0):
                studentID = int(input("Enter ID of Student to check grades: "))
                for x in range(0, len(listOfStudents)):
                    if(listOfStudents[x].ID == studentID):
                        found = 1
                        if (len(listOfStudents[x].courses) != 0):
                            found1 = 1
                            print("COURSE CODE / UNIT / GRADE")
                            for i in range(0, len(listOfStudents[x].courses)):
                                print("%s / %.2f / %.2f "%(listOfStudents[x].courses[i].courseCode, listOfStudents[x].courses[i].unit, listOfStudents[x].courses[i].grade))
                                ###print(listOfStudents[x].courses[i].courseCode + " / " +listOfStudents[x].courses[i].unit+" / "+listOfStudents[x].courses[i].grade)
                        if (found1 != 1):
                            print("Studen is not enrolled on any courses\n")
                    if(found != 1):
                        print("No Student Exisits\n")
            print("\n")         
listOfStudents = []
listOfCourses = []

print("=======Enrollment system=======\n")
terminate = 0
while(terminate == 0):
    print("Main Menu")
    print("1 - Student Menu")
    print("2 - Course Menu")
    print("3 - Enrollment")
    print("0 - Exit")
    choice = int(input("Input Choice: "))
    print("\n")
    
    if(choice == 0):
        terminate = 1
    elif(choice == 1):
        studentsMenu()
    elif(choice == 2):
        courseMenu()
    elif(choice == 3):
        enrollmentMenu()
    


'''
student1 = Student("Kyle", 11610573)
print(student1.ID)
'''
