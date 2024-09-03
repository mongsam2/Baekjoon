import sys
input = sys.stdin.readline

n, c = map(int, input().split())
houses = []
for _ in range(n):
    houses.append(int(input()))
houses.sort()

# 1 2 4 8 9      gap = (max-min) / (c-1)
# 1 5 9  8/2 = 4
# 1 3 10 11 12 18 20    공유기 3개
# 19 / 2 = 9.xxx
# 1 11 19   gap =  1~9
# 1 10 11 12 13     3개
# gap 최대 부터 하나씩 줄여가면서, 되는지 확인
# upper bound
def lowerbound(target, start_idx):
    start = start_idx
    end = len(houses)-1
    if target > houses[end]:
        return -1
    while start < end:
        mid = (start+end)//2
        if houses[mid] < target:
            start = mid+1
        else:
            end = mid
    return end

def is_possible(gap):
    now_idx = 0
    for i in range(c-1):
        now = houses[now_idx]
        next_idx = lowerbound(now+gap, now_idx)
        if next_idx == -1:
            return False
        else:
            now_idx = next_idx
    return True

# 1 2 3 4   5  6 7 8 9
max_gap = (houses[-1]-houses[0]) // (c-1)
start = 1
end = max_gap
while start <= end:
    mid = (start+end)//2
    if is_possible(mid):
        start = mid+1
    else:
        end = mid-1
print(end)