import sys
input = sys.stdin.readline
write = sys.stdout.write

'''n = int(input())
dic = {}
for _ in range(n):
    num = int(input())
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1
ans = sorted(dic.items(), key=lambda x : x[0])
for i in ans:
    for _ in range(i[1]):
        write(str(i[0]) + "\n")'''

lst = [0 for _ in range(10001)]
n = int(input())
for _ in range(n):
    num = int(input())
    lst[num] += 1
for i in range(1, 10001):
    for _ in range(lst[i]):
        write(str(i) + "\n")