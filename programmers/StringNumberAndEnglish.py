def solution(s):
    answer = 0

    nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i, value in enumerate(nums):
        if value in s:
            s = s.replace(value, str(i))
        answer = s
    answer = int(answer)
    return answer


s1 = "one4seveneight"
print(solution(s1))
s2 = "23four5six7"
print(solution(s2))
s3 = "2three45sixseven"
print(solution(s3))
s4 = "123"
print(solution(s4))
