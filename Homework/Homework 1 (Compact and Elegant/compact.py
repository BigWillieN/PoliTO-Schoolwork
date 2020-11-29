from random import randint
def calculator():
    number = int(input("How many numbers:"))
    scores = []
    for i in range(number):
      scores.append(randint(1, 30))
    print(f"Original scores: {scores}, removing lowest: {sorted(scores[1:])}  average: {(sum(sorted(scores[1:])))/(len(sorted(scores[1:])))}")
