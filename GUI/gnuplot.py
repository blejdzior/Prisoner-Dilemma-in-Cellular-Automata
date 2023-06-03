from typing import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib as mpl
import numpy as np


class GnuplotCanvas(FigureCanvas):
    def __init__(self, MainWindow, x_len:int, y_range:List) -> None:
        super().__init__(mpl.figure.Figure())
        self.mainWindow = MainWindow

        # Set plot size
        self.resize(565, 170)
    
        # The x axis length
        self.x_len = x_len
        # The y axis length
        self.y_range = y_range

        self.x_list = list(range(0, x_len))
        # List of coordinates f_C
        self.y_list_f_C = [0] * x_len
        # List of coordinates f_C_corr
        self.y_list_f_C_corr = [0] * x_len
        # List of coordinates avg_payoff
        self.y_list_avg_payoff = [0] * x_len
        # List of coordinates f_strat_ch
        self.y_list_f_strat_ch = [0] * x_len

        # Store figures axes
        self.ax = self.figure.subplots()
        return

    def updateCanvas(self, f_C, f_C_corr, avg_payoff, f_strat_ch) -> None:
        self.ax.clear()

        self.y_list_f_C.append(f_C)
        self.y_list_f_C = self.y_list_f_C[-self.x_len:]
        self.ax.plot(self.x_list, self.y_list_f_C, label = "freq of 1s")
    
        self.y_list_f_C_corr.append(f_C_corr)
        self.y_list_f_C_corr = self.y_list_f_C_corr[-self.x_len:]
        self.ax.plot(self.x_list, self.y_list_f_C_corr, label = "freq of 1s correct")

        self.y_list_avg_payoff.append(avg_payoff)
        self.y_list_avg_payoff = self.y_list_avg_payoff[-self.x_len:]
        self.ax.plot(self.x_list, self.y_list_avg_payoff, label = "avg payoff")

        self.y_list_f_strat_ch.append(f_strat_ch)
        self.y_list_f_strat_ch = self.y_list_f_strat_ch[-self.x_len:]
        self.ax.plot(self.x_list, self.y_list_f_strat_ch, label = "freq of strat change")

        self.ax.set_ylim(ymin=self.y_range[0], ymax=self.y_range[1])
        self.ax.legend(fontsize="6")
        self.draw()
        return