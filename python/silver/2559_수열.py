'''
연속적인 며칠 동안의 온도의 합이 가장 큰 값을 구한다.

N. K = input() // 온도를 측정한 전체 날짜의 수(2이상 100,000 이하), 연속적인 날짜의 수(1과 N사이의 정수)
temp_list[N+1] = input() // -100이상 100이하


max_value = -100*N
section_total = 0
for index in range(1, N+1 -K+1):
    section_total += temp_list[index]
    if index//K == 0:
        max_value = max(section_total, max_value)
        section_total = 0
print(max_value)

** 구간 합 리스트를 만들지 않아도 해결할 수 있는 방법이 존재한다.
처음에만 k만큼의 구간 합을 구하고, 이후에는 맨 뒤에 수는 빼고, 다음 수를 더하는 방식으로 최대 값을 경신한다.
'''

'''
첫 번째 방법: 구간합 리스트를 먼저 구하고, 이후에 m개 만큼의 요소들의 합을 구한다.
def prefix_sum(num_list):
    size = len(num_list)
    prefix_sum = [0]*size
    prefix_sum[0] = num_list[0]
    for index in range(1, size):
        prefix_sum[index] = prefix_sum[index-1] + num_list[index]
    return prefix_sum

n, k = map(int, input().split())
temp_list = list(map(int, input().split()))

prefix_list = prefix_sum(temp_list)
prefix_list.insert(0, 0) # 인덱스 접근을 쉽게 하기 위함
max_value = -100*n
for index in range(k, n+1):
    section_sum = prefix_list[index] - prefix_list[index-k]
    max_value = max(max_value, section_sum)
print(max_value)
'''
# 방법2: 구간합 리스트를 구하지 않고 반복문 한 번으로 해결
n, k = map(int, input().split())
temp_list = list(map(int, input().split()))


pre_section = sum(temp_list[:k]) # 첫번째 구간의 합
max_value = pre_section # 출력값
for index in range(1, n-k+1):
    new_section = pre_section - temp_list[index-1] + temp_list[index+k-1] # 다음 구간의 합
    max_value = max(max_value, new_section) # 최대값 업데이트
    pre_section = new_section # 이전 구간합 업데이트
print(max_value)