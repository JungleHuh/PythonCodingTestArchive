# 플로이드 워셜

INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF]* (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용 0으로 초기화( "a와 b는 같을 수도 있다"라는 조건 처리하기 위함)
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선 정보 입력
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            

cost = 0
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] != INF:
            cost += graph[a][b]
print(cost)