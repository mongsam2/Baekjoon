# 예를 들어 n이 12인 경우 약수들은 (1, 12), (2, 6), (3, 4)
# 36인 경우 (1, 36), (2, 18), (3, 12), (4, 9), (6, 6) 이런 식으로 약수를 2개씩 구할 수 있다.
# (6, 6)은 하나의 값만 저장해야 한다.

# -1이 입력될 때까지 반복
while True:
    n = int(input())
    if n == -1:
        break
    sum = 1 # n 자신을 제외한 나머지 약수들의 합
    numbers_1 = ['1'] # 약수의 순서쌍에서 앞에 오는 숫자들 ** 자신은 약수에 포함하지 않기 때문에 '1'만 포함한다.
    numbers_2 = [] # 약수의 순서쌍에서 뒤에 오는 숫자들
    

    # n의 약수들을 찾는 과정
    # x1과 x2는 n의 약수
    for x1 in range(2, int(n**(1/2))+1): # 제곱근 연산을 이용해 시간 단축
        if n%x1==0:
            x2 = n//x1
            numbers_1.append(str(x1))
            sum += x1
            if x2 in numbers_1: # n의 두 약수가 같다면 하나의 약수만 저장한다.
                break # 숫자가 중복 되었다면 모든 약수들을 구했다는 것
            numbers_2.append(str(x2))
            sum += x2

    # 완전수인지 판단하는 부분
    # join 함수:
    # 구분자.join(리스트) 형태로 사용
    # 리스트 요소들 사이에 구분자가 들어간 문자열로 반환
    if sum == n:
        numbers = numbers_1 + numbers_2[::-1]
        print('{} = {}'.format(n, ' + '.join(numbers)))
    else:
        print("{} is NOT perfect.".format(n))


# n의 절반까지 반복하는 방법도 있다.
'''
while True:
    num_list = []
    total = 0
    n = int(input())
    
    if n == -1:
        break
    
    for i in range(1, n//2+1):
        if n % i == 0:
            num_list.append(i)
            total += i
            
    if total == n:
        temp = ' + '.join(str(i) for i in num_list)
        print(n, '=', temp)
    else:
        print('{} is NOT perfect.'.format(n))
'''
        