class Canvas:
    def __init__(self, rows, cols, p_init_C, isSharing, is_LA, memory_h, epsilon, min_payoff):
        self.rows = rows + 2
        self.cols = cols + 2
        self.p_init_C = p_init_C
        self.isSharing = isSharing
        self.is_LA = is_LA
        self.memory_h = memory_h
        self.epsilon = epsilon
        self.min_payoff = min_payoff
