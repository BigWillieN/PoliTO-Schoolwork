def ex03():
    #This function reads a string and displays some of its values
#Input
    str1 = str(input("Enter your string"))
#Processing and Output
    if str1[-1] == ".":
        print("Your string ends with a period")
    if str1[0].isupper():
        print("Your string starts with a capital letter")
    if str1.islower():
        print("Your string contains only lowercase letters")
    if str1.isupper():
        print("Your string contains only uppercase letters")
    if str1.isdigit():
        print("Your string contains only digits")
    if str1.isalpha():
        print("Your string contains only letters")
