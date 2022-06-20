import numpy as np


def square(x: np.ndarray) -> np.ndarray:
    return np.power(x, 2)


a = [1, 2, 3, 4, 5]

# print(square.__annotations__)

print(f"a = {a}\nf(a) = {square(a)}\nType of result [f(a)] : {type(square(a))}")
