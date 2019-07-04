# Misra-Gries summary
[Misra-Gries summary](https://en.wikipedia.org/wiki/Misra%E2%80%93Gries_summary) is a streaming algorithm and
can be seen as a generalization of the [Boyer-Moore majority vote](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm) case. Instead of 
only looking for a majority that is 1 element that appears > m/2 times, Misra-Gries looks for some k elements that appear >
m/(k+1) times. For the rest of the j elements, that don't appear more than m/(k+1) times the output for those can
be any number in the list.