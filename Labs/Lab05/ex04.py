def ex04_main():

    a = 32310901
    b = 1729
    m = 2**24
    count = 1
    r_old = int(input("What is your seed?: "))
    while count <= 100:
        count += 1
        r_new = (a*r_old+b)%m
        print(r_new)
        r_old = r_new

ex04_main()
