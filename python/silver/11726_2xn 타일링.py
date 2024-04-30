# !!! 다시 풀어보기 !!!

n = int(input())
# 1 2 

lst = [0 for i in range(n+1)]
lst[1] = 1
if n>= 2:
    lst[2] = 2
for i in range(3, n+1):
    lst[i] = (lst[i-1]%10007)+(lst[i-2]%10007)
print(lst[-1]%10007)

# 1 0 6 0 5 0 1     10,007

# 0 1 2 3 4 5 6

