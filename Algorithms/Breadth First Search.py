from queue import Queue
adj_list={      # Realtionships between nodes
        'A':['B','D'],
        'B':['A','C'],
        'C':['B'],
        'D':['A','E','F'],
        'E':['D','F','G'],
        'F':['D','E','H'],
        'G':['E','H'],
        'H':['G','F']
        }
traverse = []       # For saving the directions for each step
visited={}          # To check if the node is visited of not
root = {}           # To know the parent of each node
level={}            # To know the level of each node
queue=Queue()
for node in adj_list:
    visited[node] = False
    root[node] = None
    level[node] = -1
s='A'    
visited[s]=True
level[s]=0
visited[s] = True
queue.put(s)
while not queue.empty() :
    u = queue.get()
    traverse.append(u)
    for v in adj_list[u] :
        if visited[v] == False:
            visited[v]= True
            root[v] = u
            level[v] = level[u] +1
            queue.put(v)
print (traverse)
        

        
    