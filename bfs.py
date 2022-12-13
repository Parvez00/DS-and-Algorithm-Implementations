from queue import Queue

graph = {
    'r' : ['s','v'],
    's' : ['w','r'],
    't' : ['u','w','x'],
    'u' : ['t','y'],
    'v' : ['r'],
    'w' : ['x','s','t'],
    'x' : ['t','y'],
    'y' : ['x','u']
}

color = {}
distance = {}
previous = {}

for key, value in graph.items() :
    color[str(key)] = 'w'
    distance[str(key)] = 0
    previous[str(key)] = ''


def BFS(graph, source):
    dist = 0 
    q = Queue()
    color[str(source)] = 'g'
    distance[str(source)] = 0
    previous[str(source)] = ''
    q.put(source)

    while not q.empty():
        u = q.get()
        print(u,end = " ")
        for neighbours in graph[str(u)]:
            for node in neighbours:
                if(color[str(node)] == 'w'):
                    color[str(node)] = 'g'
                    distance[str(node)] = int(distance[str(u)]) + 1
                    previous[str(node)] = u
                    q.put(node)
        
        color[str(u)] = 'b'

    for key, value in distance.items() :
        dist = dist + int(value)

    print(f'\nWeight: {dist}')

print('The BFS Traversal is: ')
BFS(graph, 's')