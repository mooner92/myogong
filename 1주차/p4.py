def solution(answers):
    answer = []
    a, b, c = 0, 0, 0
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if first[i % 5] == answers[i]:
            a += 1
        if second[i % 8] == answers[i]:
            b += 1
        if third[i % 10] == answers[i]:
            c += 1
    answer = [a, b, c]
    answer.sort()

    return answer


k = [1, 2, 3, 4, 5]
print(solution(k))
