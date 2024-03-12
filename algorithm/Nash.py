import numpy as np
from itertools import product
from algorithm.CA import CA
class Nash(CA):
    def __init__(self, rows, cols, check_all_sol, plus_delta, minus_delta,
                 payoff_C_C, payoff_C_D, payoff_D_C, payoff_D_D, is_payoff_1):
        self.rows = rows + 2
        self.cols = cols + 2
        self.check_all_sol = check_all_sol
        self.plus_delta = plus_delta
        self.minus_delta = minus_delta
        self.payoff_C_C = payoff_C_C
        self.payoff_C_D = payoff_C_D
        self.payoff_D_C = payoff_D_C
        self.payoff_D_D = payoff_D_D
        self.is_payoff_1 = is_payoff_1







    def check_all_solutions(self):
        k = self.rows
        n = self.cols
        solutions = [np.reshape(np.array(i), (k - 2, n - 2)) for i in product(range(2), repeat=((k - 2) * (n - 2)))]
        solutions = [np.c_[np.zeros(k - 2), x, np.zeros(k - 2)] for x in solutions]
        solutions = [np.r_[np.zeros((1, n)), x, np.zeros((1, n))] for x in solutions]

        print(solutions)
        return
2