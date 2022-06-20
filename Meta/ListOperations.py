import numpy as np

print("Python List Operations\n")

a = [1, 2, 3]
b = [4, 5, 6]

print(f"a + b : {a + b}\n")

try:
    print(a * b)
except:
    print(f"{a} * {b} has no meaning in python list\n----------------")

a = np.array([[1, 2], [3, 4]])

print(f"\na : {a}\nSum of axis 0 : {a.sum(axis=0)}\nSum of axis 1 : {a.sum(axis=1)}")

print("Numpy Array Operations\n")

a = [1, 2, 3]
b = [4, 5, 6]

a = np.array(a)
b = np.array(b)

print(f"a + b : {a+b}")
print(f"a * b : {a*b}\n")
