tree = {
    'A':['A','B','C'],
    'B':['B','D','E'],
    'C':['C','F','G'],
    'D':['D',0,'H'],
    'E':['E',0,0],
    'F':['F','I','J'],
    'G':['G',0,0],
    'I':['I',0,0],
    'J':['J',0,0],
    'H':['H',0,0]
}


stack = []
root = 'A'
top = 1

stack.append(root)

print("Preorder Traversal:")

while (len(stack) > 0):
    node = stack.pop()
    print(node, end=" ")
    
    node_info = tree[node]
    if node_info[2] != 0:
        stack.append(node_info[2])
    if node_info[1] != 0:
        stack.append(node_info[1])


