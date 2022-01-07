# 9가지의 숫자중 7개로 숫자 100을 만들어라
# 9개를 모두 더해 100을 뺀 뒤 TwoPointer를 사용해 두 수의 합이 100인 숫자를 리스트에서 제거

# 만약 3개로 100을 만들라고 할 때, 순서대로 앞 숫자 1개가 맞다라는 '예상'하고 나머지 2개를 Two pointer로 찾기

# 조건 : 정렬

listA = [20, 7, 23, 19, 10, 15, 25, 8, 13]

# 정렬
listA.sort()

listSum = sum(listA)
overflower = listSum - 100

left = 0
right = len(listA) - 1

# 알고리즘
while True:
    twoPointer = listA[left] + listA[right]

    if twoPointer != overflower:
        if twoPointer > overflower:
            right -= 1
        else:
            left += 1
    else:
        break

    if left == right:
        break

# a == b
listA.remove(listA[right])
listA.remove(listA[left])




