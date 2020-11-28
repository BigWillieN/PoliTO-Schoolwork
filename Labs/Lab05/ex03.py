def ex03_main():
    integ = int(input("Enter your integer: "))
    i = 2
    while integ >1:
        if integ%i == 0:
            integ = integ/i
            print(i)
        else:
            i = i+1
ex03_main()
