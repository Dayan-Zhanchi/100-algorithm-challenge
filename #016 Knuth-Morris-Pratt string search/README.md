# Knuth-Morris-Pratt string searching
[Knuth-Morris-Pratt](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm) also known as KMP is a string searching
algorithm that given a pattern finds whether it exists in a given word. It's more efficient than a naive brute force solution where you would 
compare each letter of the word with each letter of the pattern, making it a O(N * M) time complexity, where N is the length of the word and M length of the pattern. With KMP the time
complexity reduces down to O(N+M), by precomputing a table that stores for each index the longest proper suffix that is also a proper prefix of the pattern at the index.
The table is then used as a fast checkup of how much to backtrack in the pattern when encountering a partial match between the word and the pattern. 

A good video explaining this process was made by [Tushar Roy](https://www.youtube.com/watch?v=GTJr8OvyEVQ), which is also the process
my implementation follows, rather than the one explained in wiki.



