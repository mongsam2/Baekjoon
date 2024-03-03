'''
(x, y), 인접해 있는 노드의 개수
'''

def make_board():
    m, n, k = map(int, input().split())
    board = [[0 for _ in range(m)] for __ in range(n)]
    index_lst = []
    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1
        index_lst.append((x, y))
    return board, index_lst

def is_connect(x, y, board):
    m = len(board[0])
    n = len(board)
    nothing = True
    # 네 방향 모두 인접한 노드가 없을 때, total 1 증가
    if board[y][x] == 0:
        return
    board[y][x] = 0
    for i, j in [(1,0), (0,1), (-1,0), (0,-1)]:
        if (x+j < m and x+j >= 0) and (y+i < n and y+i >= 0) and (board[y+i][x+j] == 1):
            nothing = False # 방문하고자 하는 노드가 1일 경우에만 is_connect 가 실행, 따라서 for 문 전에 노드 값을 0으로 업데이트
            is_connect(x+j, y+i, board)
    return 1
    
def delete(board, index_lst):
    total = 0 # 그룹의 개수
    for index in index_lst:
        x, y = index
        if board[y][x] == 1:
            total += is_connect(x, y, board)
    print(total)
            
import sys
sys.setrecursionlimit(25000)
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    board, lst = make_board()
    delete(board, lst)
    
