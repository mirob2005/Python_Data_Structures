#Michael Robertson
#mirob2005@gmail.com
#Completed: 4/3/2013

# Implements an Adjacency Matrix

# Can declare the graph as directed/undirected in the constructor.
# Undirected prohibits self-loops whereas directed does not.
# Undirected affects the indices for both A->B and B->A whereas directed
#   only affects the direction declared in the addEdge command

from ADTs.Queue_head import Queue

class AdjMatrix:
    def __init__(self, directed=False):
        self.directed = directed
        self.matrix = []
        self.vertexList = {}
        self.numVertices = 0
        
    def __str__(self):
        string = 'Dest Vert:'
        for key in sorted(self.vertexList, key=self.vertexList.get):
            string += '%7s'%key
        string +='\n'
        for key in sorted(self.vertexList, key=self.vertexList.get):
            string += ('Vertex \'%s\': ['%(key))
            for item in self.matrix[self.vertexList[key]]:
                string += ('%5s, '%item)
            string = string.rstrip(', ')+']\n'
        return string
    
    def __contains__(self,vertex):
        return vertex in self.vertexList
    
    def __iter__(self):
        return iter(self.vertexList.keys())
    
    def addVertex(self,vertex):
        if vertex in self.vertexList:
            print('Vertex %s already exists'%vertex)
            return False
        #Vertex List keeps track of the vertex name and the corresponding index
        #   into the adjacency matrix
        self.vertexList[vertex] = self.numVertices
        self.numVertices += 1
        #Add row to matrix
        self.matrix.append([])
        #Fill out matrix to be square
        for row in self.matrix:
            while len(row) != self.numVertices:
                row.append(False)
        return True
    
    def addEdge(self,vertexFrom,vertexTo):
        if not self.directed and vertexFrom == vertexTo:
            print('Undirected graph cannot have self-loops')
            return False
        try:
            vertexFromIndex = self.vertexList[vertexFrom]
        except:
            print('Vertex %s not found'%vertexFrom)
            return False
        try:
            vertexToIndex = self.vertexList[vertexTo]
        except:
            print('Vertex %s not found'%vertexTo)
            return False
            
        if self.directed:
            #Directed
            self.matrix[vertexFromIndex][vertexToIndex] = True
        else:
            #Undirected
            self.matrix[vertexFromIndex][vertexToIndex] = True
            self.matrix[vertexToIndex][vertexFromIndex] = True
        return True
            
    def removeEdge(self,vertexFrom, vertexTo):
        try:
            vertexFromIndex = self.vertexList[vertexFrom]
        except:
            print('Vertex %s not found'%vertexFrom)
            return False
        try:
            vertexToIndex = self.vertexList[vertexTo]
        except:
            print('Vertex %s not found'%vertexTo)
            return False
        if self.directed:
            #Directed
            self.matrix[vertexFromIndex][vertexToIndex] = False
        else:
            #Undirected
            self.matrix[vertexFromIndex][vertexToIndex] = False
            self.matrix[vertexToIndex][vertexFromIndex] = False
        return True
    
    def removeVertex(self,vertex):
        if not vertex in self.vertexList:
            print('Vertex %s does not exist'%vertex)
            return False
        #Remove vertex from list
        index = self.vertexList.pop(vertex)
        #Remove corresponding column from matrix
        for row in self.matrix:
            row.pop(index)
        #Remove corresponding row from matrix
        self.matrix.pop(index)
        self.numVertices -= 1
        #Reduce the index of all vertices after the removed vertex to keep
        #   matrix and indices organized 
        for key in self.vertexList.keys():
            if self.vertexList[key] > index:
                self.vertexList[key] -= 1
        return True
    
    def traverseDFS(self):
        #Used to keep track if vertex is undiscovered(None), discovered(False),
        #   or fully explored (True)
        visit = {}
        string = ''
        for vertex in self.vertexList.keys():
            visit[vertex] = None
        for vertex in sorted(visit):
            #If any undiscovered vertices remain, they become the new source
            if visit[vertex] == None:
                string += self.DFS(vertex,visit)
        return string
        
    def DFS(self,source,visit):
        visit[source] = False
        string = '(%s '%source
        #Used to index into the adjacency matrix
        index = self.vertexList[source]
        destIndex = 0
        for edge in self.matrix[index]:
            if edge:
                for key,value in self.vertexList.items():
                    if value == destIndex:
                        #If vertex is undiscovered
                        if visit[key] == None:
                            print('Edge %s to %s is a tree edge'%(source,key))
                            string += self.DFS(key,visit)
                        elif visit[key] == False:
                            print('Edge %s to %s is a back edge'%(source,key))
                        else:
                            print('Edge %s to %s is a forward/cross edge'%(source,key))
            destIndex+=1
        visit[source] = True
        string += ' %s)'%source
        return string
    
    def traverseBFS(self,source):
        bfsQ = Queue()
        distanceTo = {}
        if not source in self.vertexList:
            print('Vertex %s does not exist'%source)
            return False
        bfsQ.enQueue(source)
        cur = bfsQ.deQueue()
        distanceTo[cur] = 0
        while cur!=None:
            #Used to index into the adjacency matrix
            index = self.vertexList[cur]
            destIndex = 0
            for edge in self.matrix[index]:
                if edge:
                    for key,value in self.vertexList.items():
                        if value == destIndex:
                            #If vertex is undiscovered
                            if not key in distanceTo:
                                bfsQ.enQueue(key)
                                distanceTo[key] = distanceTo[cur]+1
                destIndex+=1
            cur = bfsQ.deQueue()
        return distanceTo
    
    def shortestPath(self,source,dest):
        if not source in self.vertexList:
            print('Vertex %s does not exist'%source)
            return False
        if not dest in self.vertexList:
            print('Vertex %s does not exist'%dest)
            return False
        distance = self.traverseBFS(source)
        if not dest in distance:
            print('Vertex %s is not reachable from %s'%(dest,source))
            return False
        return distance[dest]
        
    
if __name__ == '__main__':
    am = AdjMatrix(True)
    
    for vertex in ['r','s','t','u','v','w','x','y']:
        am.addVertex(vertex)
    
    for source,dest in [('r','v'),('r','s'),('s','w'),('w','t'),('w','x'),('t','x'),('t','u'),('x','u'),('x','y'),('u','y')]:
        am.addEdge(source,dest)
        
    print(am)
    print('BFS: %s'%am.traverseBFS('r'))
    print('DFS: %s'%am.traverseDFS())
    source = 'r'
    dest = 'y'
    print('Shortest Path from %s to %s is %s'%(source,dest,am.shortestPath(source,dest)))
    print('\n_________________________________\n')
    
    dfs = AdjMatrix(True)
    for vertex in ['y','z','s','t','x','w','v','u']:
        dfs.addVertex(vertex)
        
    for source,dest in [('s','z'),('z','y'),('y','x'),('x','z'),('w','x'),('z','w'),('s','w'),('v','w'),('v','s'),('t','v'),('u','v'),('u','t'),('t','u')]:
        dfs.addEdge(source,dest)
        
    print(dfs)
    print('BFS: %s'%dfs.traverseBFS('s'))
    print('DFS: %s'%dfs.traverseDFS())
    source = 't'
    dest = 'y'
    print('Shortest Path from %s to %s is %s'%(source,dest,dfs.shortestPath(source,dest)))