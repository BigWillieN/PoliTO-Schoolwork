def countWords(examp):
    count = 1
    for i in examp:
        if i == " ":
            count += 1
    print(f"Number of words : {count}")
