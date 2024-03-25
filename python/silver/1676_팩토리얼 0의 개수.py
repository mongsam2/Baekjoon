n = int(input())
lst = [0 for _ in range(n+1)]
lst[0] = 1
if n>=1:
    lst[1] = 1
def factorial(n):
    global lst
    lst[n] = n * lst[n-1]

for i in range(2, n+1):
    factorial(i)

num = lst[n]
div = 10
remain = num%div
ans = 0
while remain == 0:
    ans += 1
    div = div*10
    remain = num%div
    
print(ans)


