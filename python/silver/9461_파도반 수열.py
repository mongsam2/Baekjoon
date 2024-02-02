'''
정삼각형을 나선 모양으로 붙인다.
나선에서 가장 긴 변의 길이를 K 라고 했을 때, 그 변에 길이가 K인 정삼각형을 추가한다.
p(N):  n번째 나선에서 가장 길이가 긴 (새로 이어붙인 정삼각형의 길이)

algorithm:
t: 테스트 케이스의 개수
n: 몇 번째 나선의 길이를 구할 것인지.

1, 1, 1, 2, 2, (2+1), (3+1), (4+1), (5+2), (7+2), (9+3), (12+4), (16+5)
1, 1, 1, 2, 2, 3, 4, 5, 7, 9, (9+3), (12+4), (16+5)
                                12     16      21
n = input()
len_list = [1, 1, 1, 2, 2] + [0]*(n-5)
def p(n):
    if n>=5:
        for i in 0~n-1:
            len_list[i] = len_list[i-1] + len_list[i-5]
    return len_list[n-1]
'''
import sys
t = int(input())

def p(n):
    len_list = [1, 1, 1, 2, 2] + [0 for _ in range(n-5)] # p(1) ~ p(n) 까지 저장할 리스트
    if n>=5:
        for i in range(5, n): # 바텀 업 방식으로 p(n)까지 구한다.
            len_list[i] = len_list[i-1] + len_list[i-5] # 점화식
    return len_list[n-1]

for _ in range(t): # 케이스 개수만큼 반복
    print(p(int(sys.stdin.readline())))