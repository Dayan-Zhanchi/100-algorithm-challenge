# Quicksort
[Quicksort](https://en.wikipedia.org/wiki/Quicksort) is a divide and conquer algorithm, that naturally divides the problem into sub problems, solves each subproblem the same way and and puts them
 together into one solution. It's one of the faster sorting algorithms running in average on O(n\*logn), but with worst case on O(n^2), worse than [merge sort](https://en.wikipedia.org/wiki/Merge_sort). 
 It's similiar to merge sort but it uses a pivot element that is an element of the array when dividing the elements in the array. There are 2 popular variants of quicksort, lomuto and
  hoare partition scheme. I chose to implement the latter scheme. In both schemes elements are grouped into left and right of the pivot. All elements
  less than the value of the pivot goes to the left and all elements greater than the pivot goes to the right.
  
  The biggest difference between Hoare and Lomuto is in how they implement the logic for dividing the elements to the left and right of the pivot. The choice of the pivot and the scheme impacts
   performance for special cases such as sorted arrays and repeated elements, with Hoare performing better than Lomuto at each case. However, Lomuto is easier to implement and understand.
  
  #### Lomuto 
  Lomuto moves all the elements that is lower than the pivot to the left, starting from 0 up until there are no elements left less than pivot (it checks all the elements). You can think of it as
   though it builds a new subarray within the array from position 0 that only contains elements lower than the pivot. Then the rest of the elements will naturally be greater than the pivot and
    positioned to the right of the pivot. At the end however it has to put the pivot right after the last element that was less than the pivot by switching with whichever element that was greater
     than the pivot. Repeat this process until the entire array is sorted.
 #### Hoare
 Hoare keeps track of 2 variables, a low and high index, that grow in opposite directions before stopping (low variable incrementing and high decrementing). The low only increments whenever an
  element is less than the pivot and high only decrements for elements greater than the pivot. When they find an element that doesn't fulfill this condition, then they swap both the elements to
   their opposite positions, that is low elements -> high element and high element -> low element. At the end when low is greater than or equal to high then stop the iteration and repeat this whole
    procedure to the subarrays, until the entire list is sorted.
 
 ![Quicksort visualization](Quicksort-example.gif)