# 팰린드롬 : 앞뒤가 똑같은 단어나 문장 (소주 만 병만 주소)

# 1 리스트형
import collections


def solution(str):
    # 리스트에 하나씩 담는다.
    strList = []
    for char in str:
        if char.isalnum():
            strList.append(char.lower())

    # 팰린드롬 여부 판별
    while len(strList) > 1:
        if strList.pop(0) != strList.pop():
            return False

    return True


Tstr = "A man, a plan, a canal: Panama"
Fstr = "ABCDefgAFSEF"
print(solution(Tstr))
print(solution(Fstr))

print("--------------------------------------")



# 데크 자료형을 이용한 최적화
def solution_deque(str):
    # 리스트에 하나씩 담는다.
    str_deque = collections.deque()

    for char in str:
        if char.isalnum():
            str_deque.append(char.lower())

    # 팰린드롬 여부 판별
    while len(str_deque) > 1:
        if str_deque.popleft() != str_deque.pop():
            return False

    return True

print(solution_deque(Tstr))
print(solution_deque(Fstr))


