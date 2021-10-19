arr = [
    20, 7, 23, 19, 10, 15, 25, 8, 13
]

# 정렬
arr.sort()

listSum = sum(arr)
overFlower = listSum - 100

left = 0
right = len(arr) - 1

# 알고리즘
while True:
    sum = arr[left] + arr[right]

    if sum != overFlower:
        if sum > overFlower:
            right -= 1
        else:
            left += 1
    else:
        break

    if left == right:
        break

# a == b
arr.remove(arr[right])
arr.remove(arr[left])
print(arr)
