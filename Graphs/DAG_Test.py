from adjList import AdjList

if __name__ == '__main__':

    print('DAG:')
    dag = AdjList(True)
    for vertex in ['r','s','t','u','v','w','x','y']:
        dag.addVertex(vertex)
    for source,dest in [('r','s'),('r','v'),('s','w'),('w','t'),('w','x'),('t','x'),('t','u'),('x','u'),('x','y'),('u','y')]:
        dag.addEdge(source,dest)
    
    print(dag)
    print('BFS:\n%s'%dag.traverseBFS('s'))
    print('\nDFS: %s'%dag.traverseDFS())
    
    print('Topological Sort: %s'%dag.topologicalSort())
    transpose = dag.computeTranspose()
    print('\nTranspose of dag:\n%s'%transpose)
    print('Strongly Connected Components: %s\n'%dag.stronglyConnectedComponents())
    
    print('\nTesting Copy:\n')
    copy = dag.copyGraph()
    print(copy)
    print('BFS:\n%s'%copy.traverseBFS('s'))
    print('\nDFS:%s\n'%copy.traverseDFS())
    print('Graph is a DAG: %s\n'%copy.isDAG())
    
    print('Copy Graph after removing vertex "v"')
    copy.removeVertex('v')
    print(copy)
    print('DFS:%s\n'%copy.traverseDFS())
    
    print('Compared to original graph:')
    print(dag)
    
    print('After Delete Vertex r:')
    dag.removeVertex('r')
    
    print(dag)
    print('BFS:\n%s'%dag.traverseBFS('s'))
    print('\nDFS:%s\n'%dag.traverseDFS())
    
    print('\nAfter Delete Edge x->u:')
    dag.removeEdge('x','u')
    
    print(dag)
    print('BFS:\n%s'%dag.traverseBFS('s'))
    print('\nDFS:%s\n'%dag.traverseDFS())
    
    print('Shortest Path v->y: %s'%dag.shortestPath('v','y'))
    print('Shortest Path s->y: %s'%dag.shortestPath('s','y'))
    dag.removeEdge('x','y')
    print('Shortest Path s-> y after delete edge x->y: %s'%dag.shortestPath('s','y'))
    
    print('\nGraph is a DAG: %s'%dag.isDAG())
    
    print('\nCopy:\n%s'%copy)
