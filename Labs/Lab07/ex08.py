from random import randint

def main():
   list1 = []
   i = 0
   while i < 10:
     list1.append(randint(0,50))
     i += 1
   print(list1)
   adjacent(list1)
   print(list1)

def adjacent(list1):
    for i in range(1,9):
        if list1[i] != (list1[i+1]+list1[i-1])/2:
            list1.pop(i)
    return list1
main()
