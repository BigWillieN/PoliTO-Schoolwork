 from random import randint
def main():
   list1 = []
    i = 0
    number = int(input("How many numbers do u want in ur list: "))
    while i < number:
        list1.append(randint(0,50))
        i += 1
    list1.sort()
    print(list1)
    j =sumWithoutSmallest(list1) - list1[0]
    print(j)

def sumWithoutSmallest(a):
  a = 0
  for i in range(0,len(a)-1):
    a += incoming_list[i+1]
  return a


main()
