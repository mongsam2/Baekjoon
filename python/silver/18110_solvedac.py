import sys
input = sys.stdin.readline
# 1:1  2:2  3:4    // 2
def cal(count, except_count):
    cnt = 0
    i =1
    while cnt < except_count:
        update = min(count[i], (except_count-cnt))
        count[i] -= update
        cnt += update
        i += 1
    
    cnt = 0
    i = 30
    while cnt < except_count:
        update = min(count[i], (except_count-cnt))
        count[i] -= update
        cnt += update
        i -= 1
    total = 0
    for i in range(1, 31):
        total += i*count[i]
    return total

def round2(n):
    if (n - int(n)) >= 0.5:
        return int(n) + 1
    else:
        return int(n)
count = []
n = int(input())
if n == 0:
    print(0)
    exit()
except_count = round2(n*0.3/2)
for _ in range(n):
    count.append(int(input()))
count.sort()
print(round2(sum(count[except_count:n-except_count]) / (n-2*except_count)))

