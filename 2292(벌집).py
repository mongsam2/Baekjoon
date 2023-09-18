# 1 +6 +12 +18 +24
# 1  2   3   4   5
n = int(input())
distance = 1
num = 1
while num < n:
    num = num + distance*6
    distance += 1
print(distance)
# while문 조건 잘 생각해보기