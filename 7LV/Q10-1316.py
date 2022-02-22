# https://www.acmicpc.net/problem/1316

cnt = int(input())

result = 0
for _ in range(cnt):
    word = input() # 'happy'
    error = 0

    # 문장 check
    for index in range(len(word) -1):
        now_word = word[index]  # 'h'
        next_word = word[index + 1]  # 'a'
        if now_word != next_word:
            new_word = word[index + 1:]
            if new_word.count(word[index]) > 0:
                error += 1

    if error == 0:
        result += 1

print(result)