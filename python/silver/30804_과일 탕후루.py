import sys

n = int(input())
lst = list(map(int, input().split()))

counts = dict()

start = 0
end = 0
counts[lst[start]] = 1
answer = 0

while end < len(lst):
    if len(counts) <= 2:
        if end-start+1 > answer:
            answer = end-start+1

        end += 1
        if end >= len(lst):
            break

        if lst[end] in counts:
            counts[lst[end]] += 1
        else:
            counts[lst[end]] = 1
    else:
        if counts[lst[start]] == 1:
            del counts[lst[start]]
        else:
            counts[lst[start]] -= 1
        start += 1
print(answer)
#dfs(counts, start, end)
#print(ans[1]-ans[0]+1)
#print(visited)


'''while len(counts) >= 2:
    if counts[start] == 1:
        del counts[start]
        start += 1
    else:
        counts[start] -= 1
        start += 1
    '''

'''
참고해보면 좋을 것 같은 코드

def max_fruits(n, s):
    max_fruits_count = 0
    fruit_count = {}
    left = 0
    
    for right in range(n):
        # 오른쪽 포인터가 가리키는 과일을 현재 과일 개수에 추가합니다.
        fruit_count[s[right]] = fruit_count.get(s[right], 0) + 1
        
        # 현재 과일 개수가 2를 초과하면 왼쪽 포인터를 오른쪽으로 옮겨줍니다.
        while len(fruit_count) > 2:
            fruit_count[s[left]] -= 1
            if fruit_count[s[left]] == 0:
                del fruit_count[s[left]]
            left += 1
        
        # 현재 구간의 과일 개수를 확인하여 최대값을 갱신합니다.
        max_fruits_count = max(max_fruits_count, right - left + 1)
    
    return max_fruits_count

# 입력 받기
n = int(input())
s = list(map(int, input().split()))

# 함수 호출하여 최대 과일 개수 구하기
result = max_fruits(n, s)
print(result)
'''