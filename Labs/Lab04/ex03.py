def ex03_main():
    leng = int(input("Side lenght: "))
    for i in range(leng):
        print("*" * leng)
    for z in range(leng):
        print(" "* (leng-z), "*" * (2*z-1))
    for y in range(leng, 0, -1):
        print(" "* (leng-y), "*" * (2*y-1))
ex03_main()
