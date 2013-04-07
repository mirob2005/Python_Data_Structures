from adjList import AdjList

if __name__ == '__main__':
    
    print('Undirected Graph:')
    undirected = AdjList(False)
    for vertex in ['r','s','t','u','v','w','x','y']:
        undirected.addVertex(vertex)
    for source,dest in [('r','s'),('r','v'),('s','w'),('w','t'),('w','x'),('t','x'),('t','u'),('x','u'),('x','y'),('u','y')]:
        undirected.addEdge(source,dest)
    
    print(undirected)
    print('BFS:\n%s'%undirected.traverseBFS('s'))
    print('DFS:%s\n'%undirected.traverseDFS())
    
    print('\nTesting Copy Undirected:')
    copy = undirected.copyGraph()
    print(copy)
    print('BFS:\n%s'%copy.traverseBFS('s'))
    print('\nDFS:%s\n'%copy.traverseDFS())
    
    print('\nAfter Delete Vertex r:')
    undirected.removeVertex('r')
    print(undirected)
    print('BFS:\n%s'%undirected.traverseBFS('s'))
    print('\nDFS:%s\n'%undirected.traverseDFS())    
    
    print('\nAfter Delete Edge x->u:')
    undirected.removeEdge('x','u')
    print(undirected)
    print('BFS:\n%s'%undirected.traverseBFS('s'))
    print('\nDFS:%s\n'%undirected.traverseDFS())
    
    print('Shortest Path v->y: %s'%undirected.shortestPath('v','y'))
    print('Shortest Path s->y: %s'%undirected.shortestPath('s','y'))
    undirected.removeEdge('x','y')
    
    print('Shortest Path s->y after delete edge x->y: %s'%undirected.shortestPath('s','y'))
    
    print('Graph is a DAG: %s'%undirected.isDAG())
    
    print('\nUnchanged Copy:\n%s'%copy)
    copy.removeVertex('w')
    print('Removing vertex w:\n%s'%copy)
    print('BFS:\n%s'%copy.traverseBFS('s'))
    print('\nDFS:%s\n'%copy.traverseDFS())    
    
    print('\nOriginal Graph:\n%s'%undirected)
