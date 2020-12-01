def countVowels(examp):
    vowels = ["a","e","i","o","u"]
    count = 0
    for i in examp:
        if i.lower() in vowels:
            count += 1
    print(f"Number of vowels : {count}")





