def financial_aid(income,children):

    benefit = 0
    if 30000 <= income <= 40000:
        if 3 >= children:
            benefit = 1000*children
        else:
            print("You are not fitted for financial aid.")
    elif 20000 <= income < 30000:
        if 2 >= children:
            benefit = 1500*children
        else:
            print("You are not fitted for financial aid.")
    elif income < 20000:
        benefit = 2000*children
    else:
        print("You are not fitted for financial aid.")
    return benefit

def main():
    income = int(input("What is your income: "))
    children = int(input("Number of children: "))
    zzrot = financial_aid(income,children)
    print(f"Your financial aid is: {zzrot}")

main()
