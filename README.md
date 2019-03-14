# BipartiteMatchingAlgorithm
Implements the algorithm that finds a maximum matching in a bipartite graph but finding augmented paths and inverting the matched and unmatched edges.

The code runs the algorithm exactly how a human does it on paper. The code follows these steps in a loop:
* Find all the unsaturated white vertices
* Begin a depth first search using each of the root unsaturated white vertices
* The search first checks if the current vertex is an unsaturated black vertex. If it is, then an augmenting path has been found and every edge in the path is inverted from matched to unmatched and unmatched to matched. The loop then restarts from the beginning.
* Then the search checks if the current vertex is a saturated black vertex. If it is, only follow the matched edge and no other edges.
* If the current vertex is a white vertex, follow all edges with that vertex as an endpoint.

The loop repeats until there is a full iteration where no augmented path is found. Within each run of the loop, a list of visited vertices is maintained so each vertex is only visited once. When the unsaturated white vertices are found at the beginning of the loop, they are used to create a brand new forest, so the forest from any previous iteration is discarded.
