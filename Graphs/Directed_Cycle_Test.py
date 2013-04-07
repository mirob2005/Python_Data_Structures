from adjList import AdjList
    
if __name__ == '__main__':
    
    print('Directed Cycle:')
    cycle = AdjList(True)
    for vertex in ['r','s','t','u']:
        cycle.addVertex(vertex)
    for source,dest in [('r','s'),('s','t'),('t','r'),('t','u')]:
        cycle.addEdge(source,dest)
        
    print(cycle)
    print('BFS:\n%s'%cycle.traverseBFS('s'))
    print('\nDFS: %s'%cycle.traverseDFS())
    
    print('Topological Sort: %s'%cycle.topologicalSort())
    print('Strongly Connected Components: %s\n'%cycle.stronglyConnectedComponents())
    