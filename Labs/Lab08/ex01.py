def main():
    list1 = [1,4,9,16]
    list2 = [9,7,4,9,11]
    result = merge(list1,list2)
    print(result)

def merge(a,b):
    newlist= []
    if len(a) >= len(b):
        for i in range(0, len(b)):
            newlist.append(a[i])
            newlist.append(b[i])
        for j in range(len(b), len(a)):
            newlist.append(a[j])
    else:
        for i in range(0, len(a)):
            newlist.append(a[i])
            newlist.append(b[i])
        for j in range(len(a), len(b)):
            newlist.append(b[j])
    return newlist

main()