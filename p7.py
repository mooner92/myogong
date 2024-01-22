"""
def solution(dirs):
    arr = [[0] * 11 for _ in range(11)]
    x, y = 5, 5
    dist = 0
    arr[5][5] = 1
    for i in range(len(dirs)):
        if dirs[i] == "U" and y < 10:
            y += 1
            if arr[x][y] != 1 or arr[x][y - 1] != 1:
                dist += 1
            arr[x][y] = 1
        elif dirs[i] == "D" and y > 0:
            y -= 1
            if arr[x][y] != 1 or arr[x][y + 1] != 1:
                dist += 1
            arr[x][y] = 1
        elif dirs[i] == "R" and x < 10:
            x += 1
            if arr[x][y] != 1 or arr[x - 1][y] != 1:
                dist += 1
            arr[x][y] = 1
        elif dirs[i] == "L" and x > 0:
            x -= 1
            if arr[x][y] != 1 or arr[x + 1][y] != 1:
                dist += 1
            arr[x][y] = 1
        print(f"{x} - {y} -- {dist}")
    return dist


s = "ULURRDLLU"
print(solution(s))
"""
