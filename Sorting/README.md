# *Sorting:*
## Selection Sorts:
### HeapSort:
- uses an array-based binary heap
- in-place sort, not stable
- O(n) best case, O(n log n) AVG/worst case performance
- O(1) auxiliary space

### Selection Sort:
- stable, in-place
- O(n^2) best/AVG/worst case performance
- O(1) auxiliary space

## Merge Sorts:
### MergeSort:
- not in place, stable sort
- O(n log n) best/AVG/worst case performance
- O(n) auxiliary space

## Exchange Sorts:
### QuickSort:
- not in place, not stable
- O(n log n) best/AVG, O(n^2) worst case performance
- O(n) auxiliary space
- fastest on average

### BubbleSort:
- stable, in-place
- O(n^2) - worst/AVG case, O(n) - best case (already sorted list)
- O(1) auxilary - worst case space complexity

## Insertion Sorts:
### Insertion Sort:
- stable, in-place
- O(n^2) - worst/AVG case, O(n) - best case (already sorted list)
- O(1) auxilary - worst case space complexity

All tested using language provided sort method to compare the result on a random.shuffle() list
