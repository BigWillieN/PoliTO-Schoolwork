def ex06_main():
    str1 = str(input("Enter string:"))
    for c in range(1, len(str1)+1):
        for post in range(0, len(str1)-c+1):
            print(str1[post:post+c])
