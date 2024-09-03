from collections import deque

n ,m = map(int, input().split())

q = deque([[i] for i in range(1, n+1)])
while q:
    lst = q.popleft()
    if len(lst) == m:
        print(*lst)
        continue
    
    last_num = lst[-1]
    for i in range(1, n+1):
        if i not in lst:
            q.append(lst+[i])


