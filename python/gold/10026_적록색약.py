from collections import deque

# bfs -----------------------------------------------------------------------------------------
def bfs(start, visited, rg=False):
    q = deque([start])
    colors = [board[start[0]][start[1]]]
    
    if rg and board[start[0]][start[1]] in ["R", "G"]:
        colors = ["R", "G"]
    
    visited[start[0]][start[1]] = True

    while q:
        now = q.popleft()
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = now[0]+di, now[1]+dj
            if (ni<n and ni>=0) and (nj<n and nj>=0) and not visited[ni][nj] and board[ni][nj] in colors:
                visited[ni][nj] = True
                q.append((ni, nj))
#----------------------------------------------------------------------------------------------------

n = int(input())

board = []
for _ in range(n):
    board.append(input())

visited1 = [[False for j in range(n)] for i in range(n)]
visited2 = [[False for j in range(n)] for i in range(n)]

# 정상인
answer1 = 0
for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            answer1 += 1
            bfs((i, j), visited1)

# 색약
answer2 = 0
for i in range(n):
    for j in range(n):
        if not visited2[i][j]:
            answer2 += 1
            bfs((i, j), visited2, True)

print(answer1 ,answer2)