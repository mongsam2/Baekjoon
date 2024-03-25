import sys
input = sys.stdin.readline
write = sys.stdout.write

n = int(input())
dic = {}
for _ in range(n):
    x, y = map(int, input().split())
    if y not in dic:
        dic[y] = [x]
    else:
        dic[y].append(x)
ans = sorted(dic.items(), key=lambda x : x[0])
for obj in ans:
    y = obj[0]
    xs = obj[1]
    xs.sort()
    for x in xs:
        write(str(x) + " " + str(y) + "\n")
