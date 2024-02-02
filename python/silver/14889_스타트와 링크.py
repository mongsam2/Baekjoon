'''
N: 모인 사람, 짝수
S[i][j] + S[j][i]: i번 사람과 j번 사람이 같은 팀에 있을 때, 더해지는 능력치
두 팀으로 나누었을 때, 능력치의 총합의 차이가 최소가 되도록

algorithm:
n = input() // 4<= n <=20
s[][] = input() // 1이상 100이하
remain = set(1~n)
included = set()
min_value = 200*10
def make_team(remain, included, score):
    if len(included) == n/2:
        other_score = 0
        for i in range(len(remain)-1):
            for j in range(i+1, len(remain)-1):
                other_score += s[i][j] + s[j][i]
        min_value = min(abs(score - other_score))

    for new_p in remain:
        score = 0
        for team_p in included:
            score += s[new_p][team_p] + s[team_p][new_p]
        make_team(remain.remove(new_p), included.add(new_p), score)

for person in remain: // 5개의 노드로부터 DFS 시작
    make_team(remain.remove(person), included.add(person), 0)

** 리스트의 함수를 사용하는 동시에 make_team의 인자로 넘겨주어서 remain이 none이 되는 오류가 발생함.
** 더러운 코드로 인해 시간초과, 모든 경우를 탐색하는 것을 넘어 중복되는 경우까지 탐색, 따라서 시간 초과

def make_team(member_count):
    

'''
'''
import math
import sys
n = int(input())
s = []
members = [i for i in range(n)]
included = []
score = 0
min_gap = math.inf
visited = []

for _ in range(n):
    s.append(list(map(int, sys.stdin.readline().split())))

def make_team(member_count):
    global min_gap
    global score
    global n
    if (member_count == n/2) and (included not in visited):
        visited.append(included[:])
        other_score = 0
        unincluded = [p for p in members if p not in included]
        for i in range(member_count-1):
            for j in range(i+1, member_count):
                other_score += s[unincluded[i]][unincluded[j]] + s[unincluded[j]][unincluded[i]]
        min_gap = min(min_gap, abs(score-other_score))
        return
    for new_p in [p for p in members if p not in included]:
        plus_score = 0
        for team_p in included:
            plus_score += s[new_p][team_p] + s[team_p][new_p]
        included.append(new_p)
        score += plus_score
        make_team(member_count+1)
        included.remove(new_p)
        score -= plus_score
make_team(0)
print(min_gap)
'''
import sys
import math
N = int(input())
S = []
min_gap = math.inf
for _ in range(N):
    S.append(list(map(int, sys.stdin.readline().split())))

# 한 팀에 소속되지 않은 사람들로 다른 팀을 만든다.
def make_other_team(team_list): # parameters:완성된 팀의 리스트, 전체 사람의 숫자
    global N
    other_team = []
    for p in range(N):
        if p not in team_list:
            other_team.append(p)
    return other_team

# 팀의 총 점수 계산
def score(members): # parameters: 한 팀의 멤버 리스트
    total_score = 0
    length = len(members)
    for i in range(length-1):
        for j in range(i+1, length):
            total_score += S[members[i]][members[j]] + S[members[j]][members[i]]
    return total_score

def make_team(needed_member, team_list): # 팀을 완성하기 위해 필요한 사람 수, 현재 팀 리스트
    # 이전에 팀에 합류한 번호보다 큰 번호만 팀에 추가해야 한다.
    global N # 전체 사람의 수
    global min_gap
    if needed_member == 0:# 팀이 완성이 되었다면
        team_a = score(team_list) # 먼저 완성된 팀의 점수
        other_team = make_other_team(team_list) # 다른 팀 생성
        team_b = score(other_team) # 다른 팀의 점수
        gap = abs(team_a - team_b)
        min_gap = min(min_gap, gap) # 최소 차이 업데이트
        return
    last_included = team_list[-1] 
    for person in range(N):
        if person > last_included: # 중복되는 경우는 탐색하지 않는다.
            team_list.append(person)
            make_team(needed_member-1, team_list)
            team_list.remove(person)

for i in range(N):
    make_team(N//2 - 1, [i])

print(min_gap)

# N까지 모든 경우를 탐색할 필요 없이 절반만 탐색해서 시간을 더욱 단축할 수 있다.