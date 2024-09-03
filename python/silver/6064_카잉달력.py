import sys
import math

input = sys.stdin.readline
# 최소공배수가 마지막 연도 
# m=10 n=12   60
#m: 1~10  /  n: 1~12    3,1=?  가능한 연도: while m*a + x<=최대연도: lst.append(m*a + x) a += 1

# 1,1  2,2  3,3  4,4 ~ 10,10  1,11  2,12, 3,1
def find_year(m, n, x, y):
    year_set = set()
    max_year = math.lcm(m, n)
    a = 0
    b = 0
    year1 = a*m + x
    year2 = b*n + y
    while year1 <= max_year or year2 <= max_year:
        if year1 in year_set:
            return a*m + x
        year_set.add(year1)
        if year2 in year_set:
            return b*n + y
        year_set.add(year2)
        a += 1
        b += 1
        year1 = a*m + x
        year2 = b*n + y
        #print(year_set)
    return -1

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    ans = find_year(m, n, x, y)
    print(ans)
'''
1 
100 100 34 34
'''