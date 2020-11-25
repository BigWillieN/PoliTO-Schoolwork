"Exercise 3.1"

def ex1():
#This function reads three integers and tells if they are in increasing order or decreasing order or neither"

#Input:
    x = input("X:")
    y = input("Y:")
    z = input("Z:")
#Output:
    if x>y>z:
        print("Decreasing Order")
    elif z>y>x :
        print("Increasing Order")
    else:
        print("Neither")
