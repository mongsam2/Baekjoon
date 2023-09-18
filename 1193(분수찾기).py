x = int(input())
line = 0 # 지금이 몇 번째 대각선 라인인지 저장
sum = 0  # 현재까지 확인한 숫자의 개수 저장
# **무한 루프가 아니라 line의 증가 시점 변경으로 해결 가능**

'''while True: # x의 line을 찾는 과정
    sum = sum + line
    if sum >= x: # x의 라인을 찾음
        break
    
    line += 1'''
while sum < x:
    line += 1
    sum = sum + line
index=()
if line%2 == 0: # 라인이 짝수인 경우
    index = (line-(sum-x), 1+(sum-x))
else: # 라인이 홀수인 경우
    index = (1+(sum-x), line-(sum-x))
print('{}/{}'.format(index[0], index[1]))

