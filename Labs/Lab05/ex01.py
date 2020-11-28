def ex01_main():
    list = []
    ex1 = []
    while list != ".":
       ex1 = input("Enter a string:")
       if ex1 != ".":
          list.append(ex1)
       else:
           break
    sorted_list = sorted(list)
    print(sorted_list)


ex01_main()

