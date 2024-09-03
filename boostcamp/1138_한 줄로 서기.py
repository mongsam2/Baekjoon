# 6 1 1 1 2 0 0
# 6 5 4 3 2 1 0

# 6 2 3 4 7 5 1
'''
숫자 n인 사람부터 놓는다.
i번째 사람을 놓는다고 할 때, lst[i]가 i번째 사람이 놓일 인덱스가 된다.
'''
n = int(input())
lst = list(map(int, input().split()))
answer = []
answer.append(n)
for i in range(n-1, 0, -1):
    answer.insert(lst[i-1], i)
#print(answer)

print(*answer)
