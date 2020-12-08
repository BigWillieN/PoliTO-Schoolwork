from random import randint

def main():
    count = 0
    intlist = []
    while count < 11:
        intlist.append(randint(-1000,1000))
        count += 1
    print(inde(intlist))
    print(reverse(intlist))
    print(first_last(intlist))

def inde(intlist):
    newlist = []
    for i in intlist:
        if i % 2 == 0:
            newlist.append(i)
    return newlist




def reverse(intlist):
    newlist = intlist[::-1]
    return newlist


def first_last(intlist):
    newlist = []
    newlist.append(intlist[0])
    newlist.append(intlist[-1])
    return newlist

main()
