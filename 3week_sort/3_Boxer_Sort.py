def solution(weights, head2head):
    winCount = []  # i+1번 선수가 자기보다 무거운 복서를 몇 번 이겼나
    answer = []
    for i in range(len(head2head)):
        overWin = 0
        win = 0
        stage = 0
        for j in range(len(head2head)):
            if head2head[i][j] == 'W' or head2head[i][j] == 'L':
                stage += 1
                if head2head[i][j] == 'W':
                    win += 1
                    if weights[i] < weights[j]:
                        overWin += 1
        if stage != 0:
            winper = win / stage * 100
        else:
            winper = 0
        winCount.append((i + 1, winper, overWin, weights[i]))
    ans = sorted(winCount, key=lambda x: (-x[1], -x[2], -x[3]))

    for i in ans:
        answer.append(i[0])

    return answer


output1 = solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"])
print(output1)
output2 = solution([145, 92, 86], ["NLW", "WNL", "LWN"])
print(output2)
output3 = solution([60, 70, 60], ["NNN", "NNN", "NNN"])
print(output3)
