def ex07_main():
    rem = 100
    buyers = 0
    while rem >= 0:
       tic = int(input("How many tickets do you want to buy?"))
       if tic <= 4:
           rem = rem - tic
           print(f"Remaining tickets: {rem}")
           buyers += 1
       else:
           print("No more than four tickets can be bought")
           continue
    print(f"Number of total buyers: {buyers}")
ex07_main()
