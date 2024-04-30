'''import sys
input = sys.stdin.readline
write = sys.stdout.write

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().rstrip())))
ans = {}

def dfs(idx, number):
    global board
    global ans
    if number in ans:
        ans[number] += 1
    else:
        ans[number] = 1
    board[idx[0]][idx[1]] = number
    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        next_i = idx[0]+di
        next_j = idx[1]+dj
        if (next_i>=0 and next_i<n) and (next_j>=0 and next_j<n) and board[next_i][next_j] == 1:
            dfs((next_i, next_j), number)

number = 1
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            number += 1
            dfs((i, j), number)
            

write(str(number-1)+"\n")
for count in sorted(ans.values()):
    write(str(count)+"\n")'''

import sys
from collections import deque
input = sys.stdin.readline
write = sys.stdout.write

board = []
n = int(input())
for _ in range(n):
    board.append(list(map(int, input().rstrip())))

danzi = 1
def bfs(start):
    total = 1
    q = deque([start])
    board[start[0]][start[1]] = danzi
    while q:
        now = q.popleft()
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = now[0]+di, now[1]+dj
            if (0<=ni<n and 0<=nj<n) and board[ni][nj] == 1:
                total += 1
                q.append((ni, nj))
                board[ni][nj] = danzi
    return total

answer = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            danzi += 1
            answer.append(bfs((i, j)))
answer.sort()
write(str(danzi-1)+"\n")
for ans in answer:
    write(str(ans)+"\n")



