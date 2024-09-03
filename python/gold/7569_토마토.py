import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
tomatos = []
for i in range(h):
    board = []
    for j in range(n):
        board.append(list(map(int, input().split())))
    tomatos.append(board)

q = deque()
last = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomatos[i][j][k] == 1:
                q.append((i, j, k))

last = 0
while q:
    now = q.popleft()
    for di, dj, dk in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]:
        ni, nj, nk = now[0]+di, now[1]+dj, now[2]+dk
        if (ni >= 0 and ni <h) and (nj >= 0 and nj < n) and (nk >= 0 and nk < m) and tomatos[ni][nj][nk] == 0:
            tomatos[ni][nj][nk] = tomatos[now[0]][now[1]][now[2]] + 1
            q.append((ni, nj, nk))
    last = now

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomatos[i][j][k] == 0:
                print(-1)
                exit()

#print(tomatos)
print(tomatos[last[0]][last[1]][last[2]]-1)

'''
2 2 1
1 1
1 0
'''