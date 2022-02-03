# https://www.acmicpc.net/problem/4673

# 해당 문제는 생성자 숫자를 먼저 찾은 다음
# 1 ~ 10001 에서 생성자 숫자를 뺀것이 셀프넘버만 남게 되는 풀이.

natural_num = set(range(1, 10001))
generated_num = set()

# 생성자 숫자 찾기
for i in range(1, 10001): # i = 850
    for j in str(i):      # j = "8", "5", "0"
        i += int(j)       # 850 + 8 + 5 + 0, i = 863
    generated_num.add(i)  # 생성자가 있는 숫자들

# 셀프넘버 찾기
self_num = sorted(natural_num - generated_num)


for i in self_num:
    print(i)