import sys
input = sys.stdin.readline

n = int(input())
t = int(input())
edges = {}
visited = [False for _ in range(n+1)]

for _ in range(t):
    a, b = map(int, input().split())
    if a not in edges:
        edges[a] = [b]
    else:
        edges[a].append(b)
    if b not in edges:
        edges[b] = [a]
    else:
        edges[b].append(a)
count = 0
def dfs(start):
    global count
    if start != 1:
        count += 1
    for next in edges.get(start, []):
        if not visited[next]:
            visited[next] = True
            dfs(next)

dfs(1)
print(count)