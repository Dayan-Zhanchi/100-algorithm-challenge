import mmh3
from bitarray import bitarray
import numpy as np


class Bloom:

    # n - number of elements in bloom filter
    def __init__(self, n, acceptable_false_rate):
        self.size = int(round(-n * np.log(1 / acceptable_false_rate) / (np.log(2) ** 2)))  # m - number of bits needed for n elements
        self.number_of_hash_functions = int(round((self.size / n) * np.log(2)))  # number of hash functions needed
        self.bit_array = bitarray(self.size)

    def add(self, key):
        hashes = self.__bloom_hash(key)
        for h in hashes:
            self.bit_array[h] = True

    def query(self, key):
        hashes = self.__bloom_hash(key)
        found = True
        for h in hashes:
            if self.bit_array[h] == 0:
                found = False
                break
        return found

    def __bloom_hash(self, key):
        h1 = mmh3.hash(key)
        h2 = mmh3.hash(str(h1))

        hashes = []
        for i in range(self.number_of_hash_functions):
            hashes.append((h1 + (i * h2)) % self.size)

        return hashes
