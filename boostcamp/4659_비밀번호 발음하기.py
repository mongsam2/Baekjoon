moum = ['a', 'e', 'i', 'o', 'u']

def test(word):
    '''규칙에 모두 맞으면 True, 아니면 False'''

    moum_exist = False #모음 존재 여부
    moum_continue = 0 #모음이 몇 번 연속으로 있는지
    jaum_continue = 0 #자음이 몇 번 연속으로 있는지
    prev = "" # 이전 글자

    for letter in word: #한 글자씩 확인

        #모음이 하나라도 존재하면 moum_exist=True
        if not moum_exist and letter in moum:
            moum_exist = True

        #모음과 자음이 연속하는 횟수를 세고
        if letter in moum:
            moum_continue += 1
            jaum_continue = 0
        elif letter not in moum:
            jaum_continue += 1
            moum_continue = 0
        # 만약 3번이 된다면 규칙에 맞지 않음
        if moum_continue == 3 or jaum_continue == 3:
            return False
        
        # e, o가 아니고, 같은 글자가 연속한다면 규칙에 맞지 않음
        if letter not in ["e", "o"] and letter == prev:
            return False
        prev = letter # 이전 글자를 현재 글자로 업데이트

    # 단어를 한 바퀴 돌고난 이후, 모음이 존재하지 않는다면 규칙에 맞지 않음
    if not moum_exist:
        return False
    else:
        return True

while True:
    word = input()
    if word == "end":
        break
    
    # f문자열을 이용해서 문자열 포맷팅
    if test(word):
        print(f"<{word}> is acceptable.")
    else:
        print(f"<{word}> is not acceptable.")
    