import numpy as np
from typing import List
from typing import Callable
import matplotlib.pyplot as plt


Array_Function = Callable[[np.ndarray], np.ndarray]
Chain = List[Array_Function]


def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-x))


def square(x: np.ndarray) -> np.ndarray:
    return np.power(x, 2)


def derive(
    func: Callable[[np.ndarray], np.ndarray], input_: np.ndarray, delta: float = 0.001
) -> np.ndarray:
    return (func(input_ + delta) - func(input_ - delta)) / (2 * delta)


def chain_functions(chain: Chain, a: np.ndarray) -> np.ndarray:
    """Some Functions"""
    assert len(chain) == 2
    "Length of chain must be 2"

    f1 = chain[0]
    f2 = chain[1]

    return f2(f1(a))


def chain_derivatives(chain: Chain, input_range: np.ndarray) -> np.ndarray:

    assert len(chain) == 2, "Function requires 2 functions only"
    assert input_range.ndim == 1, "This function requires 1 dimensional input array"

    f1 = chain[0]
    f2 = chain[1]

    df1dx = derive(f1, input_range)

    f1_of_x = f1(input_range)
    df1dx = derive(f1, input_range)

    df2du = derive(f2, f1_of_x)

    return df1dx * df2du


PLOT_RANGE = np.arange(-3, 3, 0.01)

chain_1 = [square, sigmoid]
chain_2 = [sigmoid, square]

plt.plot(chain_derivatives(chain_1, PLOT_RANGE))
plt.plot(chain_functions(chain_1, PLOT_RANGE))
plt.title("f(x) = sigmoid(square(x))")
plt.show()
