# 센트(0.01달러)  쿼터(0.25)  다임(0.10)  니켈(0.05), 페니(0.01) 

# 남은 달러와 동전의 달러 가격을 입력 -> 업데이트 된 잔액, 동전 개수
'''def exchange(total, d):
    return total%d, total//d
t = int(input())
for _ in range(t):
    c = int(input())
    c, quarter = exchange(c, 25)
    c, dime = exchange(c, 10)
    c, nickel = exchange(c, 5)
    penny = c
    print(quarter, dime, nickel, penny)'''

# [25, 10, 5, 1] 이런 식의 리스트로도 풀이 가능

t = int(input()) # 테스트 케이스
for _ in range(t):
    c = int(input()) # 거스름돈 (센트)
    for n in [25, 10, 5, 1]: # 쿼터, 다임, 니켈, 페니로 바꾸는데 필요한 센트의 개수
        print(c//n, end = ' ') # 쿼터, 다임, 니켈, 페니 개수 순으로 출력
        c = c%n # 남은 거스름돈을 계산
    print()