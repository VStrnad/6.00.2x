class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return str(self.src) + '->' + str(self.dest)
        
class WeightedEdge(Edge):
    def __init__(self, src, dest, totalDist, outdoorDist):
        self.src = src
        self.dest = dest
        self.totalDist = totalDist
        self.outdoorDist = outdoorDist
    def getTotalDistance(self):
        return self.totalDist
    def getOutdoorDistance(self):
        return self.outdoorDist
    def __str__(self):
        return str(self.src) + '->' + str(self.dest) +' (' + str(self.totalDist) + ', ' + str(self.outdoorDist) + ')' 

class Digraph(object):
    def __init__(self):
        self.nodes = set([])
        self.edges = {}
        
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
            
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
        
    def childrenOf(self, node):
        return self.edges[node]
        
    def hasNode(self, node):
        return node in self.nodes
        
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = res + str(k) + ' -> ' + str(d) + '\n'
        return res[:-1]
        
class WeightedDigraph(Digraph):
    def addEdge(self, weightedEdge):
        src = weightedEdge.getSource()
        dest = weightedEdge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append([dest, (float(weightedEdge.getTotalDistance()), float(weightedEdge.getOutdoorDistance()))])
    
    def childrenOf(self, node):
        children = []
        for k in self.edges[node]:
            children.append(k[0])
        return children
    
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = res + str(k) + '->' + str(d[0]) + ' (' + str(d[1][0]) + ', ' + str(d[1][1]) + ')\n'
        return res[:-1]
        
class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self.edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)
        
def printPath(path):
    # a path is a list of nodes
    result = ''
    for i in range(len(path)):
        if i == len(path) - 1:
            result = result + str(path[i])
        else:
            result = result + str(path[i]) + '->'
    return result
    
def DFS(graph, start, end, path = [], shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
    #print 'Current dfs path:', printPath(path)
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            newPath = DFS(graph,node,end,path,shortest)
            if newPath != None:
                return newPath
    
def DFSShortest(graph, start, end, path = [], shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
    #print 'Current dfs path:', printPath(path)
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path)<len(shortest):
                newPath = DFSShortest(graph,node,end,path,shortest)
                if newPath != None:
                    shortest = newPath
    return shortest
    
def BFS(graph, start, end, q = []):
    initPath = [start]
    q.append(initPath)
    while len(q) != 0:
        tmpPath = q.pop(0)
        lastNode = tmpPath[len(tmpPath) - 1]
        #print 'Current dequeued path:', printPath(tmpPath)
        if lastNode == end:
            return tmpPath
        for linkNode in graph.childrenOf(lastNode):
            if linkNode not in tmpPath:
                newPath = tmpPath + [linkNode]
                q.append(newPath)
    return None       
        
def testSP():
    nodes = []
    for name in range(6):
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[0],nodes[2]))
    g.addEdge(Edge(nodes[1],nodes[0]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[3]))
    g.addEdge(Edge(nodes[2],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[1]))
    g.addEdge(Edge(nodes[3],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[5]))
    g.addEdge(Edge(nodes[4],nodes[0]))
    sp = DFS(g, nodes[0],nodes[5])
    print 'Shortest path found by DFS: ' + printPath(sp)
    sp2 = DFSShortest(g, nodes[0],nodes[5])
    print 'Shortest path found by DFSShortest: ' + printPath(sp2)
    sp3 = BFS(g, nodes[0], nodes[5])
    print 'Shortest path found by BFS: ' + printPath(sp)

testSP()
    