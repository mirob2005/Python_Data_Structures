Python Data Structures
======================
### Lorem_ipsum.txt included for testing and timing purposes.
### Currently used to test Tries and Hash Table

## *ADTS:*
- Queue with head and tail ptr, insert new at head, remove old at tail
- Queue with only head ptr, remove old at head, append new to the end
- Stack (push/pop at head)
- Priority Queue (uses an array-based Binary Heap)

## *Linked List Operations:*
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

### *Types:*
- Single LL with head pointer
- Double LL with head pointer
- Circular LL with head & tail pointers

Unit Tests to test all 3 types and each operation

## *Binary Search Tree Operations:*
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

### *Types:*
- Iterative (uses Queue(head ptr) and Stack for traversals)
- Recursive (inherits from iterative approach, reimplements insert,find,delete,DFS,findMin,findMax)

Unit Tests to test each operation for both types

## *AVL Tree Operations:*
- insert (Balance Factor Calculations added)
- delete (Balance Factor Calculations added)
- deleteTree (new, none of the other trees has this added at this time)
- checkBalance (check the Balance Factor to see if a rotation(s) is necessary)
- calcBF (recalculate the BF for the the given root and all ancestors if necessary, insert version and delete version)
- rotateLeft
- rotateRight

- All redefined operations are recursive.

### *Rest of the operations are inherited from the recursive BST*

Unit Tests to test each operation and valid rotations.

## *Red-Black Tree Operations:*
- insert (Color Check added)
- delete (Color Check added)
- deleteTree (Same as AVL)
- checkColor (determines the new coloring and if any rotations are needed - version for post-insert and post-delete)
- rotateLeft (Same as AVL)
- rotateRight (Same as AVL)

- All redefined operations are recursive.

### *Rest of the operations are inherited from the recursive BST*

Unit Tests to test each operation, valid rotations and correct coloring.

## *Splay Tree Operations:*
- insert (splaying added)
- find (splaying added for valid/invalid finds)
- delete (splaying added for valid/invalid deletes)
- copyTree (redefined due to the structure of the splay tree varying based off order of inserts)
- findRecentAccessed (returns the root, only useful for a splay tree)
- splay (rotates the tree so that the most recent inserted/found node or parent of a recent delete is rotated to the root)

- All redefined operations are recursive.

### *Rest of the operations are inherited from the recursive BST*

Unit Tests to test each operation and valid splaying.

## *Binary Heap Operations:*
- traverseBFS
- insert (with heapifyUp to ensure heap property)
- insertList
- delete (with heapifyDown to ensure heap property)
- merge (2 heaps -> 1 heap)
- peek (get max value)
- copyHeap

### *Types:*
- Tree Structure (uses ptrs)
- Array Structure (no ptrs needed)

Units Tests to test each operation and to ensure proper tracking
of next insert/delete location to ensure shape property

## *Trie Operations:*
- traverse(Words|Prefixes) - Outputs words for generic type or all prefixes for prefix count versions
- traverseBFS
- add
- remove
- isMember (full words or prefixes specifically added)
- updateValue (Generic type only)
- getValue

### *Types:*
- Generic - allows adding words with a corresponding value, all prefix node values are None
- Prefix Count - user only adds words, values correspond to number of times that prefix is used
- Prefix Count Speed - Same as above, but using more space to allow for faster indexing

Unit tests to test each operation for all 3 types

## *Sorting:*
### Selection Sorts:
- HeapSort - uses an array-based binary heap, in-place sort, not stable,
    O(n) best case, O(n log n) AVG/worst case performance, O(1) auxiliary space

### Merge Sorts:
- MergeSort - not in place, stable sort, O(n log n) best/AVG/worst case performance,
    O(n) auxiliary space

### Exchange Sorts:
- QuickSort - not in place, not stable, O(n log n) best/AVG, O(n^2) worst case
    performance, O(n) auxiliary space, fastest on average

Tested using language provided sort method to compare the result on a random.shuffle() list

## *Hash Table Operations:*
- add
- updateValue
- delete
- lookUp
- hash

### *Types:*
- Separate Chaining Collision resolution

Unit tests to test each operation

## *Graphs:*

<table>
  <tr>
    <th>Type</th><th>Storage</th><th>Add Vertex</th><th>Add Edge</th><th>Remove Vertex</th><th>Remove Edge</th><th>Query</th>
  </tr>
  <tr>
    <td>Adjacency List</td><td>O(|V|+|E|)</td><td>O(1)</td><td>O(1)</td><td>O(|E|)</td><td>O(|E|)</td><td>O(|V|)</td>
  </tr>
  <tr>
    <td>Adjacency Matrix</td><td>O(|V|^2)</td><td>O(|V|^2)</td><td>O(1)</td><td>O(|V|^2)</td><td>O(1)</td><td>O(1)</td>
  </tr>
  <tr>
    <td>Incidence List</td><td>O(|V|+|E|)</td><td>O(1)</td><td>O(1)</td><td>O(|E|)</td><td>O(|E|)</td><td>O(|E|)</td>
  </tr>
  <tr>
    <td>Incidence Matrix</td><td>O(|V|*|E|)</td><td>O(|V|*|E|)</td><td>O(|V|*|E|)</td><td>O(|V|*|E|)</td><td>O(|V|*|E|)</td><td>O(|E|)</td>
  </tr>
</table>

### *Adjacency List:*
- Vertices are stored in a dictionary. Each vertex has a list of neighboring vertices.
- Supports direct and undirected graphs.

*Operations:*
- addVertex
- addEdge
- removeVertex
- removeEdge
- copyGraph

*Algorithm:*
*Breadth First Search*
- traverseBFS
- shortestPath

*Depth First Search*
- DAG test
- traverseDFS
- topological sort
- find strongly connnected components
- compute tranpose - used to find strongly connnected components
- Classification of edges into: 
1)Tree Edges 
2)Back Edges 
3)Forward/Cross Edges

### *Adjacency Matrix:*
- Matrix is V rows and V columns. If a vertex V1 is adjacent to vertex V2, then the V1 row and V2 column entry in the matrix will be True or carry a weight (if weighted graph) else False or infinite weight. 
- If the graph is undirected the matrix will equal it's own transpose

*Operations:*
- addVertex
- addEdge
- removeVertex
- removeEdge

*Algorithm:*
*Breadth First Search*
- traverseBFS
- shortestPath

*Depth First Search*
- traverseDFS
- Classification of edges into: 
1)Tree Edges 
2)Back Edges 
3)Forward/Cross Edges

### *Incidence List:*
- Not Implemented

### *Incidence Matrix:*
- Not Implemented

