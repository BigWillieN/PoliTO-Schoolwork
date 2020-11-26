def ex04_main():
    word = str(input("Write your name: "))
    for i in range(len(word)-1, -1, -1):
        print(word[i], end="")


