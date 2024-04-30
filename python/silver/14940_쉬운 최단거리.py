'''import sys
from collections import deque
input = sys.stdin.readline
write = sys.stdout.write

n, m = map(int, input().split())
board = []
distances = [[0 for j in range(m)] for i in range(n)]
goal = 0


for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 2:
            goal = (i, j)
    board.append(line)

q = deque([goal])
board[goal[0]][goal[1]] = 0
while q:
    now = q.popleft()
    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        next_i, next_j = now[0]+di, now[1]+dj
        if 0<=next_i<n and 0<=next_j<m and board[next_i][next_j] == 1:
            board[next_i][next_j] = 0
            distances[next_i][next_j] = distances[now[0]][now[1]] + 1
            q.append((next_i, next_j))

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            distances[i][j] = -1
    print(" ".join(map(str, distances[i])))'''

import sys
from collections import deque
input = sys.stdin.readline
write = sys.stdout.write

n, m = map(int, input().split())

start = -1
board = []
visited = [[False for j in range(m)] for i in range(n)]
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(len(line)):
        if line[j] == 2:
            start = (i, j)
            break
    board.append(line)

q = deque([start])
visited[start[0]][start[1]] = True
board[start[0]][start[1]] = 0

while q:
    now = q.popleft()
    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ni, nj = now[0]+di, now[1]+dj
        if 0<=ni<n and 0<=nj<m and board[ni][nj]==1 and  not visited[ni][nj]:
            board[ni][nj] = board[now[0]][now[1]] + 1
            visited[ni][nj] = True
            q.append((ni, nj))

for i in range(n):
    for j in range(m):
        if not visited[i][j] and board[i][j] != 0:
            board[i][j] = -1

for line in board:
    print(" ".join(map(str, line)))


