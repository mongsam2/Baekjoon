import sys
input = sys.stdin.readline

n = int(input())
sang = list(map(int, input().split()))
m = int(input())
lst = list(map(int, input().split()))

num_count = dict()
for num in sang:
    if num in num_count:
        num_count[num] += 1
    else:
        num_count[num] = 1

for query in lst:
    ans = "0"
    if query in num_count:
        ans = str(num_count[query])
    sys.stdout.write(ans + " ")
