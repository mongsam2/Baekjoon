# 10진법을 B진법으로 변환하는 방법: 
# 10진법으로 표기된 숫자를 B로 나누어 그 나머지를 표시하고 더 이상 나눌 수 없을 때까지 반복하여 표기하는 방식

n, b = list(map(int, input().split())) # n과 b를 입력받아서 정수로 변환
s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' # 10진법 수를 B진법 수로 변환할 때 사용할 문자열
remainders = [] # 나머지를 저장할 리스트
quotient = n

# 나머지들을 저장하는 과정
while quotient != 0: # 더 이상 나눌 수 없을 때까지 반복
    remainders.append(quotient%b) # 나머지 저장
    quotient = quotient//b # 나눌 수를 업데이트

# 나머지들을 꺼내면서 B진법 수로 변환
for i in remainders[::-1]:
    print(s[i], end='')
