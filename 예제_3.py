lambda x, y: x + y  # x+y를 진행하는 람다식

add = lambda x, y: x + y  # 람다식은 변수로 참조 가능
print(add(5, 4))  # 9

num = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, num))
print(squares)  # [1,4,9,16,25]
# num 배열의 각 원소를 제곱한 원소로 배열을 수정함
######
