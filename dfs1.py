graph={'A':set(['B','C']),
       'B':set(['A','D','E']),
       'C':set(['A','F']),
       'D':set(['B']),
       'E':set(['B','F']),
       'F':set(['C','E'])
    }
def dfs(graph,start):
    visited = set()
    stack  = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex]-visited)
    return visited

                
print(dfs(graph,'A'))

def dfs_paths(graph,start,goal):
    stack = [(start,[start])]
    while stack:
        (vertex,path)=stack.pop(0)
        for next in graph[vertex]-set(path):
            if next == goal:
                yield path + [next]
            else:
                    stack.append((next,path+[next]))
L1=list(dfs_paths(graph,'A','E'))
print(L1)
