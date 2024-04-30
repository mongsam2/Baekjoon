n = int(input())
times = list(map(int, input().split()))

times.sort()
ans = 0
for i in range(n):
    ans += (n-i)*times[i]
print(ans)