import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

total = 0
i = n-1
while k > 0:
    total += k//coins[i]
    k = k%coins[i]
    i -= 1

print(total)