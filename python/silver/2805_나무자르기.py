n, m = map(int, input().split())
trees = list(map(int, input().split()))
# 4 7
# 20 15 10 17
# 10 15 17 20
# 3  2  0  5
# ** 나무의 길이가 중복 될 경우

# lower bound
trees.sort()

def counting(height):
    ans = 0
    for tree in trees:
        if tree > height:
            ans += tree-height
    return ans

# 4 42 40 26 46     36
# 0 25 50    26 38 50     39 44 50      39 41 43   39 40
# 6
# 0 5 10    6 8 10   6 7  7
'''if len(trees) == 1:
    print(trees[0]-m)
    exit()'''

start = 0 # 10
end = trees[-1] # 20
while start <= end:
    mid = (start+end)//2
    mid_count = counting(mid)
    if mid_count == m:
        print(mid)
        exit()
    elif m < mid_count: # 자르는 높이를 높여라!
        start = mid+1
    elif m > mid_count: # 자르는 높이를 낮춰라!
        end = mid-1
print(end)
        

'''trees.append(0)
top_tree = trees[0]
#to_next = [0 if i==0 else trees[i-1]-trees[i] for i in range(len(trees))]
to_next = [0 for _ in range(len(trees)-1)]
for i in range(len(trees)-1):
    if trees[i] == trees[i+1]:
        to_next[i] = 0
    else:
        to_next[i] = trees[i] - trees[i+1]

level = 0
n = 1
total = 0
for count in to_next:
    for _ in range(count):
        level += 1
        total += n
        if total >= m:
            print(top_tree - level)
            exit()
    n += 1

# 나무가 하나일 때의 경우
print(top_tree-m)'''
