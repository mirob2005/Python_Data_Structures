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
        self.cycleExists = False

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
            if self.vertexList[vertexTo] in self.vertexList[vertexFrom].next:
                self.vertexList[vertexFrom].next.remove(self.vertexList[vertexTo])
            else:
                print('Edge %s to %s does not exist!'%(vertexFrom,vertexTo))
        else:
            if self.vertexList[vertexTo] in self.vertexList[vertexFrom].next:
                self.vertexList[vertexFrom].next.remove(self.vertexList[vertexTo])
                self.vertexList[vertexTo].next.remove(self.vertexList[vertexFrom])
            else:
                print('Edge %s to %s does not exist!'%(vertexFrom,vertexTo))
        return True
    
    def traverseBFS(self,source):
        path = ''
        for key, vertex in self.vertexList.items():
            vertex.visit = None
            vertex.dist = float('inf')
            vertex.predecessor = None
        self.vertexList[source].visit = False
        self.vertexList[source].dist = 0
        self.vertexList[source].predecessor = None
        bfsQ = Queue()
        bfsQ.enQueue(self.vertexList[source])
        curVertex = bfsQ.deQueue()
        while curVertex:
            for vertex in curVertex.next:
                if vertex.visit == None:
                    vertex.visit = False
                    vertex.dist = curVertex.dist+1
                    vertex.predecessor = curVertex
                    bfsQ.enQueue(vertex)
            curVertex.visit = True
            path+= ('Vertex %s, Distance: %s\n'%(curVertex.name,curVertex.dist))
            curVertex = bfsQ.deQueue()
        return path
    
    def traverseDFS(self):
        #Used to keep track if vertex is undiscovered(None), discovered(False),
        #   or fully explored (True)
        print('Edge Classifications:')
        string = ''
        for key, vertex in self.vertexList.items():
            vertex.visit = None
        for key, vertex in sorted(self.vertexList.items()):
            #If any undiscovered vertices remain, they become the new source
            if vertex.visit == None:
                string += self.DFS(vertex)
        return string
    
    def DFS(self,source):
        source.visit = False
        string = '(%s '%source.name
        for neighbor in source.next:
            if neighbor.visit == None:
                print('Edge %s to %s is a tree edge'%(source.name,neighbor.name))
                string += self.DFS(neighbor)
            elif neighbor.visit == False:
                self.cycleExists = True
                print('Edge %s to %s is a back edge'%(source.name,neighbor.name))
            else:
                print('Edge %s to %s is a forward/cross edge'%(source.name,neighbor.name))
        source.visit = True
        string += ' %s)'%source.name
        return string
    
    def shortestPath(self,source,dest):
        if not source in self:
            print('Vertex %s does not exist!'%source)
            return False
        if not dest in self:
            print('Vertex %s does not exist!'%dest)
            return False
        self.traverseBFS(source)
        return self.printPath(self.vertexList[source],self.vertexList[dest])
        
    def printPath(self,source,dest):
        path = ''
        if source == dest:
            path += source.name
        elif dest.predecessor == None:
            print('No path exists from %s to %s'%(source.name,dest.name))
            return None
        else:
            path += self.printPath(source,dest.predecessor)
            path += dest.name
        return path
    
    def isDAG(self):
        self.traverseDFS()
        return not self.cycleExists
    
    def copyGraph(self):
        pass
    
if __name__ == '__main__':
    print('DAG:')
    dag = AdjList(True)
    for vertex in ['r','s','t','u','v','w','x','y']:
        dag.addVertex(vertex)
    for source,dest in [('r','s'),('r','v'),('s','w'),('w','t'),('w','x'),('t','x'),('t','u'),('x','u'),('x','y'),('u','y')]:
        dag.addEdge(source,dest)
    
    print(dag)
    print('BFS:\n%s'%dag.traverseBFS('s'))
    print('\nDFS:\n%s'%dag.traverseDFS())
    
    print('After Delete Vertex r:')
    dag.removeVertex('r')

    print(dag)
    print('BFS:\n%s'%dag.traverseBFS('s'))
    print('\nDFS:\n%s'%dag.traverseDFS())

    print('After Delete Edge x->u:')
    dag.removeEdge('x','u')
    
    print(dag)
    print('BFS:\n%s'%dag.traverseBFS('s'))
    print('\nDFS:\n%s'%dag.traverseDFS())
    
    print('Shortest Path: %s'%dag.shortestPath('v','y'))
    print('Shortest Path: %s'%dag.shortestPath('s','y'))
    dag.removeEdge('x','y')
    print('Shortest Path after delete edge x->y: %s'%dag.shortestPath('s','y'))
    
    print('Graph is a DAG: %s'%dag.isDAG())
    
    print('__________________________\n')
    
    print('Undirected Graph:')
    undirected = AdjList(False)
    for vertex in ['r','s','t','u','v','w','x','y']:
        undirected.addVertex(vertex)
    for source,dest in [('r','s'),('r','v'),('s','w'),('w','t'),('w','x'),('t','x'),('t','u'),('x','u'),('x','y'),('u','y')]:
        undirected.addEdge(source,dest)
    
    print(undirected)
    print('BFS:\n%s'%undirected.traverseBFS('s'))
    print('\nDFS:\n%s'%undirected.traverseDFS())    
    
    print('After Delete Vertex r:')
    undirected.removeVertex('r')
    print(undirected)
    print('BFS:\n%s'%undirected.traverseBFS('s'))
    print('\nDFS:\n%s'%undirected.traverseDFS())    
    
    print('After Delete Edge x->u:')
    undirected.removeEdge('x','u')
    print(undirected)
    print('BFS:\n%s'%undirected.traverseBFS('s'))
    print('\nDFS:\n%s'%undirected.traverseDFS())
    
    print('Shortest Path: %s'%undirected.shortestPath('v','y'))
    print('Shortest Path: %s'%undirected.shortestPath('s','y'))
    undirected.removeEdge('x','y')

    print('Shortest Path after delete edge x->y: %s'%undirected.shortestPath('s','y'))
    
    print('Graph is a DAG: %s'%undirected.isDAG())