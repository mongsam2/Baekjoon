'''
N개의 수열, 수열 사이에 들어갈 N-1개의 연산자
수의 순서를 바꾸면 안 된다.
식의 계산은 우선 순위 무시, 앞에서부터 진행, 나눗셈은 정수 나눗셈
음수를 양수로 나눌 때는 양수로 바꾼 뒤 몫을 구하고 그 몫을 음수로 바꾼다.
만들 수 있는 결과의 최대와 최소를 구하라

algorithm:
operators = [add, sub, mul, div]
op_total = [+, -, x, //] 기호의 개수
op_used = [0]*4
numbers = [N] 입력 숫자들
max_val = -math.inf
min_val = math.inf
global value = numbers[0]
DFS
level = 1 
def find_val(level):
    now = value
    for i in range(4):
        if op_used < op_total:
            value = operators[i](now, numbers[level])
            max_val = max(value, max)
            min_val = min(value, min)
        value = now
한 노드당 5개의 줄기

** 트리의 끝까지 도달했을 때만 최대 최소 값을 업데이트 해주어야 한다.
** 깊이 탐색을 마치고 옆의 노드로 넘어갈 때는 사용한 연산자의 개수도 돌려놓아야 한다.
** 옆의 노드로 넘어가기 위해 값을 돌려놓을 때, 재귀 호출 바로 다음에 해야 한다.
'''
n = int(input()) # 수의 개수
numbers = list(map(int, input().split())) # 연산할 숫자들
op_total = list(map(int, input().split())) # 연산자의 개수(+, -, *, /)
def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):

    if a<0:
        return -(-a//b)
    else:
        return a//b
operators = [add, sub, mul, div] # 연산 함수를 저장하고 있는 리스트
op_used = [0]*4 # 현재까지 사용한 연산자 개수를 연산자 별로 저장
max_val = -1000000000 # 최대값
min_val = 1000000000 # 최소값
value = numbers[0] # 현재까지 식의 연산 결과값
level = 1 # DFS에서의 level

def find_val(level):
    global max_val
    global min_val
    global value
    if level == n: # 식이 완성되었으면 최대, 최소값을 업데이트
        max_val = max(value, max_val)
        min_val = min(value, min_val)
        return
    now = value # 현재 노드에서의 값을 저장
    for i in range(4): # 연산자 별로 엣지를 만들어 DFS를 진행한다.
        if op_used[i] < op_total[i]: # 아직 해당 연산자를 사용할 수 있다면,
            op_used[i] += 1 # 연산자 사용
            value = operators[i](value, numbers[level]) # value를 업데이트 후 다음 level의 노드로 이동한다.
            find_val(level+1)
            value = now # 해당 연산자의 DFS를 완료했고, 다음 연산자로 DFS를 진행하기 위해 값을 원래대로 돌려놓는다.
            op_used[i] -= 1 # 연산자의 사용 횟수도 원래대로 돌려놓는다.
find_val(1)
print(max_val)
print(min_val)