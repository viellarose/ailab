graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':[],
    'F':[]
}

# DFS
visited=[]

def dfs(n):
    if n not in visited:
        print(n,end=" ")
        visited.append(n)

        for i in graph[n]:
            dfs(i)

print("DFS:")
dfs('A')


# BFS
print("\nBFS:")

visited=[]
queue=['A']

while queue:
    n=queue.pop(0)

    if n not in visited:
        print(n,end=" ")
        visited.append(n)
        queue.extend(graph[n])