#Michael Robertson
#mirob2005@gmail.com
#Completed: 4/--/2013

# Implements an Adjacency Matrix

# Can declare the graph as directed/undirected in the constructor.
# Undirected prohibits self-loops whereas directed does not.
# Undirected affects the indices for both A->B and B->A whereas directed
#   only affects the direct declared in the addEdge command

class AdjMatrix:
    def __init__(self, directed=False):
        self.directed = directed
        self.matrix = []
        self.vertexList = {}
        self.numVertices = 0
        
    def __str__(self):
        string = ''
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
        self.vertexList[vertex] = self.numVertices
        self.numVertices += 1
        self.matrix.append([])
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
        index = self.vertexList.pop(vertex)
        for row in self.matrix:
            row.pop(index)
        self.matrix.pop(index)
        self.numVertices -= 1
        for key in self.vertexList.keys():
            if self.vertexList[key] > index:
                self.vertexList[key] -= 1
        return True
    
    def traverseDFS(self):
        pass
    
    def traverseBFS(self):
        pass
    
    
if __name__ == '__main__':
    am = AdjMatrix(True)
    
    am.addVertex('A')
    am.addVertex('B')
    am.addVertex('C')
    
    print(am)
    
    am.addEdge('B','C')
    print(am)
    
    am.removeVertex('A')
    
    print(am)
    
    am.addVertex('A')
    print(am)
    
    print('A' in am)
    for item in am:
        print(item)