def isValid(str):
    stack = []
    table = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in str:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0


str = '()[]{}'
print(isValid(str))
