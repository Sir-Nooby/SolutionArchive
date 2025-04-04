#DFS Algorithm Example

graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    
    print(start)
    #print(visited)
    
    for i in graph[start]:
        if i not in visited:
            dfs(graph, i, visited)
    return visited
    
dfs(graph, "0")
