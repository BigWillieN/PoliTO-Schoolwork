from random import randint

def main():
    counter = int(input("How many numbers do you want to generate: "))
    count = 0
    intlist = []
    while count < counter:
        intlist.append(randint(0,50))
        count += 1
    print(alternate(intlist))
    print(intlist)

def alternate(intlist):
    positives = intlist[::2]
    negatives = intlist[1::2]
    result = sum(positives)- sum(negatives)
    return result
main()
