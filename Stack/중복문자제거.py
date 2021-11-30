# 중복된 문자를 제거하고 사전식 순서로 나열하라
import collections


def removeDuplicateLetters(str):
    counter = collections.Counter(str)
    seen = set()
    stack = []
    print(counter)

    for char in str:
        counter[char] -= 1
        if char in seen:
            continue

        # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
        # 'a' < 'b' = True
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())

        stack.append(char)
        seen.add(char)
    return ''.join(stack)

str1 = 'bcabc'
str2 = 'cbacdcbc'
print(removeDuplicateLetters(str1)) # abc
print(removeDuplicateLetters(str2)) # acdb

