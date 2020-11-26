list1 = []
def ex01_main():
#A program that reads a sequence of integer inputs and prints several of its values
   num= int(input("Enter number of elements in list: "))
   for i in range(0, num):
       x = int(input("Enter elements: "))
       list1.append(x)
   print(f"The smallest is {ex01_min(list1)} and the largest is {ex01_max(list1)}")
   print(f"Number of even numbers is {ex01_even(list1)} and the number of odd numbers is {ex01_odd(list1)}")
   print(f"The cumulative totals are {ex01_cum(list1)}")

def ex01_min(list1):
   return min(list1)

def ex01_max(list1):
   return max(list1)

def ex01_even(list1):
   count = 0
   for x in list1:
      if x % 2 == 0:
         count = count+1
   return count

def ex01_odd(list1):
   count = 0
   for x in list1:
      if x % 2 != 0:
         count = count+1
   return count

def ex01_cum(list1):
   new = []
   x = 0
   for element in list1:
      x += element
      new.append(x)
   return new
