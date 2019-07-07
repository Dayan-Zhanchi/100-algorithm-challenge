def main():
    n = int(input())
    while n:
        word = input()
        pattern = input()
        starting_index_of_found_pattern = kmp(pattern, word)
        if starting_index_of_found_pattern != -1:
            print("Found: %s at index %s" % (pattern, starting_index_of_found_pattern))
        else:
            print("No pattern found")
        n -= 1


def kmp(pattern, word):
    table = construct_partial_match_table(pattern)
    i = 0
    j = 0
    while i < len(word) and j < len(pattern):
        if word[i] != pattern[j]:
            if j != 0:
                j = table[j - 1]
                continue
        if word[i] == pattern[j]:
            j += 1
        i += 1
    if j == len(pattern):
        return i - j
    return -1


def construct_partial_match_table(pattern):
    j = 0
    table = [0] * len(pattern)
    for i in range(1, len(pattern)):
        while pattern[i] != pattern[j]:
            if j != 0:
                j = table[j - 1]
            else:
                table[i] = 0
                break
        if pattern[i] == pattern[j]:
            table[i] = j + 1
            j += 1
    return table


if __name__ == '__main__':
    main()
