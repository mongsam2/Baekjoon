'''
n개의 수열에서 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구한다.
n = input() // 1이상 100,000 이하
numbers[n] = input() // -1000이상 1000이하


def nth_sum(index_list, total):
    global n
    next_index = index_list[-1] + 1
    if (next_index < n):
        total += numbers[next_index]
        index_list.append(next_index)
        nth_sum(index_list, total)
        index_list.pop()
    return

max_sum = -1000*n
for index in range(n):
    max_sum = max(max_sum, numbers[index]) #1개의 합일 때
    nth_sum([index], numbers[index])
-----------------------------------------------------------------------------------------

***DP에서는 점화식이 중요!!***
to_nth_sum = [n] // n번째 까지의 요소를 사용해서 만들 수 있는 합 중의 최대
to_nth_sum[i] = max(numbers[i], to_nth_sum[i-1] + numbers[i])

'''
n = int(input())
numbers = list(map(int, input().split()))

for i in range(1, n):
    numbers[i] = max(numbers[i], numbers[i-1] + numbers[i])

print(max(numbers))
'''
** recursion error 밯생!!
n = int(input())
numbers = list(map(int, input().split()))
max_sum = -1000*n

def nth_sum(index_list, total):
    global n
    global max_sum
    max_sum = max(max_sum, total)
    next_index = index_list[-1] + 1
    if next_index < n:
        total += numbers[next_index]
        index_list.append(next_index)
        nth_sum(index_list, total)
        index_list.pop()
    return

for index in range(n):
    nth_sum([index], numbers[index])
print(max_sum)'''


'''
** 시간초과!!
n = int(input())
numbers = list(map(int, input().split()))
max_total = -1000*n
sum_list = [0]*n 

def sub_total(number_count):
    global max_total
    global n
    for front_idx in range(0, n-number_count+1):
        sum_list[front_idx] += numbers[front_idx + number_count-1]
        max_total = max(max_total, sum_list[front_idx])

for number_count in range(1, n+1):
    sub_total(number_count)
print(max_total)'''