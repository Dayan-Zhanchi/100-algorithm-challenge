import bloom as b

def main():
    n = 6
    p = 100
    words = ['asdksadksjad', 'hej', 'sakldjsaidjlösadjksajdksajkdsajsalkdkdjskdjkasdjklsakdlskad', 'trolol', 'heja', 'hejj']
    test_words= ['sakldjsaidjlösadjksajdksajkdsajsalkdkdjskdjkasdjklsakdlskad', 'dyu', 'hejjj', 'hejaa', 'lol', ' trolol', 'hej ']
    bloom_filter = b.Bloom(n, p)
    print("Number of bits: %s" % bloom_filter.size)
    print("Number of hash functions: %s" % bloom_filter.number_of_hash_functions)
    [bloom_filter.add(word) for word in words]
    test_for_true_cases(bloom_filter, words)
    arbitrary_tests(bloom_filter, test_words)


def arbitrary_tests(bloom_filter, test_words):
    [print("%s: %s" % (word, bloom_filter.query(word))) for word in test_words]


def test_for_true_cases(bloom_filter, words):
    [print(bloom_filter.query(word)) for word in words]


if __name__ == '__main__':
    main()

