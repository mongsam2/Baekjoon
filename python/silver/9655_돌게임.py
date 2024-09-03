n = int(input())
dp = [False, False, True, False]
for i in range(4, n+1):
    dp.append(not dp[i-3])

if dp[n] == False:
    print("SK")
else:
    print("CY")

# 1  2  3  4  5  6  7  8
# 0, 1, 0, 1, 0, 1  0  1


# n-1 또는 n-3이 이미 존재한다면, n은 그 결과와 반대가 된다.
# == 상근이가 먼저 1개를 가져가고 시작한다고 가정
# == 상근이가 먼저 3개를 가져가고 시작한다고 가정

# n = 4
# 1 3
# 3

# n = 6
# 3      1
# 6      

# n = 7
# 