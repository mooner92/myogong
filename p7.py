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


def is_valid_move(nx, ny):  # ➊ 좌표를 벗어나는지 체크하는 함수
    return 0 <= nx < 11 and 0 <= ny < 11


def update_location(x, y, dir):  # ➋ 명령어를 통해 다음 좌표를 결정
    if dir == "U":
        nx, ny = x, y + 1
    elif dir == "D":
        nx, ny = x, y - 1
    elif dir == "L":
        nx, ny = x - 1, y
    elif dir == "R":
        nx, ny = x + 1, y
    return nx, ny


def solution(dirs):
    x, y = 5, 5
    ans = set()  # ➌ 겹치는 좌표는 1개로 처리하기 위함
    for dir in dirs:  # ➍ 주어진 명령어로 움직이면서 좌표 저장
        nx, ny = update_location(x, y, dir)
        if not is_valid_move(nx, ny):  # ➎ 벗어난 좌표는 인정하지 않음
            continue
        # ➏ A에서 B로 간 경우 B에서 A도 추가해야 함(총 경로의 개수는 방향성이 없음)
        ans.add((x, y, nx, ny))
        ans.add((nx, ny, x, y))
        x, y = nx, ny  # ➐ 좌표를 이동했으므로 업데이트
    return len(ans) / 2
