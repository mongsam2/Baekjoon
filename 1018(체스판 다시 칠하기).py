n, m = list(map(int, input().split())) # n과 m입력
board = [] # 보드를 문자열 리스트로 표현
for _ in range(n): 
    board.append(input())

# 체스판 경우의 수 2개
chess1 = [['B' if (i+j)%2==0 else 'W' for j in range(8)]for i in range(8)]
chess2 = [['W' if (i+j)%2==0 else 'B' for j in range(8)]for i in range(8)] 

# 체스판으로 잘랐을 시, 바꿔야하는 블록의 개수 반환
# 비교를 시작하는 보드의 인덱스를 입력
def check(r, c):
    cnt1 = 0 # chess1과 비교
    cnt2 = 0 # chess2와 비교
    
    # 보드에서 추출한 8x8 판과 chess 판을 비교
    for i in range(8):
        for j in range(8):
            if board[r+i][c+j]!=chess1[i][j]:
                cnt1+=1
            if board[r+i][c+j]!=chess2[i][j]:
                cnt2+=1
    return min(cnt1, cnt2) # 바꿔야하는 사각형의 개수를 반환

ans = n*m #  출력할 값
for i in range(n-7):
    for j in range(m-7):
        cnt = check(i, j)
        ans = min(ans, cnt)
print(ans)