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

board = []
row_possible = [[True for _ in range(10)] for i in range(9)]
col_possible = [[True for _ in range(10)] for i in range(9)]
box_possible = [[True for _ in range(10)] for i in range(9)]
zero_list = []

for row in range(9):
    input_list = list(map(int, sys.stdin.readline().split()))
    for col in range(9):
        if input_list[col]==0:
            zero_list.append((row, col))
        else:
            row_possible[row][input_list[col]] = False
            col_possible[col][input_list[col]] = False
            box_possible[row//3*3+col//3][input_list[col]] = False
    board.append(input_list) 

def show():
    for num_lst in board:
        for num in num_lst:
            sys.stdout.write(str(num))
            sys.stdout.write(' ')
        sys.stdout.write('\n')

def sudoku(index):
    if index==len(zero_list):
        show()
        exit()
    row, col = zero_list[index]
    for number in range(1, 10):
        if row_possible[row][number] and box_possible[row//3*3+col//3][number] and col_possible[col][number]:
            row_possible[row][number] = False
            col_possible[col][number] = False
            box_possible[row//3*3+col//3][number] = False
            board[row][col] = number
            sudoku(index+1)
            row_possible[row][number] = True
            col_possible[col][number] = True
            box_possible[row//3*3+col//3][number] = True
sudoku(0)

