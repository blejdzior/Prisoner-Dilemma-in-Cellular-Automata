import numpy as np
from itertools import product
from algorithm.CA import CA
class Nash(CA):

    # no init of super class, just methods of CA are used
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
        solutions = [np.c_[np.zeros(k - 2), x, np.zeros(k - 2)] for x in solutions]  # add columns with 0s at the beggining and end
        solutions = [np.r_[np.zeros((1, n)), x, np.zeros((1, n))] for x in solutions]
        sum = []
        for solution in solutions:
            sum_temp = 0
            if self.is_payoff_1:
                for i in range(1, self.rows - 1):
                    for j in range(1, self.cols - 1):
                        # jaka interpretacja akcji w odniesieniu do stanu?
                        sum_temp += self.calculate_payoff_1(solution, i, j)

            else:
                for i in range(1, self.rows - 1):
                    for j in range(1, self.cols - 1):
                        sum_temp += self.calculate_payoff_2(solution, i, j)

            sum.append(round(sum_temp / ((self.rows - 2) * (self.cols - 2)), 4))
        self.save_results(solutions, sum)
        print(sum)
        return

    def save_results(self, solutions, sum):

        f = open("RESULTS//nash_solutions.txt", "w")
        f2 = open("RESULTS//nash_payoffs.txt", "w")
        self.save_parameters(f)
        self.save_parameters(f2)
        for i in range(len(solutions)):
            f.write(str(i) + ":\n")
            f.write(str(solutions[i]))
            f.write("\n")
        index_max = np.argmax(sum)
        f2.write("{0:<7}: {1:<10}\n".format("max_val", "(" + str(index_max) + ", " + str(max(sum)) + ")"))
        for i in range(len(sum)):
            f2.write("{0:<10} {1:<10}\n".format(str(i) + ":", sum[i]))
        print("FINISHED")

    def save_parameters(self, f):
        f.write("# {0:4}: {1:<10}\n# {2:4}: {3:<10}\n".format("rows", self.rows - 2, "cols", self.cols - 2))
        f.write("# {0:10}: {1:<10}\n".format("check_all_sol", self.check_all_sol))
    def is_C_correct(self, cells, i, j):
        if cells[i, j] == 1:
            if cells[i - 1, j - 1] == 0 and cells[i - 1, j] == 0 and cells[i - 1, j + 1] == 0:
                if cells[i, j - 1] == 0 and cells[i, j + 1] == 0:
                    if cells[i + 1, j - 1] == 0 and cells[i + 1, j] == 0 and cells[i + 1, j + 1] == 0:
                        return True
        return False

    def is_D_correct(self, cells, i, j):
        if cells[i, j] == 0:
            # neighbours with 1s in corners
            if cells[i - 1, j - 1] == 1 and cells[i - 1, j] == 0 and cells[i - 1, j + 1] == 1:
                if cells[i, j - 1] == 0 and cells[i, j + 1] == 0:
                    if cells[i + 1, j - 1] == 1 and cells[i + 1, j] == 0 and cells[i + 1, j + 1] == 1:
                        return True
            # neighbours with 1s up and down
            elif cells[i - 1, j - 1] == 0 and cells[i - 1, j] == 1 and cells[i - 1, j + 1] == 0:
                if cells[i, j - 1] == 0 and cells[i, j + 1] == 0:
                    if cells[i + 1, j - 1] == 0 and cells[i + 1, j] == 1 and cells[i + 1, j + 1] == 0:
                        return True
            # neighbours with 1s left and right
            elif cells[i - 1, j - 1] == 0 and cells[i - 1, j] == 0 and cells[i - 1, j + 1] == 0:
                if cells[i, j - 1] == 1 and cells[i, j + 1] == 1:
                    if cells[i + 1, j - 1] == 0 and cells[i + 1, j] == 0 and cells[i + 1, j + 1] == 0:
                        return True
        return False
        
    def calculate_payoff_2(self, solution, i, j):
        m = 0
        sum = 0
        if solution[i, j] == 0:
            is_D = self.is_D_correct(solution, i, j )
            for k in range(i - 1, i + 2):
                for n in range(j - 1, j + 2):
                    if k == i and j == n or k == 0 or n == 0 or k == self.rows - 1 or n == self.cols - 1 :
                        continue
                    if is_D:
                        sum += self.payoff_D_C
                    else:
                        sum += self.payoff_D_D
                    m += 1
        else:
            is_C = self.is_C_correct(solution, i, j)
            for k in range(i - 1, i + 2):
                for n in range(j - 1, j + 2):
                    if k == i and j == n or k == 0 or n == 0 or k == self.rows - 1 or n == self.cols - 1 :
                        continue
                    if is_C:
                        sum += self.payoff_C_C
                    else:
                        sum += self.payoff_C_D
                    m += 1
        return round(sum / float(m), 4)

    def calculate_payoff_1(self, solution, i, j):
        m = 0
        sum = 0
        # action is D
        if solution[i, j] == 0:
            # for loop over cell's neighbours
            for k in range(i - 1, i + 2):
                for n in range(j - 1, j + 2):
                    if k == i and j == n or k == 0 or n == 0 or k == self.rows - 1 or n == self.cols - 1 :
                        continue
                    if solution[k, n] == 1:
                        sum += self.payoff_D_C
                    else:
                        sum += self.payoff_D_D
                    m += 1
        else:
            for k in range(i - 1, i + 2):
                for n in range(j - 1, j + 2):
                    if k == i and j == n or k == 0 or n == 0 or k == self.rows - 1 or n == self.cols - 1 :
                        continue
                    if solution[k, n] == 1:
                        sum += self.payoff_C_C
                    else:
                        sum += self.payoff_C_D
                    m += 1
        return round(sum / float(m), 4)
