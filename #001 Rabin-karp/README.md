Link to the algorithm:https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm

A good hash function is important and thus picking good primes and bases is essential 
to reduce the probability of hash collisions. Since this particular implementation doesn't manually 
check for string equality between the pattern and the given word when the hash are equal, then it might
return wrong answers upon hash collisions.

Not sure but the probability of hash collision is perhaps 1 − (1 − 1/B)^n, where n is the length of the
string and B is the prime chosen for the modulus operation.

Rabin-karp builds on the idea of rolling hash, where we have a window of length as the pattern and we slide
the window one step forward for each iteration, by adding the upcoming trailing character and removing
the previous character.
