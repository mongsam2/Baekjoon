'''n = int(input())
nums = list(map(int, input().split()))
sorted_nums = sorted(nums)
dic = {}
count = 0
for i in range(n):
    if sorted_nums[i] not in dic:
        dic[sorted_nums[i]] = count
        count += 1

print(" ".join([str(dic[num]) for num in nums]))'''
import sys
write = sys.stdout.write

n = int(input())
nums = list(map(int, input().split()))
sorted_nums = sorted(nums)
dic = {sorted_nums[0]: 0}

count = 1
for i in range(1, n):
    if sorted_nums[i-1] != sorted_nums[i]:
        dic[sorted_nums[i]] = count
        count += 1

for num in nums:
    write(str(dic[num]) +" ")
