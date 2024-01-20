'''
problem: 주어진 재귀함수를 참고해서 함수의 결과를 출력하는 프로그램 작성
input: 한 줄에 세 정수 a, b, c. 마지막 입력은 -1, -1, -1
output: w(a, b, c) = (결과)

조건:
1. -50 <= a, b, c <= 50 
2. 0이하의 숫자가 하나라도 포함되어야 결과 값이 생긴다.

알고리즘:
한 번 계산한 w(a, b, c)를 3차원 배열 tensor[a][b][c]에 저장한 후 다음에 같은 함수를 호출할 때 사용한다.
1~20, index = number-1
tensor = [20][20][20]
def w(a, b, c):
    if a<=0 or b<=0 or c<=0:
        return 1
    elif a>20 or b>20 or c>20:
        return w(20, 20, 20)
    if tensor[a-1][b-1][c-1] != -1:
        return tensor[a-1][b-1][c-1]
    else:
        if a<b and b<c:
            tensor[a-1][b-1][c-1] = 함수식
        else:
            tensor[a-1][b-1][c-1] = 함수식
        return tensor[a-1][b-1][c-1]
'''
import sys
tensor = [[[-1 for i in range(20)] for j in range(20)] for k in range(20)]

def w(a, b, c):
    if a<=0 or b<=0 or c<=0:
        return 1
    elif a>20 or b>20 or c>20:
        return w(20, 20, 20)
    if tensor[a-1][b-1][c-1] != -1:
        return tensor[a-1][b-1][c-1]
    else:
        if a<b and b<c:
            tensor[a-1][b-1][c-1] =  w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        else:
            tensor[a-1][b-1][c-1] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return tensor[a-1][b-1][c-1]

while(True):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    if a==-1 and b==-1 and c==-1:
        exit()
    sys.stdout.write('w({}, {}, {}) = {}\n'.format(a, b, c, w(a, b, c)))