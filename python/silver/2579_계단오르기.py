# ** 꼭 다시 풀어보기!! **

import sys
input = sys.stdin.readline

n = int(input())
steps = [0, 0, 0]
for _ in range(n):
    steps.append(int(input())) # size = n+3
score = [0 for _ in range(n+3)]
for i in range(3, n+3):
    score[i] = max(score[i-2], steps[i-1] + score[i-3]) + steps[i]
print(score[-1])


# score[n] = max(score[n-2], score[n-3] + steps[n-1]) + steps[n]
'''max_val = 0
def next_step(steps, index, cnt, total):
    global max_val
    #idx += 1 // cnt += 1
    #idx += 2 // cnt=0
    # idx > n  -> X
    if index == n:
        max_val = max(max_val, sum(total))
        return 
    if index+1 <= n and cnt < 2:
        total.append(steps[index])
        next_step(steps, index+1, cnt+1, total)
        total.pop()
    if index+2 <= n:
        total.append(steps[index])
        next_step(steps, index+2, 1, total)
        total.pop()

next_step(steps, 0, 0, [])
print(max_val)'''