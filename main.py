# a node that holds a single vertex in the forest
# the parent attribute tracks the previous vertex in the forest
class TreeNode(object):
    def __init__(self, name='root', parent=None):
        self.name = name
        self.parent = parent
        self.children = []

# store the label and colour of a vertex
class Vertex(object):
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
    def __str__(self):
        return str(self.name)
    __repr__ = __str__

# get a list of unsaturated white vertices
def getUnsaturatedWhiteVertices():
    unsaturatedWhiteVertices = []

    for v in vertices:
        if v.colour == "B":
            # skip black vertices
            continue
        saturated = False
        adjacentEdges = getAdjacentEdges(v.name)
        # check if any of the adjacent edges are matched
        for m in matching:
            if v.name in m:
                saturated = True
                break

        if saturated == False:
           unsaturatedWhiteVertices.append(v) 

    return unsaturatedWhiteVertices

# get all edges with v as an endpoint
def getAdjacentEdges(vertex_name):
    adjacentEdges = []
    for e in edges:
        if vertex_name in e:
            adjacentEdges.append(e)
    return adjacentEdges

# check if an edge is matched
def isMatchedEdge(e):
    for m in matching:
        if e[0] in m and e[1] in m:
            return True
    return False

# delete an edge from the matching
def removeMatchedEdge(e):
    for index in range(len(matching)):
        if e[0] in matching[index] and e[1] in matching[index]:
            del matching[index]
            return

# inverts the matched and unmatched edges of an augmented path
def invertAugmentedPath(leaf_node):
    current = leaf_node
    while current.parent is not None:
        # look at the edge connecting the current vertex to it's parent
        e = [current.parent.name, current.name]
        # if the edge is matched, remove it from the matching
        if isMatchedEdge(e):
            removeMatchedEdge(e)
        # if the edge was not matched, add it to the matching
        else:
            matching.append(e)
        current = current.parent

# returns the colour of a given vertex
def getVertexColour(vertex_name):
    for v in vertices:
        if v.name == vertex_name:
            return v.colour

def bipartiteMatchingAlgorithm():
    max_matching = False
    # run until the maximum matching is found
    while not max_matching:
        max_matching = True
        rootVertices = getUnsaturatedWhiteVertices()
        visited_vertices = []

        # search the forest for a matching
        # returns a unsaturated black vertex if one is found
        # or False if no unsaturated black vertex exists
        def treeSearchAux(v):
            # don't check a vertex that is already in the forest
            if v.name in visited_vertices:
                return False

            visited_vertices.append(v.name)

            # check if vertex is saturated
            saturated = False
            for m in matching:
                if v.name in m:
                    saturated = True
                    break

            if getVertexColour(v.name) == "B":
                # if the black vertex is unsaturated, an augmented path has been found
                if saturated == False:
                    return v
                else:
                    # can only follow the saturated edge
                    for m in matching:
                        if m[0] == v.name:
                            return treeSearchAux(TreeNode(m[1],v))
                        elif m[1] == v.name:
                            return treeSearchAux(TreeNode(m[0],v))

            else:
                # for a white vertex, check the adjacent edges
                result = False
                for e in getAdjacentEdges(v.name):
                    if e[0] == v.name:
                        result = treeSearchAux(TreeNode(e[1],v))
                    else:
                        result = treeSearchAux(TreeNode(e[0],v))
                    if result != False:
                        return result

            return False

        # begin the forest with the unsaturated white vertices as the tree roots
        for rootVertex in rootVertices:
            result = treeSearchAux(TreeNode(rootVertex.name))

            # when an augmenting path is found, invert the matched and unmatched edges
            if result is not False:
                max_matching = False
                invertAugmentedPath(result)
                break

# set up the first graph
vertices = [Vertex("A","W"), Vertex("B","B"), Vertex("C","W"), Vertex("D","B"), Vertex("E","B")]
edges = [["A","B"],["B","C"],["C","D"],["C","E"]]
matching = [["B","C"]]

# run the algorithm
print("Running algorithm for graph 1")
print("input matching: ", matching)
bipartiteMatchingAlgorithm()
print("new matching: ", matching)

# set up the second graph
vertices = [Vertex("A","W"), Vertex("B","W"), Vertex("C","W"), Vertex("D","W"), Vertex("E","W"),
            Vertex("F","W"), Vertex("G","W"), Vertex("H","W"), Vertex("I","W"), Vertex("J","W"),
            Vertex("1","B"), Vertex("2","B"), Vertex("3","B"), Vertex("4","B"), Vertex("5","B"),
            Vertex("6","B"), Vertex("7","B"), Vertex("8","B"), Vertex("9","B"), Vertex("10","B")]
edges = [
    ["A","6"],["A","2"],
    ["B","2"],["B","1"],
    ["C","1"],["C","3"],["C","8"],
    ["D","3"],["D","8"],["D","2"],
    ["E","2"],["E","5"],["E","6"],
    ["F","6"],["F","7"],["F","9"],["F","4"],
    ["I","5"],["I","7"],["I","9"],["I","4"],["I","8"],
    ["H","8"],["H","10"],
    ["G","8"],["G","10"],
    ["J","8"],["J","10"]
]
matching = [["A","6"],["B","2"],["C","1"], ["D","8"], ["J","10"], ["I","5"],["F","7"]]

# run the algorithm
print("Running algorithm for graph 2")
print("input matching: ", matching)
bipartiteMatchingAlgorithm()
print("new matching: ", matching)