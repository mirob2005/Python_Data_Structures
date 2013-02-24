Python Data Structures
======================
*ADTS:*
- Queue with head and tail ptr, insert new at head, remove old at tail
- Queue with only head ptr, remove old at head, append new to the end
- Stack (push/pop at head)

*Linked List Operations:*
- insert
- append
- returnIndex
- updateIndex
- deleteIndex
- insertBeforeIndex
- insertAfterIndex
- deleteData
- deleteAllData
- insertAfterEveryData
- insertBeforeEveryData
- deleteList
- copyList
- findMthToLastNode

*Types:*
- Single LL with head pointer
- Double LL with head pointer
- Circular LL with head & tail pointers

Unit Tests to test all 3 types and each operation

*Binary Search Tree Operations:*
- insert
- insertList
- find
- delete
- traverseBFS
- traverseDFSpreorder
- traverseDFSinorder
- traverseDFSpostorder
- copyTree
- findMin
- findMax

*Types:*
- Iterative (uses Queue(head ptr) and Stack for traversals)
- Recursive (inherits from iterative approach, reimplements insert,find,delete,DFS,findMin,findMax)

Unit Tests to test each operation for both types

*Binary Heap Operations:*
- traverseBFS
- insert (with heapifyUp to ensure heap property)
- insertList
- delete (with heapifyDown to ensure heap property)

Units Tests to  test each operation and to ensure proper tracking
of next insert/delete location to ensure shape property

*TODO:*
- Priority Queue using Binary Heap
- Tries
- Hash Table
- Self-balancing BST - Red-Black Tree, Splay Tree, AVL Tree
- Graphs (various types), impl. objects/ptrs, adjacency L/M, incidence L/M
- Sorting - merge sort, quicksort

