# Misra-Gries summary
[Misra-Gries summary](https://en.wikipedia.org/wiki/Misra%E2%80%93Gries_summary) is a streaming algorithm and
can be seen as a generalization of the [Boyer-Moore majority vote](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm) case. Instead of 
only looking for a majority that is 1 element that appears > m/2 times, Misra-Gries looks for some k elements that appear >
m/(k+1) times. If there are less than k elements, say j elements, that appear > m/(k+1) times then the output for the k - j elements can be any number in the data stream. However, I make a second pass to extract only the elements that appear > m/(k+1) times.

**Note that the pseudocode in the wikipage for the bound in the second branch, |Keys(A)| < k - 1, is incorrect, because there can be at most k keys.
In other words, there can be at most k elements that appear > m/(k+1) and the logic for the second branch is to add one such new potential key if the current element is not a key already, which means that there must be a space for such key to be added, thus it should be |Keys(A)| <= k-1 check instead of < k-1.**
