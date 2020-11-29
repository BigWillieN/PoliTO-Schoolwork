from random import randint


def main():
 #INPUT------------------------------------------------------

  number = int(input("Number of scores: "))

 #PROCESSING ------------------------------------------------

  scores = []
  for i in range(number):
      scores.append(randint(1, 30))
  lowest_removed = remove_lowest(scores)
  average_scores = average(scores)

  #OUTPUT ----------------------------------------------------

  print(f"Original scores: {scores}, removing lowest: {lowest_removed}, average: {average_scores}")

def remove_lowest(scores):
  _list = list(scores)
  _list.sort()
  _list.pop[0]
  return _list

def average(scores):

  return sum(scores)/len(scores)
