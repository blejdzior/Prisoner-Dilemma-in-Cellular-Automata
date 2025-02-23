# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 12:30:18 2023

@author: pozdro
"""
# from PySide6.QtWidgets import QTableWidgetItem
import numpy as np
from queue import Queue
class Cell():
    def __init__(self, _id, x, y, strategy = -1, k = -1, action = -1, state = -1, group_of_1s = False, group_of_0s = False, change_strategy = False):
        super().__init__()
        super().__init_subclass__()

        # strategy of Cell - decides cell's state in next step of Cellular automata
        # 0 - all D - always defect (state = 0)
        # 1 - all C - always coperate (state = 1)
        # 2 - kD - cooperate until no more than K neighbours defect, otherwise defect
        # 3 - kC - cooperate until no more than K neighbours cooperate, otherwise defect
        # 4 - kDC - defect until not more than K neighbors defect, otherwise cooperate 
        self.strategy = strategy
        self.state = state
        self.k = k
        
        # action depends on cell's state and states of neighbours i.e. if cell's neighbourhood (including the cell) is correct
        # then action=1 (cooperate) otherwise action=0 (defect)
        self.action = action
        
        # coordinates in cellular automata
        self.x = x
        self.y = y
        # global ID
        self.id = _id

        self.group_of_1s = group_of_1s
        self.group_of_0s = group_of_0s
        self.change_strategy = change_strategy
        self.pay_to_send = 0
        self.pay_to_receive = 0
        self.winner_agent = -1

        # cell's payoff in game with each neighbour [0] - north neighbour, [1] - north-west, [2] - west, [3] - south-west,
        # [4] - south, [5] - south-east, [6] - east, [7] - north
        self.payoffs = np.empty(8, dtype=float)
        self.sum_payoff = 0
        self.avg_payoff = 0

        self.memory = []

    def copy(self, copy_to):
        # dict = [a for a in dir(self) if not a.startswith('__') ]
        # for attribute in dict:
        #     setattr(copy_to, attribute, getattr(self, attribute))
        copy_to.strategy = self.strategy
        copy_to.state = self.state
        copy_to.k = self.k
        copy_to.action = self.action
        copy_to.x = self.x
        copy_to.y = self.y
        copy_to.id = self.id
        copy_to.group_of_1s = self.group_of_1s
        copy_to.group_of_0s = self.group_of_0s
        copy_to.change_strategy = self.change_strategy
        copy_to.pay_to_send = self.pay_to_send
        copy_to.pay_to_receive = self.pay_to_receive
        copy_to.winner_agent = self.winner_agent
        copy_to.payoffs = self.payoffs.copy()
        copy_to.sum_payoff = self.sum_payoff
        copy_to.avg_payoff = self.avg_payoff
        copy_to.memory = self.memory.copy()


    def __deepcopy__(self, memodict={}):
        cell = Cell(self.id, self.x, self.y, self.strategy, self.k, self.action, self.state, self.group_of_1s, self.group_of_0s,
                    self.change_strategy)
        cell.avg_payoff = self.avg_payoff
        cell.sum_payoff = self.sum_payoff
        cell.memory = self.memory
        return cell

    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

        
