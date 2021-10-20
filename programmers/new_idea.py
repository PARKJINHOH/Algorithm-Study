# https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    answer = ''

    # 1단계
    temp = new_id.lower()

    # 2단계
    for i in temp:
        if i == '-' or i == '_' or i == '.' or i.isdigit() or i.isalpha():
            answer += i

    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4단계
    if len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]

    # 5단계
    if len(answer) == 0:
        answer += 'a'

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7단계
    # if len(answer) < 2:
    #     for _ in range(2):
    #         answer += answer[-1]
    # elif len(answer) == 2:
    #     answer += answer[-1]
    while len(answer) < 3:
        answer += answer[-1]

    return answer


ex1 = "...!@BaT#*..y.abcdefghijklm"
ex2 = "z-+.^."
ex3 = "=.="
ex4 = "123_.def"
ex5 = "abcdefghijklmn.p"
print("ex1:", solution(ex1))
print("ex2:", solution(ex2))
print("ex3:", solution(ex3))
print("ex4:", solution(ex4))
print("ex5:", solution(ex5))
