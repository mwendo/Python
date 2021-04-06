students = []
numbStudents = input("How many students do you have?")

for i in range(int(numbStudents)):

    # Name
    name = input("Students name: ")
    while (name == ""):
        print("Invalid name, try again.....")
        name = input("Students name: ")
    students.append(name)

    # Grade
    grade = input("Students grade: ")
    while (grade == ""):
        print("Invalid grade, try again.....")
        grade = input("Students grade: ")
    students.append(grade)

    # Class
    course_selection = input(
        "Select a courese: 1 - Math, 2 - Science, 3 - History: ")
    while (course_selection < "1" or course_selection > "3" or course_selection == ""):
        print("Invalid course, try again.....")
        course_selection = input(
            "Select a courese: 1 - Math, 2 - Science, 3 - History: ")
    if (course_selection == "1"):
        students.append("Math")
    elif (course_selection == "2"):
        students.append("Science")
    elif (course_selection == "3"):
        students.append("History")


print(students)