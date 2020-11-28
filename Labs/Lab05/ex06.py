def ex06_main():
    french_name = input("Enter the french name of your country: ")
    vowel = ["A", "E", "I", "O", "U"]
    exceptions = ["Belize" ,"Cambodge" ,"Zimbabwe" ,"Zaïre", "Mozambique","Mexique"]

    if "-" in french_name:
        print(f"les {french_name}")
    elif french_name[0] in vowel:
        print(f"l'{french_name}")
    elif french_name in exceptions:
        print(f"le {french_name}")
    elif french_name[-1] == "e" :
        print(f"la {french_name}")
    else:
        print(f"le {french_name}")



ex06_main()
