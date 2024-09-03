from collections import deque

n = int(input())
edges = []
for _ in range(n):
    edges.append(list(map(int, input().split())))

answer = [[0 for j in range(n)] for i in range(n)]

def bfs(start):
    q = deque([start])
    visited = [0 for _ in range(n)]
    while q:
        now = q.popleft()
        for i in range(n):
            if edges[now][i] == 1 and not visited[i]:
                visited[i] = 1
                q.append(i)
    answer[start] = visited

for i in range(n):
    bfs(i)

for line in answer:
    print(*line)