from heapq import *
from collections import OrderedDict


def prims(graph,start,previous,distance,is_visited):
    bucket = []
    heappush(bucket,[0,start])
    distance[start] = 0
    previous[start] = -1
    while bucket:
        d,n = heappop(bucket)
        if not is_visited[n]:
            is_visited[n] = 1
            for cd,cn in graph[n]:
                if distance[cn] > cd:
                    print(distance[cn])
                    previous[cn] = n
                    distance[cn] = cd
                    heappush(bucket,[cd,cn])


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
graph = {}
previous = {}
distance = {}
is_visited = {}

all_node = []

for start,end,dist in input:
    all_node.append(start)
    all_node.append(end)

all_node = list(set(all_node))


for nodes in all_node:
    graph[nodes] = []
    previous[nodes] = None
    distance[nodes] = 1000000
    is_visited[nodes] = 0

for start,end,dist in input:
    graph[start].append([dist,end])
    graph[end].append([dist,start])


start = 'a'
prims(graph,start,previous,distance,is_visited)

print(OrderedDict(sorted(is_visited.items())))
print(OrderedDict(sorted(distance.items())))
print(OrderedDict(sorted(previous.items())))





