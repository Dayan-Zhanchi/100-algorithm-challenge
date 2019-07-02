import random

def main():
    n = 1000
    k = 10
    sample = [i for i in range(n)]
    print(reservoir_sampling(sample, k))


def reservoir_sampling(s, k):
    res = [0] * k
    for i in range(k):
        res[i] = s[i]

    for i in range(k+1, len(s)):
        j = random.randint(1, i)
        if j <= k:
            res[j-1] = s[i]
        if (i+1) % 100 == 0:
            print(res)

if __name__ == '__main__':
    main()