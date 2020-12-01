def interest_machine(balance,interest,year):
    count = 0
    new_balance = []
    while count<year:
        new_balance = interest*balance
        balance = new_balance
        count += 1
    return new_balance



def main():
    balance = int(input("What is your initial balance: "))
    interest = float(input("What is the interest rate: "))
    year = int(input("How many years: "))
    zzrot = interest_machine(balance,interest,year)
    print(f"Your expected balance is {zzrot}")

main()
