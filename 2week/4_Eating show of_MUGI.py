def solution(food_times, k):
    # 위치
    answer = 0

    # 0이 연속되면 while 문 종료
    count = 0

    # 초
    second = 0
    while True:
        if count == len(food_times):
            return -1

        if answer == len(food_times):
            answer = 0

        if food_times[answer] != 0:
            if second == k:
                return answer + 1
            food_times[answer] = food_times[answer] - 1
            count = 0
            second += 1
        else:
            count += 1
        answer += 1


food_times = [3, 1, 2]
k = 5
result = solution(food_times, k)
print("result : ", result)
