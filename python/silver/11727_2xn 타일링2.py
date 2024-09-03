# 1 3 4 
# 1 2 3 4 5 6 7 8

# ㅣ
# ㅣㅣ    =    ㅁ
#111   ㅣㅁ   미    ㅣ=   =ㅣ 
# ㅣㅣㅁ    ㅣㅣ=    ㅣㅣㅣㅣ     =ㅣㅣ     =ㅁ     ==     ㅁ=      미ㅣ     ㅁㅁ
# sol(n) = sol(n-1) + sol(n-2)*3

n = int(input())
solutions = [0 for _ in range(n+1)]
if n >= 1:
    solutions[1] = 1
if n >= 2:
    solutions[2] = 3

for i in range(3, n+1):
    solutions[i] = solutions[i-2]*2 + solutions[i-1]

print(solutions[n]%10007)