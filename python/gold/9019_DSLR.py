import sys
from collections import deque

sys.setrecursionlimit(10**5)
input = sys.stdin.readline
write = sys.stdout.write

dic = {i:order for i, order in enumerate(["D", "S", "R", "L"])}


def dsrl(start:int, end:int):
    visited = {}
    q = deque([start])
    visited[start] = ""

    while q:
        a = q.popleft()
        #print(a)
        for i in range(4):
            new_a = -1
            if i == 0:
                new_a = (int(a)*2)%10000
            elif i == 1:
                new_a = (int(a)-1)%10000
            elif i == 2: #R    0123   3012
                new_a = (a%10)*1000 + a//10
            else: #L    0123    1230
                new_a = (a%1000)*10 + a//1000

            if new_a == end:
                return visited[a]+dic[i]
            
            if new_a not in visited:
                    visited[new_a] = visited[a]+dic[i]
                    q.append(new_a)
'''
1234 3412
1000 1
1 16
'''
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    write(dsrl(a, b) + "\n")

