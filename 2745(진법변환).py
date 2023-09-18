# B진법을 10진법으로 바꾸는 방법: 
# 변환하려는 진수의 각 자리 값과 각 자리의 지승의 승을 곱한 후에 모두 더해준다.

n, b = input().split() # n과 b를 입력
b = int(b) # b로 연산을 수행해야하기 때문에 정수로 변환
ans = 0 # 출력할 답
# char_to_int: 0~Z의 수를 문자열 형태로 입력하면 정수로 변환하여 출력해주는 딕셔너리
# 0~9의 문자를 정수로 변환해주는 부분과 A~Z의 문자를 정수로 변환해주는 부분을 따로 생성한 후에 결합
# 문자의 정수 변환은 아스키코드를 이용
char_to_int = {chr(ord('0')+i):i for i in range(10)}
char_to_int2 = {chr(ord('A')+i):10+i for i in range(26)}
char_to_int.update(char_to_int2) # update(): 딕셔너리에 새로운 값을 추가하거나 기존 값을 변경해주는 함수
# B진법을 10진법으로 변환하는 과정
for i in range(len(n)):
    ans += char_to_int[n[i]]*b**(len(n)-1-i)
print(ans)

# 개선할 점: 딕셔너리 대신 문자열과 index()를 이용해서 더 간단하게 코드 작성 가능
# s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'