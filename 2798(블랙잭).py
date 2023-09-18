n, m = list(map(int, input().split())) # n과 m 입력
numbers = list(map(int, input().split())) # 카드 숫자들
max=0 # 3장의 합의 최댓값

# 모든 경우의 수를 탐색한다.
for i in range(len(numbers)): # i: 왼쪽 인덱스
    for j in range(i+1, len(numbers)): # j: 가운데 인덱스
        for k in range(j+1, len(numbers)): # k: 오른쪽 인덱스
            sum = numbers[i]+numbers[j]+numbers[k]
            if sum>max and sum<=m: # 세 수의 합이 max보다 크고 m을 넘지 않는다면 max값을 업데이트
                max = sum
print(max)