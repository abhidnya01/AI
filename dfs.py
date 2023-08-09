
graph={'A':set(['B','C']),
       'B':set(['A','D','E']),
       'C':set(['A','F']),
       'D':set(['B']),
       'E':set(['B','F']),
       'F':set(['C','E'])
    }
def bfs(graph,start):
    visited = {start}
    s =[start]
    q =[]
    q.append(start)
    while len(s) !=0:
        res =s.pop(0)
        for i in graph[res]:
            if i not in visited:
                visited.add(i)
                s.append(i)
                q.append(i)
    return q        
                
print(bfs(graph,'A'))

def bfs_paths(graph,start,goal):
    queue = [(start,[start])]
    while queue:
        (vertex,path)=queue.pop(0)
        for next in graph[vertex]-set(path):
            if next == goal:
                yield path + [next]
            else:
                    queue.append((next,path+[next]))

print(list(bfs_paths(graph,'A','F')))

def shortest_path(graph,start,goal):
    try:
        return next(bfs_path(graph,start,goal))
    except StopIteration:
        return None
    
    
                    


        
            





































