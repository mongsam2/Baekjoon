# 3 6 9 12 15
#  5   10  15  20   25
lst = []
ans = [0]*3
for _ in range(3):
    lst.append(input())

num_idx = 0
for i in range(2, -1, -1):
    if lst[i].isdigit():
        lst[i] = int(lst[i])
        num_idx= i


for di in range(1, 3):
    if num_idx+di < 3:
        lst[num_idx+di] = lst[num_idx]+di

ans = lst[-1] + 1
fizz = ans%3 == 0
buzz= ans%5 == 0

if fizz:
    if buzz:
        print("FizzBuzz")
    else:
        print("Fizz")
else:
    if buzz:
        print("Buzz")
    else:
        print(ans)



