from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
tomatos = []
not_reds = set()
reds = set()
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 0:
            not_reds.add((i, j))
        elif line[j] == 1:
            reds.add((i, j))
    tomatos.append(line)


def bfs(): # (i, j) 형식의 튜플
    q = deque()
    for red in reds:
        q.append(red)
    now = (-1, -1)
    while q:
        now = q.popleft()
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            next_i, next_j = now[0]+di, now[1]+dj
            if (next_i >= 0 and next_i < n) and (next_j >= 0 and next_j < m) and tomatos[next_i][next_j] == 0:
                tomatos[next_i][next_j] = tomatos[now[0]][now[1]] + 1
                not_reds.remove((next_i, next_j))
                q.append((next_i, next_j))
    if len(not_reds) == 0:
        return tomatos[now[0]][now[1]] - 1
    else:
        return -1

ans = bfs()
print(ans)