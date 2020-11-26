def ex05_main():
    number = int(input("Gib number: "))
    for i in range(0, number+1):
        if i>=2:
            for a in range(2, i):
                if (i%a== 0):
                    break
            else:
                print(i)
ex05_main()
