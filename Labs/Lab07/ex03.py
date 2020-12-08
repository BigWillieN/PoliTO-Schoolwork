def main():
    a = []
    xer = input("Enter a prompt to list a:")
    while xer != "":
      a.append(xer)
      xer = input("Enter a prompt to list a:")
    b = []
    zor = input("Enter a prompt to list b:")
    while zor != "":
      b.append(zor)
      zor = input("Enter a prompt to list b:")
    print(equals(a,b))

def equals(a,b):
    if b == a:
        return True
    else:
        return False

main()

