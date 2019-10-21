
class Node(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
class Edge(object):
    def __init__(self,src,dest):
        self.src=src
        self.dest=dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName()+'->'+self.dest.getName()
class Digraph(object):
    def __init__(self):
        self.edges={}
    def addNod(self,node):
        if node in self.edges:
            raise ValueError('Duplicate Node')
        else:
            self.edges[node]=[]
    def addEdge(self,edge):
        src=edge.getSource()
        dest=edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Nodes not in graph')
            self.edges[src].append(dest)
        
            
         
    
    
