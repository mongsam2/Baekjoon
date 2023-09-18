'''
# 5의 개수: 0~maximum
# 3의 개수: total 무게가 n을 넘어가기 전까지, 정확하게 n이 되지 못하면 패스
# 정확하게 n이 되는 경우가 없으면 -1 출력
n = int(input())
five_maximum = n//5 + 1
minimum = 5000//3 # 짐의 최소 개수
for i in range(five_maximum):
    total = 0 # 짐의 총 무게 ** 반드시 for문 안에 선언!
    #print('i : {}'.format(i))
    j=-1
    while total<=n:
        j+=1
        total = 5*i + 3*j
        #print('{}*{} + {}*{} = {}'.format(5, i, 3, j, 5*i + 3*j))
        if total==n:
            minimum = min(i+j, minimum)

if minimum == 5000//3:
    print(-1)
else:
    print(minimum)
'''
# 위 알고리즘은 이중 반복문으로 복잡하고 시간이 오래 걸림
# 가방의 개수를 최소화 하려면 5의 개수를 최대로 해야한다.
# n이 5로 나누어질 때 까지 3을 빼준다.
# 3을 계속 뺐을 때, 5로 나누어지지 않고, 0이 되지 않았다면 n은 현재 음수라는 뜻이다.
# n이 음수라면 -1을 출력해 준다.
n = int(input())
total = 0 # 설탕 가방의 개수
while n>0: # n이 0이거나 음수가 되면 반복 종료
    if n%5 == 0:
        total += n//5
        n = 0
    else:
        n -= 3
        total += 1
if n<0:
    print(-1)
else:
    print(total)