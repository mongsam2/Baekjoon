'''import sys
input = sys.stdin.readline
write = sys.stdout.write

def dfs(now):
    global n
    global cnt
    if now == n:
        cnt += 1
    else:
        if now+1 <= n:
            dfs(now+1)
        if now+2 <= n:
            dfs(now+2)
        if now+3 <= n:
            dfs(now+3)

t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    dfs(0)
    write(str(cnt)+"\n")
'''
import sys
input = sys.stdin.readline

ways = [0 for _ in range(11)]
ways[1] = 1 # ways[4] = ways[3] + ways[2] + ways[1]
ways[2] = 2
ways[3] = 4

for n in range(4, 11):
    ways[n] = ways[n-1] + ways[n-2] + ways[n-3]

t = int(input())
for _ in range(t):
    n = int(input())
    print(ways[n])
