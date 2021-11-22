from collections import deque

def solution(s):
    answer = -1

    stack = deque()

    for char in s:
        print(char)

        if stack.pop():
            stack.append(char)





    return answer


s = "baabaa"
print(solution(s))



# stack 구현현
# 문자열에서 은 알파벳이 2개 붙어 있는 짝
# 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다
# 문자열을 모두 제거한다면 짝지어 제거하기가 종료
# 성공적으로 수행할 수 있으면 1을, 아닐 경우 0을 리턴해주면 됩니다.