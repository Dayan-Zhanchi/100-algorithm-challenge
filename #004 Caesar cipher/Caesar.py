import sys

def caesar(c, shift):
    for i in range(len(c)):
        if c[i] >= 'A' and c[i] <= 'Z':
            c[i] = chr(((ord(c[i])-65+shift) % 26) + 65)
        elif c[i] >= 'a' and c[i] <= 'z':
            c[i] = chr(((ord(c[i])-97+shift) % 26) + 97)
    return c

def main():
    c = list(sys.argv[1])
    shift = int(sys.argv[2])
    print("".join(caesar(c,shift)))

if __name__ == "__main__":
    main()