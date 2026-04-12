import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        z_minus = z - np.max(z)
        exp_minus = np.exp(z_minus)
        return np.round(exp_minus / (np.sum(exp_minus)),4)
