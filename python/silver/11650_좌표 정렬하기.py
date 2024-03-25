import sys
input = sys.stdin.readline
write = sys.stdout.write

lst = []
n = int(input())
for _ in range(n):
    lst.append(list(map(int, input().split())))

for items in sorted(lst):
    x, y = items
    write(str(x) + " " + str(y) + "\n")