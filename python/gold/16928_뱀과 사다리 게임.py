import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n, m = map(int, input().split())
edges = dict()
for _ in range(n):
    x, y = map(int, input().split())
    edges[x] = y
for _ in range(m):
    u, v = map(int, input().split())
    edges[u] = v

heap = [] # (count, block) 카운트가 적은 블록을 꺼내서 다음 경로 탐색
visited = set()
heappush(heap, (0, 1))

now = 1
while now != 100:
    count, now = heappop(heap)
    if now == 100:
        print(count)
        break

    for i in range(1, 7):
        next_block = now+i

        if next_block <= 100 and next_block not in visited:
            if next_block in edges:
                heappush(heap, (count+1, edges[next_block]))
                visited.update([next_block, edges[next_block]])
            else:
                heappush(heap, (count+1, next_block))
                visited.add(next_block)


'''min_count = [0 for _ in range(101)] # min_count[i] i번째 칸에 도착할 수 있는, 주사위를 던지는 최소 횟수
min_count[1] = 0
min_count[2] = 1'''
# min_count[3] =
# if reverse_stair[3]:  min_count[reverse_stair[3]]
# else:  min_count[max(1, 3-6)]    1 2 3 4 5 6 7
# 
'''for i in range(3, 101):
    if i in reverse_stair:
        min_count[i] = min_count[reverse_stair[i]]
    else:
        min_count[i] = min([min_count[i-j] for j in range(1, 7) if i-j not in snake and i-j>=1])+1

for i in range(2, 101):
    if i in reverse_snake:
        min_count[i] = min(min_count[reverse_snake[i]], min_count[i])

for i in range(2, 101):
    if i in reverse_stair:
        min_count[i] = min_count[reverse_stair[i]]
    else:
        min_count[i] = min(min([min_count[i-j] for j in range(1, 7) if i-j not in snake and i-j>=1])+1, min_count[i])

print(min_count[-1])
print([(i, v) for i, v in enumerate(min_count)])'''


'''
2 1
5 80
31 99
81 30

7 - 50 사다리, 55 - 45 뱀, 47 - 94
2 1
7 50
47 94
55 45

'''