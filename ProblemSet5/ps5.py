# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
# This imports everything from `graph.py` as if it was defined in this file!
from ps5_graph import * 

#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here 
# describing how you will model this problem as a graph. 

# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#
mapFilename = "/Users/andrewmarmion/Google Drive/Python/6.00.2x/ProblemSet5/mit_map.txt"
def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    print "Loading map from file..."
    # inFile: file
    inFile = open(mapFilename, 'r', 0) #this loads the file for reading. r = read
        
    # this strips the \n from each line and stores it in a list called lines           
    lines = [(line.rstrip('\n')) for line in inFile]
    
    # this takes each line and makes it into it's own list splitting at the comma
    nodes = []    
    for c in lines:
        a = c.split(',')
        element = []
        for b in a:
            d = b.split()
            elements = []
            for i in d:
                elements.append(int(i))
            
        nodes.append(elements)
    
#starting node:     node[0], 
#ending node:       node[1], 
#total distace:     node[2], 
#outdoor distance:  node[3]
        
    g = WeightedDigraph()
    for node in nodes:
        if not(node[0] in g.nodes):
            g.addNode(node[0])
        
    for node in nodes:
        g.addEdge(WeightedEdge(node[0],node[1],node[2],node[3]))
        
    return g    

#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and what the constraints are

def calculateDistance(graph, path, m):
    '''
    graph: instance of class Digraph or its subclass
    path: is the path that we have travelled
    m: if 0 calculate total totalDistance, if 1 calculate total 
    
    returns the distance travelled on the path
    '''
    #make a copy of the path
    copyPath = path[:] 
    #set the totalDistance travelled so far to 0
    totalDistance = 0
    
    for source in path[:-1]: 
        copyPath = copyPath[1:] 
        next_node = copyPath[0]
        children = graph.edges[source] 
        for i in xrange(len(children)): 
            if children[i][0] == next_node: 
                totalDistance += graph.edges[source][i][1][m] 
                break
    return totalDistance

def DFS(graph, start, end, maxTotalDist, maxDistOutdoors, path=[]):
    '''
    graph: instance of class Digraph or its subclass
    start: starting node
    end:   ending node
    maxTotalDist: the maximum total distance allowed
    maxDistOutdoors: the maximum outdoor distance allowed
    path: the path that has been travelled so far
    
    returns all the paths
    '''
    
    #set up the inital path
    path = path + [start]
    
    #if the start is the end then we are done
    if start == end:         
        return [path]
        
    #store the paths here    
    paths = []
    for node in graph.childrenOf(start):
        #check to see if we have already been there
        if node not in path:
            #calculate the path
            newPath = DFS(graph, node, end, maxTotalDist, maxDistOutdoors, path)
            #check to see that the path meets the constraints
            for p in newPath: 
                if calculateDistance(graph, p, 0) <= float(maxTotalDist) and calculateDistance(graph,p,1) <= float(maxDistOutdoors):
                    paths.append(p)
    return paths
        

def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #set up the nodes
    start = Node(start)
    end = Node(end)
    
    #find the paths
    paths = DFS(digraph, start, end, maxTotalDist, maxDistOutdoors, path=[])
    
    #raise an error if there were no paths found
    if len(paths) == 0: raise ValueError("no paths")
    
    #set the bestPath to None and the bestDist to the maxTotalDist    
    bestPath = None 
    bestDist = maxTotalDist
    
    #check each path in paths to see if its total distance is less than the best distance
    #if it is update the bestDist and bestPath  
    for path in paths:
        totalDistance =calculateDistance(digraph, path,0)
        if totalDistance <= bestDist:
            bestDist = totalDistance
            bestPath = path
    
    #create list of nodes in bestPath                
    bestPathNodes = []    
    for n in bestPath:
        bestPathNodes.append(n.getName())
    return bestPathNodes

#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#
def DFSShortest(graph, start, end, maxTotalDist, maxDistOutdoors, path=[]):
    '''
    graph: instance of class Digraph or its subclass
    start: starting node
    end:   ending node
    maxTotalDist: the maximum total distance allowed
    maxDistOutdoors: the maximum outdoor distance allowed
    path: the path that has been travelled so far
    
    returns all the paths
    '''
    #set up the initial path
    path = path + [start]
    
    #if we are at the end then we are done
    if start == end:         
        return [path]
    
    #store the paths here    
    paths = [] 
    
    for node in graph.childrenOf(start):
        if calculateDistance(graph, path+[node], 0) > float(maxTotalDist) or calculateDistance(graph,path+[node], 1) > float(maxDistOutdoors): 
            continue 
        if node not in path:
            newPath = DFSShortest(graph, node, end, maxTotalDist, maxDistOutdoors, path)
            for p in newPath: 
                paths.append(p)
    return paths

