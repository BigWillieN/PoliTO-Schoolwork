#first we need to make main function to put our inputs and outputs
def main():
   initial_List = []
   user_Input = input("Enter your number, press Q to quit. ")
   while user_Input != "Q":
       initial_List.append(int(user_Input))
       user_Input = input("Enter your number, press Q to quit. ")
   if magic_Square(initial_List) is True:
       print("Your square is a magic square.")
   else:
       print("Your square is NOT a magic square.")
def magic_Square(x):
#now we need to make our first elimination to save some time. I thought making an ideal list and comparing it to our de facto list would be the optimal situation
   if sorted(x) == [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]:
#for the next step we will find and list the rows and columns and diagonals with a mathematical method
        first_row = []
        second_row = []
        third_row = []
        fourth_row = []
        first_column = []
        second_column = []
        third_column = []
        fourth_column = []
        first_diagonal = []
        second_diagonal = [x[3],x[6],x[9],x[12]]
        for i in range(0, (len(x))):
           if i // 4 == 0:
               first_row.append(int(x[i]))
           if i // 4 == 1:
               second_row.append(int(x[i]))
           if i // 4 == 2:
               third_row.append(int(x[i]))
           if i // 4 == 3:
               fourth_row.append(int(x[i]))
           if i % 4 == 0:
               first_column.append(int(x[i]))
           if i % 4 == 1:
               second_column.append(int(x[i]))
           if i % 4 == 2:
               third_column.append(int(x[i]))
           if i % 4 == 3:
               fourth_column.append(int(x[i]))
           if i % 5 == 0:
               first_diagonal.append(int(x[i]))
#now I intend to put the sums into a final list and if every item in the list is equal, then we conclude that our nunmbers are a magic square
        final_List = [sum(first_diagonal),sum(first_column),sum(first_row), sum(second_diagonal), sum(second_column), sum(second_row), sum(third_column), sum(third_row), sum(fourth_row), sum(fourth_column)]
        if final_List[0] == final_List[-1]:
               return True
        else:
               return False



main()