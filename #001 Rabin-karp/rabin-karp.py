base = 27
prime = 10e9 + 7  # well known choice of prime in competitive programming


def main():
    n = int(input())
    while n:
        pattern = input()
        word = input()
        pattern_hash = compute_hash(pattern)
        word_hash = compute_hash(word[:len(pattern)])  # calculate the first window of the word

        power = 1
        for i in range(len(pattern)):
            power = (power * base) % prime

        found = False
        for i in range(len(word) - len(pattern) + 1):
            if word_hash == pattern_hash:
                print("Match found in position %5s" % i)
                found = True
                break
            if i + len(pattern) < len(word):
                word_hash = ((word_hash * base) + ord(word[i + len(pattern)])) % prime  # add trailing char
                word_hash -= power * ord(word[i]) % prime # remove leading char
                if word_hash < 0:
                    word_hash += prime
        if not found:
            print("No match found")
        n -= 1


def compute_hash(pattern):
    hash = 0
    for i in range(len(pattern)):
        hash = (hash * base) + ord(pattern[i]) % prime
    return hash


if __name__ == '__main__':
    main()
