from typing import List
from typing import Callable
import numpy as np
import matplotlib.pyplot as plt

Array_Function = Callable[[np.ndarray], np.ndarray]
Chain = List[Array_Function]


def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-x))


def square(x: np.ndarray) -> np.ndarray:
    return np.power(x, 2)


def chain_functions(chain: Chain, x: np.ndarray) -> np.ndarray:
    """Some Functions"""
    assert len(chain) == 2
    "Length of chain must be 2"

    f1 = chain[0]
    f2 = chain[1]

    return f2(f1(x))


PLOT_RANGE = np.arange(-3, 3, 0.01)

chain_funcs = [square, sigmoid]

plt.plot(chain_functions(chain_funcs, PLOT_RANGE))
plt.show()
