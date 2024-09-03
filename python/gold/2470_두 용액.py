import math

n = int(input())
lst = list(map(int, input().split()))

lst.sort() 
# -99 -2 -1 4 98  //  
# -90 -20 -3 -1

start = 0
end = len(lst)-1
most_zero = math.inf
value_lst = [0, 0]
while start<end:
    value = lst[start]+lst[end]
    if abs(value) < most_zero:
        value_lst[0] = lst[start]
        value_lst[1] = lst[end]
        most_zero = abs(value)
    if value <= 0: # 음수값 줄여!, end + 1
        start += 1
    elif value > 0: # 양수값 줄여
        end -= 1
        # 두 용액 저장 후 반복 종료

print(value_lst[0], value_lst[1])