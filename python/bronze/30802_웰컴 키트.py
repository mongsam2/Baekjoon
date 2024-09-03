from math import ceil

n = int(input())
clothes = list(map(int, input().split()))
t, p = map(int, input().split())

clothes_count = 0
for size in clothes:
    clothes_count += ceil(size/t)

print(clothes_count)
print(n//p, n%p)