from heapq import heappop, heappush
import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

max_answer = 0
def dfs(idx, visited):
    global max_answer
    global n, m
    if len(visited) == 4:
        total = sum([board[i][j] for i, j in visited])  
        if max_answer < total:
            max_answer = total
            #print(elements)
        return
    now = idx
    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
         ni, nj = now[0]+di, now[1]+dj
         if (ni>=0 and ni<n) and (nj>=0 and nj<m) and (ni, nj) not in visited:
             visited.add((ni, nj))
             dfs((ni, nj), visited)
             visited.remove((ni, nj))


def fuckyou(idx):
    global m, n, max_answer
    global board
    nodes = []
    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ni, nj = idx[0]+di, idx[1]+dj
        if (ni>=0 and ni<n) and (nj>=0 and nj<m):
            nodes.append(board[ni][nj])
    if len(nodes) >= 3:
        total =  sum(sorted(nodes, reverse=True)[:3]) + board[idx[0]][idx[1]]
        if total > max_answer:
            max_answer = total

for i in range(n):
    for j in range(m):
        visited = set()
        visited.add((i, j))
        dfs((i, j), visited)
        visited.remove((i, j))
        fuckyou((i, j))


print(max_answer)





'''def bfs(start):
    global max_answer
    q = deque([(start,)])
    checked[(start,)] = board[start[0]][start[1]]
    while q:
        elements = q.popleft()
        if len(elements) == 4:
            if max_answer < checked[elements]:
                print(elements)
                max_answer = checked[elements]
            continue
        now = elements[-1]
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = now[0]+di, now[1]+dj
            new_set = elements + ((ni, nj),)
            if (ni>=0 and ni<n) and (nj>=0 and nj<m) and (ni,nj) not in elements and new_set not in checked:
                q.append(new_set)
                checked[new_set] = checked[elements] + board[ni][nj]'''


''''''

'''def search(start): #그리디
    global n, m, max_answer
    max_heap = []
    heappush(max_heap, (-board[start[0]][start[1]], start))
    visited = set([(start[0], start[1])])
    total_score = 0
    for _ in range(4):
        score, now = heappop(max_heap)
        #print(-score)
        total_score -= score
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = now[0]+di, now[1]+dj
            if (ni>=0 and ni<n) and (nj>=0 and nj<m) and ((ni, nj) not in visited):
                visited.add((ni, nj))
                heappush(max_heap, (-board[ni][nj], (ni, nj)))
    
    if max_answer < total_score:
        #print(total_score)
        max_answer = total_score

for i in range(n):
    for j in range(m):
        search((i, j))

print(max_answer)
'''