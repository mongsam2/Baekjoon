n = int(input())
m = int(input())
s = input()

ans = 0
o_count = 0
stack = []
perfact = False
for letter in s:
    if len(stack) == 0:
        if letter == "I":
            stack.append(letter)
    else:
        if letter == "O": # 전 문자가 I일 때만, O를 추가
            if stack[-1] == "I":
                stack.append(letter)
            else: # 전 문자가 같은 O라면, 스택 초기화
                stack = []
                o_count = 0
        else: # I일 때, 
            if stack[-1] == "O":
                stack.append(letter)
                o_count += 1
                perfact = True
            else:
                o_count = 0
                stack = ["I"]
    if perfact and o_count >= n:
        #print(stack)
        perfact = False
        ans += 1
print(ans)

