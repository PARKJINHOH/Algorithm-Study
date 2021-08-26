n, m, k = list(map(int, input().split()))
data = list(map(int, input().split()))

# 첫번째, 두번째 큰값 -> sort() 후 뒤에서 찾기
# Max로 찾으려고 했음. -> 중복 값(1,3,3,2)이 나오면 해당 문제 실패
data.sort()
fMax = data[n - 1]
sMax = data[n - 2]

result = 0

while True:
    # range 잘 살펴보기
    for i in range(k):
        if m == 0:
            break
        result += fMax #k번동안 제일 큰수
        m -= 1
    if m == 0:
        break
    result += sMax # k번 이후 두번째 큰수
    m -= 1
print(result)
