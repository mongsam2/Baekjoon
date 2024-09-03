# 임의의 n국가가 k 국가보다 순위가 높은지 반환
def is_upper(n:list[int], k_nation:list[int]):
    '''
    n 국가가 k국가보다 순위가 높을 때만 True
    '''
    for i in range(1, 4): # 금, 은, 동 매달의 차례대로 비교
        if n[i] > k_nation[i]:
            return True
        elif n[i] < k_nation[i]:
            return False
        else:
            continue
    return False


n, k = map(int, input().split())
nations_dict = dict()
for _ in range(n):
    nation = list(map(int, input().split()))
    nations_dict[nation[0]] = nation

#print(nations_dict)
'''
{
1: [1, 3, 0, 0], 
3: [3, 0, 0, 2], 
4: [4, 0, 2, 0], 
2: [2, 0, 2, 0]
}
'''

rank = 1
for nation in nations_dict.values():
    #print(nation)
    '''if id == nation[0]:
        continue'''
    if is_upper(nation, nations_dict[k]):
        rank += 1
print(rank)


#----------------------------------------------------------------------------------------------
# 참고: dict.values()
'''
dict_values(
    [
        [1, 1, 2, 0], 
        [2, 0, 1, 0], 
        [3, 0, 1, 0], 
        [4, 0, 0, 1]
    ]
)
'''