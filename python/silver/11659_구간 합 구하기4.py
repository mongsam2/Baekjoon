'''
수 N개가 주어졌을 때, i번째부터 j번째까지 합을 구하기

N, M = input() // 수의 개수, 케이스의 개수
NUMBERS = input() // N개의 숫자들, 1000보다 작거나 같은 자연수
i, j = input()

for k in i~j:
    total += NUMBERS[k]
'''
import sys
input = sys.stdin.readline
write = sys.stdout.write

N, M = map(int, input().split())
NUMBERS = [0] + list(map(int, input().split()))

# 누적합 배열 생성
def cumulate():
    ans_list = [0]*(N+1) # 인덱스 접근을 편하게 하기 위함
    ans_list[1] = NUMBERS[1]
    for i in range(2, N+1): # 누적합 구하기
        ans_list[i] = ans_list[i-1] + NUMBERS[i]
    return ans_list
def indexing(i, j, lst): # i부터 j까지의 합 구하기
    return lst[j] - lst[i-1]

cumulation_list = cumulate()
for _ in range(M):
    i, j = map(int, input().split())
    ans = indexing(i, j, cumulation_list)
    write(str(ans))
    write("\n")