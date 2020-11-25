"Exercise 3.2"

def ex2():
#This function translates letter grade into numerical grade

#Input
    grade = input("Enter your letter grade:")
#Processing
    if grade.upper() == "F":
        number = 0.0
    elif grade.upper() == "D-":
        number = 0.7
    elif grade.upper() == "D+":
        number = 1.3
    elif grade.upper() == "C-":
        number = 1.7
    elif grade.upper() == "C+":
        number = 2.3
    elif grade.upper() == "B-":
        number = 2.7
    elif grade.upper() == "B+":
        number = 3.3
    elif grade.upper() == "A-":
        number = 3.7
    elif grade.upper() == "A+":
        number = 4
#Output
    print(f"Your letter grade is: {grade}, your numerical grade is: {number}")
