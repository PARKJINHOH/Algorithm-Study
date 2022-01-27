# https://www.acmicpc.net/problem/1546

cnt = int(input())
result = 0

# 점수 입력
old_score = list(map(int, input().split()))
max_score = max(old_score)

for i in old_score:
    result = result + (i / max_score * 100)

print(result / cnt)
