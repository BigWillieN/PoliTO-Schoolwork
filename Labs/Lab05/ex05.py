def ex05_main():
    ini_prey = int(input("Initial prey population: "))
    ini_pred = int(input("Initial predator population: "))
    B = float(input("Rate of predation: "))
    A = float(input("Rate of birth exceeding natural death: "))
    C = float(input("Rate of predator death exceeding birth without food: "))
    D = float(input("Predator increase in the presence of food: "))
    year = int(input("Period of years that has passed: "))
    count = 1
    while count <= year:
        new_prey = ini_prey*(1+A-B*ini_pred)
        new_pred = ini_pred*(1-C+D*ini_prey)
        print(f"Population of prey in year {count} is {new_prey}")
        print(f"Population of predators in year {count} is {new_pred}")
        ini_prey = new_prey
        ini_pred = new_pred
        count += 1
ex05_main()
