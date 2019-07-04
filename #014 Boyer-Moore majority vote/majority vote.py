def main():
    a = [2, 9, 9, 9, 7, 6, 4, 9, 9, 9, 3, 9]
    b = [10, 1, 2, 1, 1, 5, 1, 5, 5]
    c = [10, 5, 2, 1, 1, 5, 1, 5, 1]
    print("Input: %s, majority: %s" % (a, bm_maj_vote(a)))
    print("Input: %s, majority: %s" % (b, bm_maj_vote(b)))
    print("Input: %s, majority: %s" % (c, bm_maj_vote(c)))


def bm_maj_vote(a):
    counter = 0
    id = -1
    for e in a:
        if counter == 0:
            id = e
            counter = 1
        elif e == id:
            counter += 1
        else:
            counter -= 1

    # second pass to determine whether m is really majority
    if a.count(id) > int(len(a)/2):
        return id
    return None

main()
