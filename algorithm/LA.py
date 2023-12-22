# Learning automaton
from algorithm.CA import CA
import copy
import random
import time
import os
class LA(CA):
    def __init__(self, M_rows, N_cols, p_init_C, allC, allD, kD, kC, minK, maxK, num_of_iter,
                 payoff_C_C, payoff_C_D, payoff_D_C, payoff_D_D, is_sharing, synch_prob,
                 is_tournament, p_state_mut, p_strat_mut, p_0_neigh_mut, p_1_neigh_mut, is_debug, is_test1, is_test2,
                 f, optimal_num1s, is_payoff_1, u, memory_h, epsilon, min_payoff, is_multi_run=False, seed=None):
        # Parent class init
        CA.__init__(self, M_rows, N_cols, p_init_C, allC, allD, kD, kC, minK, maxK, num_of_iter,
                 payoff_C_C, payoff_C_D, payoff_D_C, payoff_D_D, is_sharing, synch_prob,
                 is_tournament, p_state_mut, p_strat_mut, p_0_neigh_mut, p_1_neigh_mut, is_debug, is_test1, is_test2,
                 f, optimal_num1s, is_payoff_1, u, is_multi_run, seed, is_LA=True)

        # Depth of cells memory
        self.h = memory_h
        # Chance that strategy will be assigned randomly to a cell
        self.epsilon = epsilon

        self.min_payoff = min_payoff

        self.kDC = round(1 - self.allC - self.allD - self.kD - self.kC, 4)
        if self.kDC < 0:
            self.kDC = 0
        self.strategies = []
        if self.allC > 0:
            self.strategies.append(1)
        if self.allD > 0:
            self.strategies.append(0)
        if self.kD > 0:
            self.strategies.append(2)
        if self.kC > 0:
            self.strategies.append(3)
        if self.kDC > 0:
            self.strategies.append(4)
        self.cells = []
        self.automaton_init()



    def evolution(self):

        if self.is_multi_run:
            print("process started PID: %d" % os.getpid())
        else:
            print("thread started")

        for k in range(self.num_of_iter):
            _, cells = self.cells[k]
            for i in range(1, self.M_rows - 1):
                for j in range(1, self.N_cols - 1):
                    cells[i, j].sum_payoff = 0

            change_strat_count = 0
            change_strat_count_final = 0

            sum_payoff_temp = 0

            cells_temp = copy.deepcopy(cells)
            # update cell states according to strategy:
            for i in range(1, self.M_rows - 1):
                for j in range(1, self.N_cols - 1):
                    # decide whether cell will be changing strategy in this iteration with synch_prob probability
                    self.is_cell_changing_strategy(cells_temp[i, j])
                    self.update_cell_states(cells, cells_temp, i, j)

            # decide action
            if self.is_payoff_1:
                for i in range(1, self.M_rows - 1):
                    for j in range(1, self.N_cols - 1):
                            cells_temp[i, j].action = self.decide_action(cells_temp, i, j)

            # calculate payoffs
            for i in range(1, self.M_rows - 1):
                for j in range(1, self.N_cols - 1):
                    if self.is_payoff_1:
                        self.calculate_payoff_1(cells_temp, i, j)
                    else:
                        self.calculate_payoff_2(cells_temp, i, j)
                    # cells[i, j].avg_payoff /= u_
                    sum_payoff_temp += cells_temp[i, j].avg_payoff

            # redistribute payoffs
            if self.is_sharing:
                cells_temp1 = copy.deepcopy(cells_temp)
                sum_payoff_temp = 0
                for i in range(1, self.M_rows - 1):
                    for j in range(1, self.N_cols - 1):
                        self.redistribute_payoff(cells_temp, cells_temp1, i, j)
                        sum_payoff_temp += cells_temp[i, j].avg_payoff

            self.avg_payoff.append((k, sum_payoff_temp / ((self.M_rows - 2) * (self.N_cols - 2))))

            # checks if it has reached max num of iterations so the rest of loop doesn't have to execute
            if k >= self.num_of_iter - 1:
                # u_ += 1
                break

            for i in range(1, self.M_rows - 1):
                for j in range(1, self.N_cols - 1):

                    # put current_strategy on top of memory list and pop the first element
                    cells_temp[i, j].memory.pop(0)
                    cells_temp[i, j].memory.append((cells_temp[i, j].strategy, cells_temp[i, j].k,
                                                    cells_temp[i, j].avg_payoff))

                    # select new strategy from memory
                    if cells_temp[i, j].change_strategy:
                        self.select_strategy(cells_temp[i, j])

                    # cell changing strategy counter
                    if cells_temp[i, j].strategy != cells[i, j].strategy:
                        change_strat_count_final += 1
                    else:
                        if (cells[i, j].strategy == 2 or cells[i, j].strategy == 3 or cells[
                            i, j].strategy == 4) and \
                                cells[i, j].k != cells_temp[i, j].k:
                            change_strat_count_final += 1


                    # mutate strategy
                    if self.p_strat_mut != 0:
                        x = random.random()
                        if x <= self.p_strat_mut:
                            self.mutate_strat(cells_temp[i, j])

                    # mutate state
                    if self.p_state_mut != 0:
                        x = random.random()
                        if x <= self.p_state_mut:
                            self.mutate_state(cells_temp, i, j)

                    # decide if in group of 1s or 0s
                    cells_temp[i, j].group_of_1s = self.is_group_of_1s(cells_temp, i, j)
                    if not cells_temp[i, j].group_of_1s:
                        cells_temp[i, j].group_of_0s = self.is_group_of_0s(cells_temp, i, j)

                    # mutation when in group of 1s or 0s
                    if cells_temp[i, j].group_of_0s:
                        if self.p_neigh_0_mut != 0:
                            x = random.random()
                            if x <= self.p_neigh_0_mut:
                                cells_temp[i, j].state = 1
                    elif cells_temp[i, j].group_of_1s:
                        if self.p_neigh_1_mut != 0:
                            x = random.random()
                            if x <= self.p_neigh_1_mut:
                                cells_temp[i, j].state = 0

            self.misc_stats.append((k + 1, change_strat_count, change_strat_count_final))
            self.cells.append((k + 1, cells_temp))
            if not self.is_multi_run:
                self.calculate_stats_for_graph(k)
                time.sleep(0.05)

        if not self.is_multi_run:
            self.calculate_stats_for_graph(k)
        self.statistics = self.calculate_statistics()
        if self.is_multi_run:
            print("process finished PID: %d" % os.getpid())
        else:
            print("thread finished")
            self.signal_finished.emit()




    def automaton_init(self):
        self.init_cells_memory()
        self.init_cells(self.cells[0][1], self.p_init_C)
        cells = self.cells[0][1]
        for i in range(1, self.M_rows - 1):
            for j in range(1, self.N_cols - 1):
                self.select_strategy(cells[i, j])


    def init_cells_memory(self):
        self.cells.append((0, self.create_CA(0.5, self.allC, self.allD, self.kD, self.kC, self.minK, self.maxK)))
        _, cells = self.cells[0]
        for k in range(self.h):
            if k > 0:
                self.init_cells(cells, 0.5)
            cells_temp = copy.deepcopy(cells)
            for i in range(1, self.M_rows - 1):
                for j in range(1, self.N_cols - 1):
                    self.update_cell_states(cells, cells_temp, i, j)
            for i in range(1, self.M_rows - 1):
                for j in range(1, self.N_cols - 1):
                    cells_temp[i, j].sum_payoff = 0
                    if self.is_payoff_1:
                        cells_temp[i, j].action = self.decide_action(cells_temp, i, j)
                        self.calculate_payoff_1(cells_temp, i, j)
                    else:
                        self.calculate_payoff_2(cells_temp, i, j)

                    cells[i, j].memory.append((cells_temp[i, j].strategy, cells_temp[i, j].k,
                                               cells_temp[i, j].avg_payoff))

    def init_cells(self, cells, p_init_C):
        self.init_states(cells, p_init_C)
        self.init_strategies(cells)

    def init_strategies(self, cells):
        b1 = self.allC
        b2 = self.allD + b1
        b3 = self.kD + b2
        b4 = self.kC + b3
        for i in range(1, self.M_rows - 1):
            for j in range(1, self.N_cols - 1):
                x = random.random()

                if x <= b1:
                    cells[i, j].strategy = 1
                    cells[i, j].k = -1
                elif x <= b2:
                    cells[i, j].strategy = 0
                    cells[i, j].k = -1
                elif x <= b3:
                    cells[i, j].strategy = 2
                    y = random.randint(self.minK, self.maxK)
                    cells[i, j].k = y
                elif x <= b4:
                    cells[i, j].strategy = 3
                    y = random.randint(self.minK, self.maxK)
                    cells[i, j].k = y
                else:
                    cells[i, j].strategy = 4
                    y = random.randint(self.minK, self.maxK)
                    cells[i, j].k = y

    def init_states(self, cells, p_init_C):
        for i in range(1, self.M_rows - 1):
            for j in range(1, self.N_cols - 1):
                x = random.random()
                if x <= p_init_C:
                    cells[i, j].state = 1
                else:
                    cells[i, j].state = 0

    def select_strategy(self, cell):
            x = random.random()
            if x <= self.epsilon:
                cell.strategy, cell.k = self.init_cell_strategy(self.allC, self.allD, self.kD,
                                                                self.kC, self.minK, self.maxK)
            else:
                strategy, k, max_payoff = cell.memory[0]
                for z in range(1, self.h):
                    strategy_temp, k_temp, payoff = cell.memory[z]
                    if payoff >= max_payoff:
                        strategy = strategy_temp
                        k = k_temp
                        max_payoff = payoff
                if self.min_payoff >= 0 and max_payoff <= self.min_payoff:
                    cell.strategy, cell.k = self.init_cell_strategy(self.allC, self.allD, self.kD,
                                                                    self.kC, self.minK, self.maxK)
                else:
                    cell.strategy = strategy
                    cell.k = k








