N,M = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input())))



def dfs(x,y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

count = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            count +=1
print(count)
        