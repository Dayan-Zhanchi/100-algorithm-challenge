import sys

def luhn(input):
    sum = 0
    for i in range(len(input)):
        digit = ord(input[i]) - ord('0')
        if (i % 2) != 0:
            digit = digit * 2
            if digit > 9:
                digit = digit - 9
        sum += digit
    return (sum % 10 == 0)

def main():
    input = list(sys.argv[1])
    valid = luhn(input)
    length = len(input)
    firstTwoDigits = int("".join(input[0:2]))

    if valid and length == 15 and ( firstTwoDigits == 37 or firstTwoDigits == 34):
        print("AMEX\n")
    
    elif valid and length == 16 and (firstTwoDigits >= 50 or firstTwoDigits <= 55):
        print("MASTERCARD\n")

    elif valid and (length == 16 or length == 13) and (int(input[0]) == 4):
        print("VISA\n")

    else:
        print("INVALID\n")

if __name__ == "__main__":
    main()