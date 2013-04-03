# *Graphs:*

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

## *Adjacency List:*

## *Adjacency Matrix:*
- Matrix is V rows and V columns. If a vertex V1 is adjacent to vertex V2, then the V1 row and V2 column entry in the matrix will be True or carry a weight (if weighted graph) else False or infinite weight. 
- If the graph is undirected the matrix will equal it's own transpose

## *Incidence List:*

## *Incidence Matrix:*

## *Operations:*
- addVertex
- addEdge
- removeVertex
- removeEdge

## *Algorithm:*
### *Breadth First Search*
- traverseBFS
- shortestPath

### *Depth First Search*
- traverseDFS
- Classification of edges into: 1)Tree Edges 2)Back Edges 3)Forward/Cross Edges
