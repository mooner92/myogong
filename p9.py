def solution(demical):
    stack = []
    while demical > 0:
        remainder = demical % 2
        stack.append(str(remainder))
        demical //= 2
    binary = ""
    while stack:
        binary += stack.pop()
    return binary


####
####
