k = 2


def main():
    a = [10, 5, 2, 1, 1, 5, 1, 5, 1, 5, 1]
    b = [10, 5, 2, 1, 1, 5, 1, 4, 1, 3, 1]

    print("Input: %s, output: %s" % (a, misra_gries(a)))
    print("Input: %s, output: %s" % (b, misra_gries(b)))


def misra_gries(data):
    a = dict()

    for e in data:
        if e in a.keys():
            a[e] += 1
        elif len(a.keys()) <= k - 1:
            a[e] = 1
        else:
            for key in list(a.keys())[:]:
                a[key] -= 1
                if a[key] == 0:
                    a.pop(key)
    freq_items = []
    for key in a.keys():
        if data.count(key) > int(len(data) / (k + 1)):
            freq_items.append(key)
    return freq_items

main()