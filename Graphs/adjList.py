#Michael Robertson
#mirob2005@gmail.com
#Completed: 4/--/2013

# Implements an Adjacency List

from ADTs.Queue_head import Queue

class Vertex:
    def __init__(self,name):
        self.name = name
        self.next = []
        self.visit = None
        self.dist = float('inf')
        self.predecessor = None
    def __str__(self):
        if not self.next:
            string = 'Vertex %s has no outgoing edges.\n'%self.name
        else:
            string = 'Vertex %s has edges to: '%self.name
            for vertex in self.next:
                string += ('%s, '%vertex.name)
            string = string.rstrip(', ') + '\n'
        return string
    
class AdjList:
    def __init__(self, directed=False):
        self.directed = directed
        self.vertexList = {}

    def __str__(self):
        string = ''
        for key, value in self.vertexList.items():
            string += str(value)
        if not string:
            string = '(Empty)'
        return string

    def __contains__(self,vertex):
        for vert in self.vertexList.keys():
            if vert == vertex:
                return True
        return False
    
    def __iter__(self):
        return iter(self.vertexList.keys())
    
    def addVertex(self,vertex):
        if vertex in self:
            print('Vertex %s already exists!'%vertex)
            return False
        self.vertexList[vertex] = Vertex(vertex)
        #print('Added vertex %s to the graph'%vertex)
        return True
        
    def addEdge(self,vertexFrom,vertexTo):
        if vertexFrom not in self:
            print('Vertex %s does not exist!'%vertexFrom)
            return False
        if vertexTo not in self:
            print('Vertex %s does not exist!'%vertexTo)
            return False
        if self.directed:
            self.vertexList[vertexFrom].next.append(self.vertexList[vertexTo])
            #print('Added directed edge from %s to %s'%(vertexFrom,vertexTo))
        else:
            self.vertexList[vertexFrom].next.append(self.vertexList[vertexTo])
            self.vertexList[vertexTo].next.append(self.vertexList[vertexFrom])
            #print('Added undirected edge from %s to %s'%(vertexFrom,vertexTo))
        return True
        
    def removeVertex(self,vertex):
        if vertex not in self:
            print('Vertex %s does not exist!'%vertex)
            return False
        removed = self.vertexList.pop(vertex)
        for key, vertex in self.vertexList.items():
            if removed in vertex.next:
                vertex.next.remove(removed)
        return True
    
    def removeEdge(self,vertexFrom,vertexTo):
        if vertexFrom not in self:
            print('Vertex %s does not exist!'%vertexFrom)
            return False
        if vertexTo not in self:
            print('Vertex %s does not exist!'%vertexTo)
            return False
        if self.directed:
            self.vertexList[vertexFrom].next.remove(self.vertexList[vertexTo])
        else:
            self.vertexList[vertexFrom].next.remove(self.vertexList[vertexTo])
            self.vertexList[vertexTo].next.remove(self.vertexList[vertexFrom])
        return True
    
    def traverseBFS(self,source):
        pass
    
    def traverseDFS(self):
        pass
    
    def shortestPath(self):
        pass
    
    def isDAG(self):
        pass
    
if __name__ == '__main__':
    print('DAG:')
    dag = AdjList(True)
    for vertex in ['r','s','t','u','v','w','x','y']:
        dag.addVertex(vertex)
    for source,dest in [('r','s'),('r','v'),('s','w'),('w','t'),('w','x'),('t','x'),('t','u'),('x','u'),('x','y'),('u','y')]:
        dag.addEdge(source,dest)
    
    print(dag)
    
    print('After Delete Vertex:')
    dag.removeVertex('r')
    print(dag)

    print('After Delete Edge:')
    dag.removeEdge('x','u')
    print(dag)
    
    print('Undirected Graph:')
    undirected = AdjList(False)
    for vertex in ['r','s','t','u','v','w','x','y']:
        undirected.addVertex(vertex)
    for source,dest in [('r','s'),('r','v'),('s','w'),('w','t'),('w','x'),('t','x'),('t','u'),('x','u'),('x','y'),('u','y')]:
        undirected.addEdge(source,dest)
    
    print(undirected)
    
    print('After Delete Vertex:')
    undirected.removeVertex('r')
    print(undirected)
    
    print('After Delete Edge:')
    undirected.removeEdge('x','u')
    print(undirected)