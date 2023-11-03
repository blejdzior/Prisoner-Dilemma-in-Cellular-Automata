# Learning automaton
from algorithm.CA import CA
class LA(CA):
    def __init__(self, M_rows, N_cols, p_init_C, allC, allD, kD, kC, minK, maxK, num_of_iter,
                 payoff_C_C, payoff_C_D, payoff_D_C, payoff_D_D, is_sharing, synch_prob,
                 is_tournament, p_state_mut, p_strat_mut, p_0_neigh_mut, p_1_neigh_mut, is_debug, is_test1, is_test2,
                 f, optimal_num1s, is_payoff_1, u, memory_h, epsilon, is_multi_run=False, seed=None):
        # Parent class init
        CA.__init__(self, M_rows, N_cols, p_init_C, allC, allD, kD, kC, minK, maxK, num_of_iter,
                 payoff_C_C, payoff_C_D, payoff_D_C, payoff_D_D, is_sharing, synch_prob,
                 is_tournament, p_state_mut, p_strat_mut, p_0_neigh_mut, p_1_neigh_mut, is_debug, is_test1, is_test2,
                 f, optimal_num1s, is_payoff_1, u, is_multi_run, seed, is_LA=True)

        # Depth of cells memory
        self.h = memory_h
        # Chance that strategy will be assigned randomly to a cell
        self.epsilon = epsilon


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

    def automaton_init(self):
        self.init_cells_memory()


    def init_cells_memory(self):
        for i in range(self.h):
            cells = self.create_CA(0.5, self.allC, self.allD, self.kD, self.kC, self.minK, self.maxK)


