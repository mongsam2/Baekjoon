# *** 꼭 다시 풀어보기 !! ***

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
breaks = []
#btns = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
if m!=0:
    breaks = input().split()

min_count = abs(n - 100)
if len(breaks) == 10:
    print(min_count)
    exit()
for number in range(1_000_001):
    right = True
    for b in breaks:
        if b in str(number):
            right = False
            break
    if right:
        min_count = min(len(str(number)) + abs(number-n), min_count)
print(min_count)



'''def next_button(lst):
    global n
    global btns
    global min_count
    global is_correct
    idx = len(lst)
    if idx == len(n) + 1:
        num = int("".join(lst))
        goal = int(n)
        min_count = min(min_count, len(lst)+abs(goal-num))
        return
    if idx == len(n):
        for b in btns:
            next_button(lst + [b])
        num = int("".join(lst))
        goal = int(n)
        min_count = min(min_count, len(lst)+abs(goal-num))
        return
    if idx == len(n)-1:
        for b in btns:
            next_button(lst + [b])
        if lst != []:
            num = int("".join(lst))
            goal = int(n)
            min_count = min(min_count, len(lst)+abs(goal-num))
        return
    if is_correct and n[idx] in btns:
        return next_button(lst + [n[idx]])
    else:
        is_correct=False
        for b in btns:
            next_button(lst + [b])'''



# 199
#1
#9


