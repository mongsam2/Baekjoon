n = int(input())
cnt = 0 # 666포함되는 몇 번째 숫자인지 저장
num = 666 # 1씩 증가하면서 모든 경우의 수 탐색
while True:
    if '666' in str(num): # 숫자를 문자열로 변환해서 666이 포함되는지 확인
        cnt+=1
        if cnt==n: # n번째 숫자를 출력
            print(num)
            break
    num+=1
    