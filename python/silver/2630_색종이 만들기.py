import sys
input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

def is_same_color(board, start, end):
    r1, c1 = start
    r2, c2 = end
    start_color = board[start[0]][start[1]]
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            if start_color != board[i][j]:
                return -1
    return start_color
ans = [0, 0]   
def devide(board, start, end):
    global ans
    #print("{} to {}".format(start, end))
    status = is_same_color(board, start, end)
    if status == -1:
        half_size = (end[0] - start[0] + 1)//2
        devide(board, start, (end[0]-half_size, end[1]-half_size))
        devide(board, (start[0], start[1]+half_size), (end[0]-half_size, end[1]))
        devide(board, (start[0]+half_size, start[1]), (end[0], end[1]-half_size))
        devide(board, (start[0]+half_size, start[1]+half_size), end)
    else:
        ans[status] += 1
devide(board, (0, 0), (n-1, n-1))
print(ans[0])
print(ans[1])