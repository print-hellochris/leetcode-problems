from typing import List


def solution(a: [int], b: [int], x: int) -> int:
    res = 0
    for i in b:
        if i > x:
            res += 1

    return res


a = [3, 1, 2]
b = [7, 3, 2]
c = 4

print(solution(a, b, c))

# SHOULD ANSWER FUCKING 1
