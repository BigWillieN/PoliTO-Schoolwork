from random import randint
def main():
    i = 0
    seq = []
    while i < 20:
        seq.append(randint(0,99))
        i += 1
    print(seq)
    seq_new = sorted(seq)
    print(seq_new)

main()