def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
    not exceed maxDistOutdoors.
    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)
    Assumes:
        start and end are numbers for existing buildings in graph
    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.
        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #create the nodes
    start = Node(start)
    end = Node(end)
    
    #find all the paths
    paths = DFSShortest(digraph, start, end, maxTotalDist, maxDistOutdoors, path=[])
    if len(paths) == 0: raise ValueError
    
    #let's find the best path
    bestPath = None
    #set the shortest distance equal to the maximum total distance
    shortestDistance = maxTotalDist 
    #for each path check it's total distance, if it is the shortest distance found
    #save it as the bestPath
    for path in paths:
        totalDistance = calculateDistance(digraph, path, 0)
        if totalDistance <= shortestDistance:
            shortestDistance = totalDistance
            bestPath = path
            
    #create list of nodes in bestPath         
    bestPathNodes = []    
    for n in bestPath:
        bestPathNodes.append(n.getName())
    return bestPathNodes
    
# Uncomment below when ready to test
#### NOTE! These tests may take a few minutes to run!! ####
if __name__ == '__main__':
    #Test cases
    mitMap = load_map(mapFilename)
    print isinstance(mitMap, Digraph)
    print isinstance(mitMap, WeightedDigraph)
    print 'nodes', mitMap.nodes
    print 'edges', mitMap.edges


    LARGE_DIST = 1000000

    #Test case 1
    print "---------------"
    print "Test case 1:"
    print "Find the shortest-path from Building 32 to 56"
    expectedPath1 = ['32', '56']
    brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath1
    print "Brute-force: ", brutePath1
    print "DFS: ", dfsPath1
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)
#
#    #Test case 2
#    print "---------------"
#    print "Test case 2:"
#    print "Find the shortest-path from Building 32 to 56 without going outdoors"
#    expectedPath2 = ['32', '36', '26', '16', '56']
#    brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
#    dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
#    print "Expected: ", expectedPath2
#    print "Brute-force: ", brutePath2
#    print "DFS: ", dfsPath2
#    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2)
#
#    #Test case 3
#    print "---------------"
#    print "Test case 3:"
#    print "Find the shortest-path from Building 2 to 9"
#    expectedPath3 = ['2', '3', '7', '9']
#    brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#    dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#    print "Expected: ", expectedPath3
#    print "Brute-force: ", brutePath3
#    print "DFS: ", dfsPath3
#    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)
#
#    #Test case 4
#    print "---------------"
#    print "Test case 4:"
#    print "Find the shortest-path from Building 2 to 9 without going outdoors"
#    expectedPath4 = ['2', '4', '10', '13', '9']
#    brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
#    dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
#    print "Expected: ", expectedPath4
#    print "Brute-force: ", brutePath4
#    print "DFS: ", dfsPath4
#    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4)
#
#    #Test case 5
#    print "---------------"
#    print "Test case 5:"
#    print "Find the shortest-path from Building 1 to 32"
#    expectedPath5 = ['1', '4', '12', '32']
#    brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
#    dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
#    print "Expected: ", expectedPath5
#    print "Brute-force: ", brutePath5
#    print "DFS: ", dfsPath5
#    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5)
#
#    #Test case 6
#    print "---------------"
#    print "Test case 6:"
#    print "Find the shortest-path from Building 1 to 32 without going outdoors"
#    expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
#    brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
#    dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
#    print "Expected: ", expectedPath6
#    print "Brute-force: ", brutePath6
#    print "DFS: ", dfsPath6
#    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)
#
#    #Test case 7
#    print "---------------"
#    print "Test case 7:"
#    print "Find the shortest-path from Building 8 to 50 without going outdoors"
#    bruteRaisedErr = 'No'
#    dfsRaisedErr = 'No'
#    try:
#        bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
#    except ValueError:
#        bruteRaisedErr = 'Yes'
#    
#    try:
#        directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
#    except ValueError:
#        dfsRaisedErr = 'Yes'
#    
#    print "Expected: No such path! Should throw a value error."
#    print "Did brute force search raise an error?", bruteRaisedErr
#    print "Did DFS search raise an error?", dfsRaisedErr
#
#    #Test case 8
#    print "---------------"
#    print "Test case 8:"
#    print "Find the shortest-path from Building 10 to 32 without walking"
#    print "more than 100 meters in total"
#    bruteRaisedErr = 'No'
#    dfsRaisedErr = 'No'
#    try:
#        bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
#    except ValueError:
#        bruteRaisedErr = 'Yes'
#    
#    try:
#        directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
#    except ValueError:
#        dfsRaisedErr = 'Yes'
#    
#    print "Expected: No such path! Should throw a value error."
#    print "Did brute force search raise an error?", bruteRaisedErr
#    print "Did DFS search raise an error?", dfsRaisedErr
