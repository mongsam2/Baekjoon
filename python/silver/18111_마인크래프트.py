import sys
input = sys.stdin.readline
import math

def time_cal(height, block_count):
    needed_b = 0
    time = 0
    for h in range(257):
        count = block_count[h]
        if count>0:
            if height > h:
                needed_b += (height-h)*count
                time += (height-h)*count
            elif height < h:
                needed_b -= (h-height)*count
                time += (h-height)*2*count
    return time, needed_b

n, m, b = map(int, input().split())

block_count = [0 for _ in range(257)]
min_num = 257
max_num = -1
for _ in range(n):
    lst = list(map(int, input().split()))
    for num in lst:
        block_count[num] += 1
        min_num = min(min_num, num)
        max_num = max(max_num, num)

min_time = math.inf
ans_height = -1
for height in range(min_num, max_num+1):
    new_time, needed_b = time_cal(height, block_count)
    if needed_b > b:
        continue
    if min_time == new_time:
        ans_height = max(ans_height, height)
    elif new_time < min_time:
        min_time = new_time
        ans_height = height
print(min_time, ans_height)



# 참고할 만한 문제풀이
'''N, M, B = map(int, input().split())
arr = [0] * 257

for i in range(N):
    arr_i = list(map(int, input().split()))
    for n in arr_i:
        arr[n] += 1

time, height = [], []

for h in range(256, -1, -1): # 기준 높이 (0~256)
    B_h, time_h = B, 0
    for i in range(257): # 인덱스
        if arr[i] > 0: # 개수가 1개 이상일 때 수행
            if h < i:
                time_h += 2 * arr[i] * (i-h) # 시간 * 개수 * 차이
                B_h += arr[i] * (i-h)
            elif h > i:
                time_h += 1 * arr[i] * (h-i) # 시간 * 개수 * 차이
                B_h -= arr[i] * (h-i)
    if B_h < 0:
        continue
    time.append(time_h)
    height.append(h)

print(min(time), height[time.index(min(time))])'''