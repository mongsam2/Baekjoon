from collections import deque

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(input()))

people = 0
def bfs(start):
    global people
    q = deque([start])
    board[start[0]][start[1]] = "X"
    while q:
        now = q.popleft()
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = now[0]+di, now[1]+dj
            if (ni>=0 and ni<n) and (nj>=0 and nj<m) and board[ni][nj] != "X":
                if board[ni][nj] == "P":
                    people += 1
                q.append((ni, nj))
                board[ni][nj] = "X"

for i in range(n):
    for j in range(m):
        if board[i][j] == "I":
            bfs((i, j))

if people == 0:
    print("TT")
else:
    print(people)
