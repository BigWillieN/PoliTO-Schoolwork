def ex02_main():
#Write programs that read a line of input as a string and print
   str1 = input("Enter your string: ")
   print(f"Only the uppercase letters: {ex02_upper(str1)}")
   print(f"Every seccond letter: {ex02_dub(str1)}")
   print(f"All vowels replaced by _ {ex02_undersc(str1)}")
   print(f"The number of digit in the string: {ex02_dig(str1)}")
   print(f"The position of all vowels in string: {ex02_vow(str1)}")


def ex02_upper(str1):
    list1 = []
    for i in str1:
        if  i>= "A" and i <= "Z":
            list1.append(i)
    return list1

def ex02_dub(str1):
    return str1[1::2]

def ex02_undersc(str1):
    vowels  = ["a", "e", "i", "o", "u"]
    low = str1.lower()
    for x in low:
        if x in vowels:
            low = low.replace(x, "_")
    return low

def ex02_dig(str1):
    count = 0
    for i in str1:
        if i.isdigit() == True:
            count = count +1
    return count

def ex02_vow(str1):
    vowels  = ["a", "e", "i", "o", "u"]
    positions = []
    low = str1.lower()
    for i, l in enumerate(low):
        if l in vowels:
            positions.append(i)
    return positions




ex02_main()
