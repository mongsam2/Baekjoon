'''
problem: 스도쿠를 완성하여 출력
input: 9줄에 걸쳐서 한 줄에 9개씩 숫자가 주어진다.(1~9). 이 때 빈칸은 0이다.
output: 빈 칸을 채워서 한 줄에 9개씩 출력한다.

조건:
1. 각각의 가로줄과 세로줄에 숫자가 한 번씩만 나와야함.
2. 3x3 네모 안에 숫자가 한 번씩 나와야 함.

알고리즘:
입력 단계에서 조건들에 부합하는 숫자들을 리스트에 따로 저장한다.

board = [9][9]
line_possible = [9][9]
box_possible = [9][9]
zero_list = [(), (), ()]

for row 0~8:
    input_lst = input()
    for col 0~8:
        if input_list[col] == 0:
            zero_list.append((row, col))
        else:
            line_possible[input_list[col]] = False
            box_possible[row//3+col//3][input_list[col]] = False
    
def sudoku(index):
    if index=len(zero_list):
        print(board)
        exit()
    row, col = zero_list[index]
    for number 1~9:
        if line_possible[number] and box_possible[number]:
            line_possible[row][number] = False
            box_possible[row//3+col//3][number] = False
            board[row][col] = number
            sudoku(index+1)
            line_possible[row][number] = True
            box_possible[row//3+col//3][number] = True
'''
# 1. 세로줄 조건을 포함하지 않아서 문제가 발생
import sys

board = [] # 스도쿠 판
row_possible = [[True for _ in range(10)] for i in range(9)] # row_possible[row][number] row번째 행에서 number를 사용할 수 있는가
col_possible = [[True for _ in range(10)] for i in range(9)] # col_possible[col][number] col번째 열에서 number를 사용할 수 있는가
box_possible = [[True for _ in range(10)] for i in range(9)] # box_possible[i][number] i번째 box에서 number를 사용할 수 있는가
zero_list = [] # 빈 칸의 위치 정보를 튜플로 저장

# 입력 단계
for row in range(9):
    input_list = list(map(int, sys.stdin.readline().split())) # 입력 행
    for col in range(9): # 입력 행의 숫자를 하나씩 확인
        if input_list[col]==0: # 숫자가 0일 경우 zero_list에 추가
            zero_list.append((row, col))
        else:
            row_possible[row][input_list[col]] = False # row번째 행에서 해당 숫자 사용확인
            col_possible[col][input_list[col]] = False # col번째 열에서 해당 숫자 사용확인
            box_possible[row//3*3+col//3][input_list[col]] = False # 해당 박스에서 숫자 사용확인
    board.append(input_list) # 스도쿠 row 번째 행 입력

# 스도쿠 보드 출력
def show():
    for num_lst in board:
        for num in num_lst:
            sys.stdout.write(str(num))
            sys.stdout.write(' ')
        sys.stdout.write('\n')

# DFS 방식
def sudoku(index):
    if index==len(zero_list): # 스도쿠 판의 모든 빈 칸을 채웠을 경우, 보드 출력 후 종료
        show()
        exit()
    row, col = zero_list[index] # 빈 칸의 행과 열 정보
    for number in range(1, 10): # 1~9까지 들어갈 수 있는 숫자 탐색
        if row_possible[row][number] and box_possible[row//3*3+col//3][number] and col_possible[col][number]: # 행, 열, 박스에 해당 숫자가 있는지 확인
            row_possible[row][number] = False # 조건 업데이트
            col_possible[col][number] = False # //
            box_possible[row//3*3+col//3][number] = False # //
            board[row][col] = number # 빈 칸에 숫자 채우기
            sudoku(index+1) # 다음 빈 칸으로 이동
            row_possible[row][number] = True # 다음 숫자를 채워보기 전에 기존에 채웠던 숫자 지우기
            col_possible[col][number] = True # //
            box_possible[row//3*3+col//3][number] = True # //
sudoku(0)

