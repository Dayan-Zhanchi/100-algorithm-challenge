import random

def main():
    n = 10
    elements_to_be_shuffled = [i for i in range(n)]
    print(fisher_yates_shuffle(elements_to_be_shuffled))


def fisher_yates_shuffle(elements_to_be_shuffled):
    for i in range(len(elements_to_be_shuffled) - 1, 0, -1):
        j = random.randint(0, i)
        tmp = elements_to_be_shuffled[j]
        elements_to_be_shuffled[j] = elements_to_be_shuffled[i]
        elements_to_be_shuffled[i] = tmp
    return elements_to_be_shuffled

if __name__ == '__main__':
    main()