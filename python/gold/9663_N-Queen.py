'''
problom: N개의 퀸이 서로 공격할 수 없게 놓기

input: N (체스판의 크기 N x N)

output: 퀸을 놓을 수 있는 방법의 수

조건:
1. 대각선 불가능
2. 평행 불가능
3. 일자 불가능

count = 0
index = []

def pass(row, col):
    for i in 0 ~ row-1:
        if col == index[i] or abs(row-i) / abs(col-index[i]) == 1:
            return false
    return true

def queen(row): -> row 번째 행에서 queen의 위치를 정하고 다음 행도 똑같이 수행. 대각선에 퀸이 오게 되면 중단
    for col in 0 ~ N:
        if pass(row, col):
            index[row] = col
            if row == N-1:
                count += 1
                break
            queen(row+1)
            
queen(0)
---------------------------------------------------------------------------------------------------------------------

board = [N][N]

'''

# 1. 모든 컬럼을 확인해봤을 때, 가능한 경우가 없을 경우 index에서 값을 빼줘야 한다.
# 2. 시간초과
# 3. 방문한 열을 리스트에 저장

n = int(input()) # 체스판의 크기
global count # 방법의 수
count = 0
index = [0]*n # index[i] i번째 행에서 퀸의 위치
visited = [False]*n # visited[i] i번째 열에 퀸이 있는지 여부

# (row, col) 위치에 놨을 때, 대각선에 다른 퀸이 있는지 확인(없으면 True, 있으면 False 반환)
def passing(row, col):
    for i in range(row): # 지금까지 놓았던 퀸들을 확인
        if row-i==abs(col-index[i]): # 대각선에 있는지 확인
            return False
    return True

# row 번째 열에 퀸을 놓는다.
def queen(row):
    global count
    if row==n: # 모든 행에 퀸을 놓았을 경우
        count += 1
        return
    for col in range(n): # 모든 열을 탐색(DFS)
        if visited[col]: # col번째 열에 이미 퀸이 있는지 확인
            continue
        if passing(row, col): # 대각선에 다른 퀸이 있는지 확인(없을 경우)
            index[row] = col
            visited[col] = True
            queen(row+1) # 다음 행으로 이동
        visited[col] = False # 모든 열에 퀸을 놓을 수 없어서 이전 행으로 돌아갈 때, 현재 행에서 놓은 퀸의 위치를 지워야한다.

queen(0)
print(count)