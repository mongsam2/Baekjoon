ans = 0 # 검은색의 넓이
n = int(input()) # 색종이의 수
background = [[0 for _ in range(100)] for x in range(100)] # 흰색 도화지를 2차원 리스트로 표현

# n개의 검은 색종이를 해당 위치에 붙인다.
for _ in range(n):
    x, y = list(map(int, input().split())) # 검은 색종이를 붙일 x, y좌표
    # 10x10 크기만큼 검은 색으로 칠한다.
    for i in range(x, x+10):
        for j in range(y, y+10):
            background[i][j] = 1
# 검은색의 넓이를 구한다.
for line in background:
    ans += line.count(1)
print(ans)

# *** 주의 ***
#----------------------------------------------------
# 리스트를 곱해서 만든 리스트는 '참조'를 통해서 만들어짐
#----------------------------------------------------