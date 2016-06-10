# Enter your code here. Read input from STDIN. Print output to STDOUT

# N shops, M roads, K fish
N,M,K = map(int, raw_input().strip().split())

# T[i] is number of fish sold at shop i
# A[i] is fish sold at shop i

T = []
A = []

for i in range(N):
    numbers = map(int, raw_input().strip().split())
    T.append(numbers[0])
    A.append(numbers[1:])

# XY is road, Z is weight of road

weighted_graph = []
graph = []

for j in range(M):
    weighted_graph.append(map(int, raw_input().strip().split()))
    graph.append(weighted_graph[j][0:2])

# Need to find smallest subset of N containing N and 1 and also associated with all distinct Aij

paths = []
cycles = []

def findNewPaths(path):
    start_node = path[0]
    next_node= None
    sub = []

    #visit each edge and each node of each edge
    for edge in graph:
        node1, node2 = edge
        if start_node in edge:
                if node1 == start_node:
                    next_node = node2
                else:
                    next_node = node1
        
        if start_node == N:
            if isNew(path):
                    paths.append(path)
                    
        elif not visited(next_node, path): 
                # neighbor node not on path yet
                sub = [next_node]
                sub.extend(path)
                # explore extended path
                findNewPaths(sub);
                
        elif next_node == N:  # making sure we only get paths from 1 to N
                # Path found
                if isNew(path):
                    paths.append(path)

def findNewCycles(path):
    start_node = path[0]
    next_node= None
    sub = []

    #visit each edge and each node of each edge
    for edge in graph:
        node1, node2 = edge
        if start_node in edge:
                if node1 == start_node:
                    next_node = node2
                else:
                    next_node = node1
                    
        # if not visited(next_node, path):
        if not visited(next_node, path): # making sure we only go up to cycles of size 4
                # neighbor node not on path yet
                sub = [next_node]
                sub.extend(path)
                # explore extended path
                findNewCycles(sub);
                
        # elif len(path) > 2  and next_node == path[-1]:
        elif len(path) > 2 and next_node == N:  # making sure we only catch cycles of size 4
                # cycle found
                inv = invert(path)
                if isNew(path) and isNew(inv):
                    cycles.append(path)

def invert(path):
    return rotate_to_smallest(path[::-1])

#  rotate cycle path such that it begins with the smallest node
def rotate_to_smallest(path):
    n = path.index(min(path))
    return path[n:]+path[:n]


def isNew(path):
    return not path in paths

def visited(node, path):
    return node in path

def fishCount(path):
    fish_count = [0 for f in range(K)]
    if len(path) == 0:
        return fish_count
    else: 
        for node in path:
            for fish in A[node - 1]:
                fish_count[fish - 1] = 1
    return fish_count

def pathWeight(path):
    weight = 0
    if len(path) == 1:
        return weight
    else:
        for i in range(len(path) - 1):
            i = len(path) - 1 - i
            if [path[i], path[i-1]] in graph:
                weight += weighted_graph[graph.index([path[i], path[i-1]])][2]
            else:
                weight += weighted_graph[graph.index([path[i-1], path[i]])][2]
    return weight

findNewPaths([1])
findNewCycles([N])

cycles[:0] = [[N]]

value = 10000000000

for index, path1 in enumerate(paths):
    for path2 in paths[index:]:
        for cycle in cycles:
            for cycle2 in cycles:
                fishies = 0
                for i in range(K):
                    if max(fishCount(path1)[i] + fishCount(cycle)[i], fishCount(path2)[i] + fishCount(cycle2)[i]) > 0:
                        fishies += 1
        if fishies == K:
            print path1, cycle, '1'
            print path2, cycle2, '2'
            value = min(value, max(pathWeight(path1) + pathWeight(cycle), pathWeight(path2) + pathWeight(cycle2)))
    
print value