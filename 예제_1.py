import sys

print(sys.float_info.epsilon)  # 2.220441231231412e-16
a = 0.1 + 0.1 + 0.1
b = 0.3
print(a - b)  # 5.5511151241241223e-17
if (a - b) < sys.float_info.epsilon:
    print("a=b")
else:
    print("a!=b")
