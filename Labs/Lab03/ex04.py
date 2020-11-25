def ex04():
 #The following algorithm identifies the season (Spring, Summer, Fall or Winter) to which a date belongs, given the month and day.

#Input
    month = int(input("Numerical value of the month:"))
    day = int(input("Numerical value of the day:"))
    season = " "
 #Processing
    if 1<= month <=3 :
        season = "Winter"
    elif 4<= month <=6:
        season = "Spring"
    elif 7<= month <=9:
        season = "Summer"
    elif 10<= month <=12:
        season = "Fall"
    else:
        print("Invalid Month")
    if month % 3 == 0:
        if day >= 21:
            if season == "Winter":
                season = "Spring"
            elif season == "Spring":
                season = "Summer"
            elif season == "Summer":
                season = "Fall"
            else:
                season = "Winter"
        elif day > 30:
             print("Invalid day")
#Output
    print(f"Your season is {season}")


