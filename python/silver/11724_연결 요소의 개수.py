'''import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False for _ in range(n+1)]
edges = {}
for _ in range(m):
    a, b = map(int, input().split())
    if a in edges:
        edges[a].append(b)
    else:
        edges[a] = [b]
    if b in edges:
        edges[b].append(a)
    else:
        edges[b] = [a]

def dfs(v):
    visited[v] = True
    for next in edges.get(v, []):
        if not visited[next]:
            dfs(next)

ans = 0
for i in range(1, n+1):
    if not visited[i]:
        ans += 1
        dfs(i)

print(ans)'''

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

edges = {}
for _ in range(m):
    u, v = map(int, input().split())
    if u not in edges:
        edges[u] = [v]
    else:
        edges[u].append(v)
    if v not in edges:
        edges[v] = [u]
    else:
        edges[v].append(u)

visited = [False for _ in range(n+1)]

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        now = q.popleft()
        for next in edges.get(now, []):
            if not visited[next]:
                q.append(next)
                visited[next] = True

answer = 0
for node in range(1, n+1):
    if not visited[node]:
        answer += 1
        bfs(node)

print(answer)
