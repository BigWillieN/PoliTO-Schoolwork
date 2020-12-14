#Gives the neighbor index values of any 3x3 table (row, column) pair
def getNeighbors(row, column):
    neighbors = []
    #if method has not row and column parameters, we could evaluate row and column values by any index parameter supported.
    #row = indexParameterSupported//3
    #col = indexParameterSupported%3
    c1 = column - 1
    c2 = column
    c3 = column + 1
    r1 = row-1
    r2 = row
    r3 = row+1
    if c1 >= 0:
        if r1 >= 0 and ((c1 != column) or (r1 != row)):
            neighbors.append(3*r1+c1)
        if r2 >= 0 and ((c1 != column) or (r2 != row)):
            neighbors.append(3*r2+c1)
        if 3 > r3 >= 0 and ((c1 != column) or (r3 != row)):
            neighbors.append(3*r3+c1)
    if c2 >= 0:
        if r1 >= 0 and ((c2 != column) or (r1 != row)):
            neighbors.append(3*r1+c2)
        if r2 >= 0 and ((c2 != column) or (r2 != row)):
            neighbors.append(3*r2+c2)
        if 3> r3 >= 0 and ((c2 != column) or (r3 != row)):
            neighbors.append(3*r3+c2)
    if 3 > c3 >= 0:
        if r1 >= 0 and ((c3 != column) or (r1 != row)):
            neighbors.append(3*r1+c3)
        if r2 >= 0 and ((c3 != column) or (r2 != row)):
            neighbors.append(3*r2+c3)
        if 3 > r3 >= 0 and ((c3 != column) or (r3 != row)):
            neighbors.append(3*r3+c3)
    return sorted(neighbors)

def main():
    values = [0, 10, 20, 30, 40, 50, 60, 70, 80]
    average = 0
    sum = 0
    neighborIndexes = getNeighbors(0, 0)
    print(f"Neighbor Indexes: {neighborIndexes}")
    for i in neighborIndexes:
        sum += values[i]
    average = sum / len(neighborIndexes)
    print(f"Average: {average}")
