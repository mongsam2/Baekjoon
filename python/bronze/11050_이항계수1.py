n, k = map(int, input().split())

# 8c2    8*7 / 2*1
up = 1
down = 1
for i in range(k):
    up = up*(n-i)
    down = down*(k-i)
print(up//down)