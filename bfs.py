
graph={'A':['B','C'],
       'B':['A','D'],
       'C':['A','F'],
       'D':['B'],
       'E':['B','F'],                                                                                        
       'F':['C','E']
    }
def bfs(graph,start):
    visited = {start}
    s =[start]
    q =[start]
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
L1=list(bfs_paths(graph,'A','F'))
print(L1)

def shortest_path(graph,start,goal):
    try:
        return next(bfs_path(graph,start,goal))
    except StopIteration:
        return None
    
    
                    




































