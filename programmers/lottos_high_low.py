# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = []

    zeroCount = 0
    winCount = 0

    for lot in lottos:
        if lot == 0:
            zeroCount += 1
            continue

        for win in win_nums:
            if lot == win:
                winCount += 1
                break

    # 최고 순위 번호
    lot_win = zeroCount + winCount
    if lot_win < 1:
        answer.append(6)
    else:
        answer.append(7 - lot_win)

    # 최저 순위 번호
    if winCount < 1:
        answer.append(6)
    else:
        answer.append(7 - winCount)

    return answer


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))

lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]
print(solution(lottos, win_nums))

lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]
print(solution(lottos, win_nums))