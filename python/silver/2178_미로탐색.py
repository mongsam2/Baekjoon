import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().rstrip())))

q = deque([[(0, 0), 1]])
visited = [[False for j in range(m)] for i in range(n)]
visited[0][0] = True
while q:
    current_idx, count = q.popleft()
    if current_idx == (n-1, m-1):
        print(count)
        break
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        next_y, next_x = (current_idx[0]+dy, current_idx[1]+dx)
        if (next_y >= 0 and next_y < n) and (next_x >= 0 and next_x < m) and board[next_y][next_x] == 1 and not visited[next_y][next_x]:
            q.append([(next_y, next_x), count+1])
            visited[next_y][next_x] = True
