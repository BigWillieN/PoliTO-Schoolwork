def find(string, match):
    exo = False
    if match in string:
        exo = True
    return exo

b = find("Mississippi", "sip")
print(b)
