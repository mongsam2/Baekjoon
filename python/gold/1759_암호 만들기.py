l, c = map(int, input().split())
moum = set(["a", "e", "i", "o", "u"])
letters = sorted(input().split())

def dfs(idx_lst, moum_count):
    global l, c, letters, moum
    if len(idx_lst) == l and len(idx_lst)-moum_count >= 2 and moum_count >= 1:
        print("".join([letters[idx] for idx in idx_lst]))
        return
    
    for i in range(idx_lst[-1]+1, c):
        idx_lst.append(i)
        if letters[i] in moum:
            dfs(idx_lst, moum_count+1)
        else:
            dfs(idx_lst, moum_count)
        idx_lst.pop()

for i in range(c-l+1):
    if letters[i] in moum:
        dfs([i], 1)
    else:
        dfs([i], 0)

'''
acis
acit
aciw
acst
acsw
actw
aist
aisw
aitw
astw
cist
cisw
citw
istw
'''