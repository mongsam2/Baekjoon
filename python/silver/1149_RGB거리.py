'''
i+1번째 집은 i번째 집과 다른 색깔이어야 한다.

n = input() // 집의 개수 2이상 1,000이하
[R, G, B] = input() // 색깔별 비용

** 백트래킹 방식으로 할 경우 시간초과
min_cost[n][color]: n번째 집에서 color 색을 선택했을 때, 최소비용
min_cost[n+1][color] = min(min_cost[n][(color+1)%3], min_cost[n][(color+2)%3]) + houses[n+1][color]
'''


n = int(input())
houses = []
color_list = [0]*n
for _ in range(n):
    houses.append(list(map(int, input().split())))

min_cost = houses.copy()
for nth in range(1, n):
    for color in range(3):
        min_cost[nth][color] = min(min_cost[nth-1][(color+1)%3], min_cost[nth-1][(color+2)%3]) + houses[nth][color] # 아름답다...!
print(min(min_cost[n-1]))



