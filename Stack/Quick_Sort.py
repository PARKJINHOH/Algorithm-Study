def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # pivot 보다큰 데이터
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # pivot 보다 작은 데이터
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


array = [5, 6, 7, 8, 1, 2, 3, 4, 0, 1, 11]

quick_sort(array, 0, len(array) - 1)
print(array)