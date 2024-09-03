import sys
input = sys.stdin.readline
write = sys.stdout.write

n, m = map(int, input().split())
dic = dict()
for _ in range(n):
    address, password = input().rstrip().split()
    dic[address] = password
for _ in range(m):
    address = input().rstrip()
    write(dic[address]+"\n")