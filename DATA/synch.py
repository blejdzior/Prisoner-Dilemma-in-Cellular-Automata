class Synch:
    def __init__(self, synch_prob, optimal_num_1s, u, is_payoff_1):
        self.synch_prob = synch_prob
        self.optimal_num_1s = optimal_num_1s
        self.u = u
        self.is_payoff_1 = is_payoff_1
        self.is_payoff_2 = False
        if not self.is_payoff_1:
            self.is_payoff_2 = True
