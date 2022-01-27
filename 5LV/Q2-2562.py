# https://www.acmicpc.net/problem/2562

max_num = 0
max_count = 0
count = 0

for i in range(9):
    input_num = int(input())
    count = count + 1
    if input_num > max_num:
        max_num = input_num
        max_count = count

print(max_num)
print(max_count)