from random import randint
def main():
    list1 = []
    i = 0
    number = int(input("How many numbers do u want in ur list: "))
    while i < number:
        list1.append(randint(0,50))
        i += 1
    print(list1)
    print(reverser(list1))

def reverser(a):
    new_list = a[::-1]
    return new_list
main()
