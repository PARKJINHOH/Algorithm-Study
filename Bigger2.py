n, m, k = list(map(int, input().split()))
data = list(map(int, input().split()))

# M의 크기가 100억 이상처럼 커지면 시간 초과 판정을 받게 된다.
# 반복되는 수열에 대해서 파악 후 개선하자.

data.sort()
fMax = data[n - 1]
sMax = data[n - 1]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * fMax  # 가장 큰 수의 합 더하기
result += (m - count) * sMax  # 두번째로 큰 수의 합 더하기
