'''
def f(x):
    n = 3
    stars = ['***', '* *', '***']
    ans = ['***', '* *', '***']
    while n < x:
        stars = ans[:]
        for i in range(n):
            ans[i] = stars[i]*3
        for i in range(n):
            ans.append(stars[i] + ' '*n + stars[i])
        for i in range(n):
            ans.append(stars[i]*3)
        n = n*3
    
    for star in ans:
        print(star)
f(int(input()))
'''

'''
f(x)
f(3)
라인1: ***
라인2: * *
라인3: ***

f(9)
i: 1~3
라이i = 라인i*3

*********
* ** ** *
*********

공백: 3공백

i: 4~6
라인i = 라인i-3 + 공백3 + 라인i-3

i: 7~9
라인i = 라인i-6*3

f(27)
1~9 x/3개씩
10~18  공백 x/3
19~27

'''

def star(n):
    if n==1:
        return ['*']
    stars = star(n//3)
    ans = []
    for s in stars:
        ans.append(s*3)
    for s in stars:
        ans.append(s + ' '*(n//3) + s)
    for s in stars:
        ans.append(s*3)
    return ans