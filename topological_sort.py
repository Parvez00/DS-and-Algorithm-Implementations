from queue import Queue

graph = {
    'undershorts' : ['pants','shoes'],
    'pants' : ['belt','shoes'],
    'belt' : ['jacket'],
    'shirt' : ['tie','belt'],
    'tie' : ['jacket'],
    'jacket' : [],
    'socks' : ['shoes'],
    'shoes' : [],
    'watch' : []
}

color = {}
previous = {}
trv_time = {}

dfs_traversal = []

topological_sort = []

for key, value in graph.items() :
    color[str(key)] = 'w'
    trv_time[str(key)] = [-1, -1]
    previous[str(key)] = ''

time = 0

def dfs_visit(graph, source):
    global time
    color[str(source)] = 'g'
    trv_time[str(source)][0] = time
    dfs_traversal.append(source)

    for node in graph[source]:
        if color[str(node)] == 'w':
            previous[str(node)] = source
            dfs_visit(graph, node)

    topological_sort.append(source)
    
    color[str(source)] = 'b'
    trv_time[str(source)][1] = time
    time = time+1

def dfs_trv(graph):
    for key, value in graph.items() :
        if color[str(key)] == 'w':
            dfs_visit(graph,key)


dfs_trv(graph)
topological_sort.reverse()
print(f"Sorted Order is:  {topological_sort}")