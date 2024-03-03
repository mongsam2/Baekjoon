import sys
input = sys.stdin.readline

n = int(input())
total = 0 # 평균을 구하기 위해 사용
lst = [] # 입력값들을 정렬할 리스트
count = {}
for _ in range(n):
    num = int(input())
    total += num
    lst.append(num)
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
lst.sort()
max_count = max(count.values())
mods = []
for num, freq in count.items():
    if freq == max_count:
        mods.append(num)
mod = sorted(mods)[1] if len(mods)>1 else mods[0]

avg = round(total/n)
med = lst[n//2]
size = lst[-1] - lst[0]

print(avg)
print(med)
print(mod)
print(size)



# 평균: 총합 / 중앙값, 범위: 정렬, 최반값: 숫자 별로 count
