# https://www.acmicpc.net/problem/1157

import collections

alphabet = input()
alphabet = alphabet.lower()
alpha_list = list(alphabet)

if len(alpha_list) == 1:
    print(alphabet.upper())
else:
    first = collections.Counter(alpha_list).most_common()[0]
    sec = collections.Counter(alpha_list).most_common()[1]

    if first[1] == sec[1]:
        print("?")
    else:
        result = first[0]
        print(result.upper())