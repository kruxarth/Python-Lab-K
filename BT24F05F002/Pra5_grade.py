# This program takes a student's marks as input and generates a grade.
# practical 5: Grade Generation
def grade_generate(mark):
    if (mark >= 90):
        print("You got A grade")
    elif (mark >= 80):
        print("You got B grade")
    elif (mark >= 70):
        print("You got C grade")
    elif (mark >= 60):
        print("You got D grade")
    elif (mark >= 33):
        print("You got E grade")
    else:
        print("You got F grade \nyou are FAIL")

mark = float(input("enter the marks (0 to 100): "))
grade_generate(mark)
