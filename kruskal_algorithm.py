
def find(graph,node):
    if isinstance(graph[node], int) and graph[node] < 0:
        return node
    else:
        temp = find(graph,graph[node])
        graph[node] = temp
        return temp


def union(graph,n1,n2,mst):
    ta = n1
    tb = n2
    a = find(graph,n1)
    b = find(graph,n2)

    if a==b:
        pass
    else:
        mst.append([ta,tb])
        if graph[a] < graph[b]:
            graph[a] = graph[a] + graph[b]
            graph[b] = a
        else:
            graph[b] = graph[a] + graph[b]
            graph[a] = b

input = [
    ['a','b',4],
    ['a','h',8],
    ['b','c',8],
    ['b','h',11],
    ['h','i',7],
    ['h','g',1],
    ['c','i',2],
    ['c','d',7],
    ['c','f',4],
    ['g','f',2],
    ['g','i',6],
    ['d','e',9],
    ['d','f',14],
    ['f','e',10]
]

total_node = 9
input_sorted = sorted(input,key = lambda x : x[2])

dst_graph = {}

all_node = []

mst = []

for start,end,dist in input:
    all_node.append(start)
    all_node.append(end)

all_node = list(set(all_node))

for nodes in all_node:
    dst_graph[nodes] = -1

for u,v,d in input_sorted:
    union(dst_graph,u,v,mst)

print(mst)