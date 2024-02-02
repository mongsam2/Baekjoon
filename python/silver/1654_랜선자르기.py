'''
int k, n = input() // k: 가지고 있는 랜선의 개수, n: 필요한 랜선의 개수

k개의 길이의 합을 n으로 나눈 평균을 초기값을 정한다.
이것이 출력값의 최대값
출력값을 줄여가면서 k개의 숫자들을 출력값으로 나눈 몫을 구한다.
몫들의 합이 n과 같아질때 까지 반복한다.

# 풀이 2
<231> --> 최대 길이
[457, 539, 743, 802] // lan
[1, 2, 3, 3]    // 최대 길이로 나올 수 있는 조각들의 수
[228, 179, 185, 200] // 조각의 수를 하나 늘리기 위해 요구되는 길이

# 풀이 3
이분탐색

** 랜선이 하나 일때, 오답 발생 추정
** 
2 4
50
200
반복문 범위 설정 문제 -> 더 많이 나누어져도 된다는 문제 조건을 생각하지
'''
import sys
input = sys.stdin.readline
k, n = map(int, input().split())
lan_list = []
max_num = 0
total = 0
for i in range(k):
    l = int(input())
    lan_list.append(l)
    max_num = max(max_num, l)
min_length = 1
max_length = max_num

ans = 0
while min_length <= max_length:
    mid = (min_length + max_length) // 2
    '''if mid == 0:
        print(mid)'''
    count = 0
    for i in range(k):
        count += lan_list[i]//mid
    if count >= n:
        ans = max(ans, mid)
        min_length = mid + 1
    elif count < n:
        max_length = mid - 1
print(ans)