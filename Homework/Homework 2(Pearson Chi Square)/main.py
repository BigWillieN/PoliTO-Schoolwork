
import random
def main():
#This function is written to see if the hypothetical die is fair or not.
     roll = int(input("Enter how many times you want to roll your die: "))
     count= 0
     results = []
     while (count< roll):
         dice_value = random.randint(1,6)
         results.append(dice_value)
         count = count+1
     x = results.count(1)
     y = results.count(2)
     z = results.count(3)
     d = results.count(4)
     e = results.count(5)
     f = results.count(6)
     chisquared = ((x-(roll/6))**2)/(roll/6) + ((y-(roll/6))**2)/(roll/6) + ((z-(roll/6))**2)/(roll/6) + ((d-(roll/6))**2)/(roll/6) + ((e-(roll/6))**2)/(roll/6) + ((f-(roll/6))**2)/(roll/6)
     if chisquared <= 11.07:
        print("Dice is fair.")
     else:
        print("Dice isn't fair.")
     print(chisquared)
     print(x, y, z, d, e, f)
main()
