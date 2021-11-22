def solution(record):
    answer = []
    user = {}

    # 마지막 닉네임 알아보기
    for char in record:
        command = char.split()

        state = command[0]
        uuid = command[1]

        if state == "Enter":
            nickname = command[2]
            user[uuid] = nickname

        if state == "Change":
            nickname = command[2]
            user[uuid] = nickname

    for char in record:
        command = char.split()

        state = command[0]
        uuid = command[1]

        if state == "Enter":
            a = user[uuid] + "님이 들어왔습니다."
            answer.append(a)

        if state == "Leave":
            a = user[uuid] + "님이 나갔습니다."
            answer.append(a)

    return answer


# 채팅방을 나간 후, 새로운 닉네임으로 다시 들어간다.
# 채팅방에서 닉네임을 변경한다.
# 기존에 채팅방에 출력되어 있던 메시지의 닉네임도 전부 변경
# 채팅방은 중복 닉네임을 허용

recore = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
print(solution(recore))

# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
