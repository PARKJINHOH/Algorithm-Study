# 선택 알고리즘
def selectionSort(OriArr):
    arr = OriArr.copy()

    # 하나를 선택해, 최소값을 찾아 앞에서 부터 정렬하는 방법
    for i in range(len(arr) - 1):
        minVal = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minVal]:
                minVal = j
        arr[i], arr[minVal] = arr[minVal], arr[i]
    print("sort: ", arr)


# 퀵 알고리즘
def quickSort(arr, start, end):

    # 하나의 숫자를 선택해, 해당 숫자보다 작으면 왼쪽, 높으면 오른쪽 -> 반복
    if start >= end:
        return

    # pivot
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[right], arr[left] = arr[left], arr[right]
    quickSort(arr, start, right - 1) # 좌측 정렬
    quickSort(arr, right + 1, end)   # 우측 정렬




# 삽입 알고리즘
def insertSort(OriArr):
    arr = OriArr.copy()
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
    print("insert : ", arr)


# 힙 알고리즘
def heapSort(OriArr):
    arr = OriArr.copy()
    pass


numbers = [10, 4, 3, 68, 48, 29, 50, 109]
print(numbers)

numbers_quick = [10, 4, 3, 68, 48, 29, 50, 109]
selectionSort(numbers)
quickSort(numbers_quick, 0, len(numbers_quick) - 1)
print("quick : ", numbers_quick)

insertSort(numbers)

heapSort(numbers)
