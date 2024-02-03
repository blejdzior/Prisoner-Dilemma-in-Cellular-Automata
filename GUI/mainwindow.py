# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 10:35:46 2023

@author: pozdro
"""
import datetime
import math
import time
import asyncio
import timeit

from PySide6.QtWidgets import (QMainWindow, QTableWidgetItem, QMessageBox, QGraphicsScene)
from PySide6.QtGui import (QColor, QPixmap)
from PySide6.QtCore import (QRect, QThreadPool, QMutex, Slot, Signal, QThread)
from GUI.ui_mainwindow import Ui_MainWindow
from PySide6.QtGui import (QBrush, QGradient, QRadialGradient)


from DATA.canvas import Canvas
from DATA.competition import Competition
from DATA.debugger import Debugger
from DATA.iterations import Iterations
from DATA.mutation import Mutation
from DATA.myData import MyData
from DATA.seed import Seed
from DATA.strategies import Strategies
from DATA.synch import Synch
from DATA.payoff import Payoff

from algorithm.CA import CA
from algorithm.LA import LA
from GUI.animation import Animation
from algorithm.CAQT import CAQT

from GUI.gnuplot import GnuplotCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from algorithm.StatisticsMultirun import StatisticsMultirun
import multiprocessing

import os
from pathlib import Path
from concurrent.futures.process import ProcessPoolExecutor

from memory_profiler import profile


class MainWindow(QMainWindow):
    anim_start_signal = Signal()
    automata_start_signal = Signal()
    def __init__(self):
        super().__init__()
        self.is_multi_run = None
        self.automata = None
        self.automata_multirun = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.isAnimationRunning = False
        self.visualization_mode = 0

        # colors for state coloring, each for CA/LA, and payoff function.
        self.red = QColor(240, 7, 35)
        self.blue = QColor(7, 7, 240)
        self.green = QColor(18, 191, 15)
        self.orange = QColor(255, 100, 0)
        self.color = None

        self.animation = Animation(0, 0, 0)
        self.animation.signal.connect(self.animation_signal_handler)
        self.animation.signal.connect(self.update_graph)
        self.anim_start_signal.connect(self.animation.run)

        self.animation_thread = QThread()
        self.animation.moveToThread(self.animation_thread)
        self.animation.signalFinished.connect(self.animation_thread.quit)
        self.animation_thread.finished.connect(self.isRunning_false)

        self.pool = ProcessPoolExecutor(max_tasks_per_child=1)
        self.automata_thread = QThread()


        # self.animation.signal.connect(self.update_graph)

    def resetIterations(self):
        print("Reset iteracji")
        self.ui.spinBox_num_of_iter.value = 0

    def displayDataWarning(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Can't process DATA.\nThe DATA entered is incorrect.")
        msg.setWindowTitle("Invalid input")
        msg.exec_()

    def selectVisualizationMode(self, mode):
        match mode:
            case 0:
                self.state_color_handler()
            case 1:
                self.strategies_color_handler()
            case 2:
                self.kD_strategies_color_handler()
            case 3:
                self.kC_strategies_color_handler()
            case 4:
                self.kDC_strategies_color_handler()
            case 5:
                self.action_color_handler()

    def savedImagesMessage(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Images saved.")
        msg.setWindowTitle("Done!")
        msg.exec_()

    def saveImage(self):
        currentMode = self.visualization_mode
        for mode in range(6):
            self.selectVisualizationMode(mode)
            pixmap = QPixmap(self.ui.graphicsView_CA.size())
            self.ui.graphicsView_CA.render(pixmap)
            if not os.path.exists('IMAGES'):
                os.makedirs('IMAGES')
            fileName = "IMAGES//image" + str(self.ui.lcdNumber_iters.value()) + str(self.visualization_mode) + ".png"
            pixmap.save(fileName, "PNG", -1)
        self.selectVisualizationMode(currentMode)
        self.savedImagesMessage()


    def changeCellsColor(self, selected, R, G, B, opacity=255):
        for ix in selected:
            row, column = ix
            self.ui.graphicsView_CA.item(row, column).setBackground(QColor(R,G,B, opacity))

    def changeCellsColor_QColor(self, selected, color):
        for ix in selected:
            row, column = ix
            self.ui.graphicsView_CA.item(row, column).setBackground(color)

    def roundDivision(self, size, n):
        floor = math.floor(size / n)
        roof = math.ceil(size / n)
        floorDif = abs(size - floor * n)
        roofDif = abs(size - roof * n)
        if floorDif < roofDif:
            return floor
        else:
            return roof

    def create_automata(self):
        rows = self.data.canvas.rows
        cols = self.data.canvas.cols
        if self.seed.isCustomSeed:
            seed = self.seed.customSeed
        else:
            seed = None
        if not self.canvas.is_LA:
             self.automata = CA(rows, cols, self.data.canvas.p_init_C, self.data.strategies.all_C,
                           self.data.strategies.all_D, self.data.strategies.k_D, self.data.strategies.k_C,
                           self.data.strategies.k_var_min, self.data.strategies.k_var_max,
                           self.data.iterations.num_of_iter,
                           self.data.payoff.d, self.data.payoff.c, self.data.payoff.b, self.data.payoff.a,
                           self.canvas.isSharing,
                           self.data.synch.synch_prob, self.data.competition.isTournament,
                           self.data.mutations.p_state_mut,
                           self.data.mutations.p_strat_mut, self.data.mutations.p_0_neighb_mut,
                           self.data.mutations.p_1_neighb_mut,
                           self.data.debugger.isDebug, self.data.debugger.is_test1, self.data.debugger.is_test2, self.f,
                           self.data.synch.optimal_num_1s, self.data.synch.is_payoff_1, self.data.synch.u, self.is_multi_run,
                           seed)
        else:
            self.automata = LA(rows, cols, self.data.canvas.p_init_C, self.data.strategies.all_C,
                               self.data.strategies.all_D, self.data.strategies.k_D, self.data.strategies.k_C,
                               self.data.strategies.k_var_min, self.data.strategies.k_var_max,
                               self.data.iterations.num_of_iter,
                               self.data.payoff.d, self.data.payoff.c, self.data.payoff.b, self.data.payoff.a,
                               self.canvas.isSharing,
                               self.data.synch.synch_prob, self.data.competition.isTournament,
                               self.data.mutations.p_state_mut,
                               self.data.mutations.p_strat_mut, self.data.mutations.p_0_neighb_mut,
                               self.data.mutations.p_1_neighb_mut,
                               self.data.debugger.isDebug, self.data.debugger.is_test1, self.data.debugger.is_test2,
                               self.f,
                               self.data.synch.optimal_num_1s, self.data.synch.is_payoff_1, self.data.synch.u,
                               self.canvas.memory_h, self.canvas.epsilon, self.canvas.min_payoff,
                               self.is_multi_run,
                               seed)

        self.automata.moveToThread(self.automata_thread)
        self.automata.signal.connect(self.update_graph_async)

        self.automata_start_signal.connect(self.automata.evolution)

        self.automata.signal_finished.connect(self.automata_thread.quit)
        self.automata.signal_finished.connect(self.create_coloring)
        self.automata.signal_finished.connect(self.save_results)

    def create_automata_multirun(self):
        rows = self.data.canvas.rows
        cols = self.data.canvas.cols
        if self.seed.isCustomSeed:
            seed = self.seed.customSeed
        else:
            seed = None
        # self.pool = multiprocessing.Pool(maxtasksperchild=1)
        self.result = []
        for i in range(self.data.iterations.num_of_exper):
            self.result.append(self.pool.submit(run_process, rows, cols, self.data.canvas.p_init_C, self.data.strategies.all_C,
                            self.data.strategies.all_D, self.data.strategies.k_D, self.data.strategies.k_C,
                            self.data.strategies.k_var_min, self.data.strategies.k_var_max,
                            self.data.iterations.num_of_iter,
                            self.data.payoff.d, self.data.payoff.c, self.data.payoff.b, self.data.payoff.a,
                            self.canvas.isSharing,
                            self.data.synch.synch_prob, self.data.competition.isTournament,
                            self.data.mutations.p_state_mut,
                            self.data.mutations.p_strat_mut, self.data.mutations.p_0_neighb_mut,
                            self.data.mutations.p_1_neighb_mut,
                            self.data.debugger.isDebug, self.data.debugger.is_test1, self.data.debugger.is_test2, 1,
                            self.data.synch.optimal_num_1s, self.data.synch.is_payoff_1, self.data.synch.u, self.is_multi_run,
                            seed, self.canvas.is_LA, self.canvas.memory_h, self.canvas.epsilon, self.canvas.min_payoff))
        #
        # self.result = self.pool.map(run_process, rows, cols, self.data.canvas.p_init_C, self.data.strategies.all_C,
        #                                       self.data.strategies.all_D, self.data.strategies.k_D, self.data.strategies.k_C,
        #                                       self.data.strategies.k_var_min, self.data.strategies.k_var_max,
        #                                       self.data.iterations.num_of_iter,
        #                                       self.data.payoff.d, self.data.payoff.c, self.data.payoff.b, self.data.payoff.a,
        #                                       self.canvas.isSharing,
        #                                       self.data.synch.synch_prob, self.data.competition.isTournament,
        #                                       self.data.mutations.p_state_mut,
        #                                       self.data.mutations.p_strat_mut, self.data.mutations.p_0_neighb_mut,
        #                                       self.data.mutations.p_1_neighb_mut,
        #                                       self.data.debugger.isDebug, self.data.debugger.is_test1, self.data.debugger.is_test2, 1,
        #                                       self.data.synch.optimal_num_1s, self.data.synch.is_payoff_1, self.data.synch.u,
        #                                       self.is_multi_run,
        #                                       seed, self.canvas.is_LA, self.canvas.memory_h, self.canvas.epsilon,
        #                                       self.canvas.min_payoff))

    def createTableCA(self):
        rows = self.data.canvas.rows
        cols = self.data.canvas.cols
        self.ui.graphicsView_CA.setRowCount(rows)
        self.ui.graphicsView_CA.setColumnCount(cols)
        self.f = open("RESULTS//outputs.txt", "w")
        # if self.data.iterations.num_of_exper > 1:
        if self.data.iterations.num_of_exper == 1:
            self.is_multi_run = False
        else:
            self.is_multi_run = True
        if self.is_multi_run:
            self.create_automata_multirun()
            self.automata = self.result[0].result()
        else:
             self.create_automata()
        if self.canvas.is_LA:
            if self.synch.is_payoff_1:
                self.color = self.orange
            else:
                self.color = self.green
        else:
            if self.synch.is_payoff_1:
                self.color = self.red
            else:
                self.color = self.blue

        k, cells = self.automata.cells[0]
        for n in range(rows):
            for m in range(cols):
                self.ui.graphicsView_CA.setItem(n, m, QTableWidgetItem())
                if cells[n, m].state == 1:
                        self.ui.graphicsView_CA.item(n, m).setBackground(self.color)
        cellWidth = self.roundDivision(300, cols)
        cellHeight = self.roundDivision(300, rows)
        width = cellWidth * cols + 2
        height = cellHeight * rows + 2
        self.ui.graphicsView_CA.setGeometry(QRect(540, 80, width, height))
        self.ui.graphicsView_CA.horizontalHeader().setDefaultSectionSize(cellWidth)
        self.ui.graphicsView_CA.verticalHeader().setDefaultSectionSize(cellHeight)
        self.ui.pushButton_start_anim.setDisabled(True)

        if not self.is_multi_run:
            self.automata_thread.start()
            self.automata_start_signal.emit()



    def create_coloring(self):
        self.coloring_state = []
        self.coloring_allC = []
        self.coloring_allD = []
        self.coloring_kD = []
        self.coloring_kC = []
        self.coloring_kDC = []

        self.coloring_kD_0 = []
        self.coloring_kD_1 = []
        self.coloring_kD_2 = []
        self.coloring_kD_3 = []
        self.coloring_kD_4 = []
        self.coloring_kD_5 = []
        self.coloring_kD_6 = []
        self.coloring_kD_7 = []
        self.coloring_kD_8 = []

        self.coloring_kC_0 = []
        self.coloring_kC_1 = []
        self.coloring_kC_2 = []
        self.coloring_kC_3 = []
        self.coloring_kC_4 = []
        self.coloring_kC_5 = []
        self.coloring_kC_6 = []
        self.coloring_kC_7 = []
        self.coloring_kC_8 = []

        self.coloring_kDC_0 = []
        self.coloring_kDC_1 = []
        self.coloring_kDC_2 = []
        self.coloring_kDC_3 = []
        self.coloring_kDC_4 = []
        self.coloring_kDC_5 = []
        self.coloring_kDC_6 = []
        self.coloring_kDC_7 = []
        self.coloring_kDC_8 = []
        self.coloring_actions = []

        rows = self.data.canvas.rows
        cols = self.data.canvas.cols

        for iter, cells in self.automata.cells:

            coloring_state_temp = []
            coloring_allD_temp = []
            coloring_allC_temp = []
            coloring_kD_temp = []
            coloring_kC_temp = []
            coloring_kDC_temp = []
            coloring_kD_0_temp = []
            coloring_kD_1_temp = []
            coloring_kD_2_temp = []
            coloring_kD_3_temp = []
            coloring_kD_4_temp = []
            coloring_kD_5_temp = []
            coloring_kD_6_temp = []
            coloring_kD_7_temp = []
            coloring_kD_8_temp = []
            coloring_kC_0_temp = []
            coloring_kC_1_temp = []
            coloring_kC_2_temp = []
            coloring_kC_3_temp = []
            coloring_kC_4_temp = []
            coloring_kC_5_temp = []
            coloring_kC_6_temp = []
            coloring_kC_7_temp = []
            coloring_kC_8_temp = []
            coloring_kDC_0_temp = []
            coloring_kDC_1_temp = []
            coloring_kDC_2_temp = []
            coloring_kDC_3_temp = []
            coloring_kDC_4_temp = []
            coloring_kDC_5_temp = []
            coloring_kDC_6_temp = []
            coloring_kDC_7_temp = []
            coloring_kDC_8_temp = []
            coloring_actions_temp = []
            for i in range(rows):
                for j in range(cols):
                    # state coloring
                    if cells[i, j].state == 1:
                        coloring_state_temp.append((i, j))
                        # all D
                    if cells[i, j].strategy == 0:
                        coloring_allD_temp.append((i, j))
                        # all C
                    elif cells[i, j].strategy == 1:
                        coloring_allC_temp.append((i, j))
                        # kD
                    elif cells[i, j].strategy == 2:
                        coloring_kD_temp.append((i, j))
                        if cells[i, j].k == 0:
                            coloring_kD_0_temp.append((i, j))
                        elif cells[i, j].k == 1:
                            coloring_kD_1_temp.append((i, j))
                        elif cells[i, j].k == 2:
                            coloring_kD_2_temp.append((i, j))
                        elif cells[i, j].k == 3:
                            coloring_kD_3_temp.append((i, j))
                        elif cells[i, j].k == 4:
                            coloring_kD_4_temp.append((i, j))
                        elif cells[i, j].k == 5:
                            coloring_kD_5_temp.append((i, j))
                        elif cells[i, j].k == 6:
                            coloring_kD_6_temp.append((i, j))
                        elif cells[i, j].k == 7:
                            coloring_kD_7_temp.append((i, j))
                        elif cells[i, j].k == 8:
                            coloring_kD_8_temp.append((i, j))
                        # kC
                    elif cells[i, j].strategy == 3:
                        coloring_kC_temp.append((i, j))
                        if cells[i, j].k == 0:
                            coloring_kC_0_temp.append((i, j))
                        elif cells[i, j].k == 1:
                            coloring_kC_1_temp.append((i, j))
                        elif cells[i, j].k == 2:
                            coloring_kC_2_temp.append((i, j))
                        elif cells[i, j].k == 3:
                            coloring_kC_3_temp.append((i, j))
                        elif cells[i, j].k == 4:
                            coloring_kC_4_temp.append((i, j))
                        elif cells[i, j].k == 5:
                            coloring_kC_5_temp.append((i, j))
                        elif cells[i, j].k == 6:
                            coloring_kC_6_temp.append((i, j))
                        elif cells[i, j].k == 7:
                            coloring_kC_7_temp.append((i, j))
                        elif cells[i, j].k == 8:
                            coloring_kC_8_temp.append((i, j))
                        # kDC
                    elif cells[i, j].strategy == 4:
                        coloring_kDC_temp.append((i, j))
                        if cells[i, j].k == 0:
                            coloring_kDC_0_temp.append((i, j))
                        elif cells[i, j].k == 1:
                            coloring_kDC_1_temp.append((i, j))
                        elif cells[i, j].k == 2:
                            coloring_kDC_2_temp.append((i, j))
                        elif cells[i, j].k == 3:
                            coloring_kDC_3_temp.append((i, j))
                        elif cells[i, j].k == 4:
                            coloring_kDC_4_temp.append((i, j))
                        elif cells[i, j].k == 5:
                            coloring_kDC_5_temp.append((i, j))
                        elif cells[i, j].k == 6:
                            coloring_kDC_6_temp.append((i, j))
                        elif cells[i, j].k == 7:
                            coloring_kDC_7_temp.append((i, j))
                        elif cells[i, j].k == 8:
                            coloring_kDC_8_temp.append((i, j))
                    if cells[i, j].action == 1:
                        coloring_actions_temp.append((i, j))

            self.coloring_state.append(coloring_state_temp)
            self.coloring_allC.append(coloring_allC_temp)
            self.coloring_allD.append(coloring_allD_temp)
            self.coloring_kD.append(coloring_kD_temp)
            self.coloring_kC.append(coloring_kC_temp)
            self.coloring_kDC.append(coloring_kDC_temp)
            self.coloring_kD_0.append(coloring_kD_0_temp)
            self.coloring_kD_1.append(coloring_kD_1_temp)
            self.coloring_kD_2.append(coloring_kD_2_temp)
            self.coloring_kD_3.append(coloring_kD_3_temp)
            self.coloring_kD_4.append( coloring_kD_4_temp)
            self.coloring_kD_5.append(coloring_kD_5_temp)
            self.coloring_kD_6.append(coloring_kD_6_temp)
            self.coloring_kD_7.append(coloring_kD_7_temp)
            self.coloring_kD_8.append(coloring_kD_8_temp)
            self.coloring_kC_0.append(coloring_kC_0_temp)
            self.coloring_kC_1.append(coloring_kC_1_temp)
            self.coloring_kC_2.append(coloring_kC_2_temp)
            self.coloring_kC_3.append(coloring_kC_3_temp)
            self.coloring_kC_4.append(coloring_kC_4_temp)
            self.coloring_kC_5.append(coloring_kC_5_temp)
            self.coloring_kC_6.append(coloring_kC_6_temp)
            self.coloring_kC_7.append(coloring_kC_7_temp)
            self.coloring_kC_8.append(coloring_kC_8_temp)
            self.coloring_kDC_0.append(coloring_kDC_0_temp)
            self.coloring_kDC_1.append(coloring_kDC_1_temp)
            self.coloring_kDC_2.append(coloring_kDC_2_temp)
            self.coloring_kDC_3.append(coloring_kDC_3_temp)
            self.coloring_kDC_4.append(coloring_kDC_4_temp)
            self.coloring_kDC_5.append(coloring_kDC_5_temp)
            self.coloring_kDC_6.append(coloring_kDC_6_temp)
            self.coloring_kDC_7.append(coloring_kDC_7_temp)
            self.coloring_kDC_8.append(coloring_kDC_8_temp)
            self.coloring_actions.append(coloring_actions_temp)


    def setData(self):
        self.data = MyData(self.canvas, self.competition, self.debugger,
                         self.iterations, self.mutation, self.seed,
                         self.strategies, self.synch, self.payoff)
        self.createTableCA()

    def closeRunningThreads(self):
        # Terminating running threads
        if self.isAnimationRunning == True:
            if self.animation.stillRunning():
                self.animation.terminate()
            self.isAnimationRunning = False
            self.ui.spinBox_iters.setValue(0)

    def startSimulation(self):
        self.start = time.time()
        self.ui.disableStartButton()

        self.closeRunningThreads()

        #Tutaj należy sprawdzić wszystkie wprowadzone dane zanim zostaną one przekazane dalej
        allC = self.ui.doubleSpinBox_allC.value()
        allD = self.ui.doubleSpinBox_allD.value()
        kD = self.ui.doubleSpinBox_kD.value()
        kC = self.ui.doubleSpinBox_kC.value()
        kDC = self.ui.doubleSpinBox_kDC.value()
        strategySum = allC + allD + kD + kC + kDC
        if strategySum != 1:
            self.displayDataWarning()
            return
        if self.ui.checkBox_min_payoff.isChecked():
            min_payoff = self.ui.spinBox_min_payoff.value()
        else:
            min_payoff = -1
        self.canvas = Canvas(self.ui.spinBox_Mrows.value(),
                            self.ui.spinBox_Ncols.value(),
                            self.ui.doubleSpinBox_p_init_C.value(),
                            self.ui.checkBox_sharing.isChecked(),
                            self.ui.checkBox_LA.isChecked(),
                            self.ui.spinBox_memoryh.value(),
                            self.ui.spinBox_epsilon.value(),
                            min_payoff)

        self.competition = Competition(self.ui.radioButton_roulette.isChecked(),
                                        self.ui.radioButton_tournament.isChecked())

        self.debugger = Debugger(self.ui.radioButton_debug.isChecked(),
                                    self.ui.radioButton_CA_state.isChecked(),
                                    self.ui.radioButton_CA_strat.isChecked(),
                                 self.ui.radioButton_test1.isChecked(), self.ui.radioButton_test2.isChecked(),
                                 self.ui.radioButton_test3.isChecked())

        self.iterations = Iterations(self.ui.spinBox_num_of_iter.value(),
                                        self.ui.spinBox_num_of_exper.value())

        self.mutation = Mutation(self.ui.doubleSpinBox_p_state_mut.value(),
                                    self.ui.doubleSpinBox_p_strat_mut.value(),
                                    self.ui.doubleSpinBox_p_0_neigh_mut.value(),
                                    self.ui.doubleSpinBox_p_1_neigh_mut.value())

        self.seed = Seed(self.ui.radioButton_clock.isChecked(),
                            self.ui.radioButton_custom.isChecked(),
                            self.ui.spinBox_custom_seed.value())

        self.synch = Synch(self.ui.doubleSpinBox_synch_prob.value(),
                            self.ui.spinBox_optimal_num_1s.value(), self.ui.spinBox_u.value(),
                           self.ui.radiobutton_pay_fun_1.isChecked())

        self.strategies = Strategies(self.ui.doubleSpinBox_allC.value(),
                                        self.ui.doubleSpinBox_allD.value(),
                                        self.ui.doubleSpinBox_kD.value(),
                                        self.ui.doubleSpinBox_kC.value(),
                                        self.ui.doubleSpinBox_kDC.value(),
                                        self.ui.spinBox_kMin.value(),
                                        self.ui.spinBox_kMax.value())

        self.payoff = Payoff(self.ui.doubleSpinBox_a.value(),
                             self.ui.doubleSpinBox_b.value(),
                             self.ui.doubleSpinBox_c.value(),
                             self.ui.doubleSpinBox_d.value())
        self.ui.spinBox_iters.setMaximum(self.iterations.num_of_iter-1)
        self.visualization_mode = 0  # state visualization
        self.create_graph()
        self.setData()

        self.ui.pushButton_states.setDisabled(0)
        self.ui.pushButton_strategies.setDisabled(0)
        self.ui.pushButton_kD.setDisabled(0)
        self.ui.pushButton_kC.setDisabled(0)
        self.ui.pushButton_kDC.setDisabled(0)
        self.ui.pushButton_actions.setDisabled(0)
        self.ui.pushButton_states.setDisabled(0)
        if self.is_multi_run:
            self.create_coloring()
            self.save_results()

        # self.simulationDoneMessage()
        # self.enableStartButton()
    def calculate_exec_time(self):
        print(self.end - self.start)
    def state_color_handler(self):
        rows = self.data.canvas.rows
        cols = self.data.canvas.cols
        iter = self.ui.spinBox_iters.value()

        for i in range(rows):
            for j in range(cols):
                self.ui.graphicsView_CA.item(i, j).setBackground(QColor(255, 255, 255, 255))

        # self.changeCellsColor(self.coloring_state[iter], 255, 100, 0)
        self.changeCellsColor_QColor(self.coloring_state[iter], self.color)
        self.visualization_mode = 0


    def strategies_color_handler(self):
        # if self.isAnimationRunning == True:
        #     self.animation.extendSleepTime()

        rows = self.data.canvas.rows
        cols = self.data.canvas.cols
        iter = self.ui.spinBox_iters.value()

        for i in range(rows):
            for j in range(cols):
                self.ui.graphicsView_CA.item(i, j).setBackground(QColor(255, 255, 255, 255))

        self.changeCellsColor(self.coloring_allC[iter], 255, 100, 0)  # red
        self.changeCellsColor(self.coloring_allD[iter], 0, 0, 255)  # blue
        self.changeCellsColor(self.coloring_kD[iter], 0, 128, 0)  # green
        self.changeCellsColor(self.coloring_kC[iter], 0, 255, 255)  # cyan
        self.changeCellsColor(self.coloring_kDC[iter], 255, 20, 147)  # pink
        self.visualization_mode = 1

    def kD_strategies_color_handler(self):
        # if self.isAnimationRunning == True:
        #     self.animation.extendSleepTime()

        rows = self.data.canvas.rows
        cols = self.data.canvas.cols
        iter = self.ui.spinBox_iters.value()

        for i in range(rows):
            for j in range(cols):
                self.ui.graphicsView_CA.item(i, j).setBackground(QColor(0, 0, 0, 255))

        self.changeCellsColor(self.coloring_kD_0[iter], 0, 128, 0, 0)
        self.changeCellsColor(self.coloring_kD_1[iter], 0, 128, 0, 31)
        self.changeCellsColor(self.coloring_kD_2[iter], 0, 128, 0, 62)
        self.changeCellsColor(self.coloring_kD_3[iter], 0, 128, 0, 93)
        self.changeCellsColor(self.coloring_kD_4[iter], 0, 128, 0, 124)
        self.changeCellsColor(self.coloring_kD_5[iter], 0, 128, 0, 156)
        self.changeCellsColor(self.coloring_kD_6[iter], 0, 128, 0, 187)
        self.changeCellsColor(self.coloring_kD_7[iter], 0, 128, 0, 218)
        self.changeCellsColor(self.coloring_kD_8[iter], 0, 128, 0, 255)

        self.visualization_mode = 2

    def kC_strategies_color_handler(self):
        # if self.isAnimationRunning == True:
        #     self.animation.extendSleepTime()

        rows = self.data.canvas.rows
        cols = self.data.canvas.cols
        iter = self.ui.spinBox_iters.value()

        for i in range(rows):
            for j in range(cols):
                self.ui.graphicsView_CA.item(i, j).setBackground(QColor(0, 0, 0, 200))

        self.changeCellsColor(self.coloring_kC_0[iter], 0, 255, 255, 0)
        self.changeCellsColor(self.coloring_kC_1[iter], 0, 255, 255, 31)
        self.changeCellsColor(self.coloring_kC_2[iter], 0, 255, 255, 62)
        self.changeCellsColor(self.coloring_kC_3[iter], 0, 255, 255, 93)
        self.changeCellsColor(self.coloring_kC_4[iter], 0, 255, 255, 124)
        self.changeCellsColor(self.coloring_kC_5[iter], 0, 255, 255, 156)
        self.changeCellsColor(self.coloring_kC_6[iter], 0, 255, 255, 187)
        self.changeCellsColor(self.coloring_kC_7[iter], 0, 255, 255, 218)
        self.changeCellsColor(self.coloring_kC_8[iter], 0, 255, 255, 255)

        self.visualization_mode = 3

    def kDC_strategies_color_handler(self):
        # if self.isAnimationRunning == True:
        #     self.animation.extendSleepTime()

        rows = self.data.canvas.rows
        cols = self.data.canvas.cols
        iter = self.ui.spinBox_iters.value()

        for i in range(rows):
            for j in range(cols):
                self.ui.graphicsView_CA.item(i, j).setBackground(QColor(0, 0, 0, 200))

        self.changeCellsColor(self.coloring_kDC_0[iter], 255, 20, 147, 0)
        self.changeCellsColor(self.coloring_kDC_1[iter], 255, 20, 147, 31)
        self.changeCellsColor(self.coloring_kDC_2[iter], 255, 20, 147, 62)
        self.changeCellsColor(self.coloring_kDC_3[iter], 255, 20, 147, 93)
        self.changeCellsColor(self.coloring_kDC_4[iter], 255, 20, 147, 124)
        self.changeCellsColor(self.coloring_kDC_5[iter], 255, 20, 147, 156)
        self.changeCellsColor(self.coloring_kDC_6[iter], 255, 20, 147, 187)
        self.changeCellsColor(self.coloring_kDC_7[iter], 255, 20, 147, 218)
        self.changeCellsColor(self.coloring_kDC_8[iter], 255, 20, 147, 255)

        self.visualization_mode = 4

    def action_color_handler(self):
        rows = self.data.canvas.rows
        cols = self.data.canvas.cols
        iter = self.ui.spinBox_iters.value()
        for i in range(rows):
            for j in range(cols):
                self.ui.graphicsView_CA.item(i, j).setBackground(QColor(0, 0, 255, 255))
        self.changeCellsColor(self.coloring_actions[iter], 255, 100, 0)
        self.visualization_mode = 5

    def save_parameters(self, f):
        f.write("#num_of_iter: " + str(self.data.iterations.num_of_iter))
        f.write("\n#num_of_exper: " + str(self.data.iterations.num_of_exper))
        f.write("\n#rows: " + str(self.data.canvas.rows - 2))
        f.write("\n#cols: " + str(self.data.canvas.cols - 2))
        f.write("\n#p_init_C: " + str(self.data.canvas.p_init_C))
        f.write("\n#p_state_mut: " + str(self.data.mutations.p_state_mut))
        f.write("\n#p_strat_mut: " + str(self.data.mutations.p_strat_mut))
        f.write("\n#p_0_neighb: " + str(self.data.mutations.p_0_neighb_mut))
        f.write("\n#p_1_neighb: " + str(self.data.mutations.p_1_neighb_mut))
        if(self.data.competition.isRoulette):
            f.write("\n#comp_type: roulette")
        elif(self.data.competition.isTournament):
            f.write("\n#comp_type: tournament")
        else:
            f.write("\n#comp_type: None?")

        f.write("\n#sharing: " + str(self.data.canvas.isSharing))
        f.write("\n#allC: " + str(self.data.strategies.all_C))
        f.write("\n#allD: " + str(self.data.strategies.all_D))
        f.write("\n#kD: " + str(self.data.strategies.k_D))
        f.write("\n#kC: " + str(self.data.strategies.k_C))
        f.write("\n#kDC: " + str(self.data.strategies.k_DC))
        f.write("\n#k_values: " + str(self.data.strategies.k_var_min) + " to " + str(self.data.strategies.k_var_max))
        f.write("\n#synchronity_prob: " + str(self.data.synch.synch_prob))
        f.write("\n#optimal_num_of_1s: " + str(self.data.synch.optimal_num_1s))
        f.write("\n#playerC_opponentD_payoff: " + str(self.data.payoff.c))
        f.write("\n#playerC_opponentC_payoff: " + str(self.data.payoff.d))
        f.write("\n#playerD_opponentD_payoff: " + str(self.data.payoff.a))
        f.write("\n#playerD_opponentC_payoff: " + str(self.data.payoff.b))
        f.write("\n#debug:  " + str(self.data.debugger.isDebug))
        f.write("\n#pay_off_1: " + str(self.data.synch.is_payoff_1))
        f.write("\n#pay_off_2: " + str(self.data.synch.is_payoff_2))
        f.write("\n#u: " + str(self.data.synch.u))
        if self.canvas.is_LA:
            f.write("\n#epsilon: " + str(self.canvas.epsilon))
            f.write("\n#h: " + str(self.canvas.memory_h))
            if self.canvas.min_payoff >= 0:
                f.write("\n#min_payoff: " + str(self.canvas.min_payoff))

    def save_results(self):
        f = open("RESULTS//results_a.txt", "w")
        f2 = open("RESULTS//results_b.txt", "w")
        f3 = open("m-RESULTS//m_results_a.txt", "w")
        f4 = open("m-RESULTS//max_f_C_corr.txt", "w")



        if not self.is_multi_run:
            self.save_parameters(f)
            self.save_parameters(f2)
        if self.is_multi_run:
            self.save_parameters(f3)
            self.save_parameters(f4)

        if self.is_multi_run:
            stats_multirun = []
            self.automata_multirun = []
            for result in self.result:
                self.automata_multirun.append((result.result().seed, result.result().statistics))
                del result

            # self.pool.close()
            # self.pool.join()

        for i in range(self.data.iterations.num_of_exper):
            if self.is_multi_run:
                self.automata = self.automata_multirun[i]
            else:
                self.automata = (self.automata.seed, self.automata.statistics)

            if self.is_multi_run:
                f3.write("\n\n\n#Experiment: " + str(i))
                f3.write("\n\n#seed: " + str(self.automata[0]) + "")
                f3.write("\n{0:10}{1:13}{2:18}{3:16}{4:16}{5:16}".format("#iter", "f_C", "f_C_corr", "av_sum", "f_allC",
                                                                        "f_allD"))
                f3.write(
                    "{0:14}{1:14}{2:15}{3:20}{4:26}".format("f_kD", "f_kC", "f_kDC", "f_strat_ch", "f_strat_ch_final"))
                f3.write("{0:17}{1:17}{2:21}\n".format("f_cr_0s", "f_cr_1s", "optim_solut"))

                f4.write("\n\n\n#Experiment: " + str(i))
                f4.write("\n\n#seed: " + str(self.automata[0]) + "")
                f4.write("\n{0:10}{1:13}{2:18}{3:16}{4:16}{5:16}".format("#iter", "f_C", "f_C_corr", "av_sum", "f_allC",
                                                                        "f_allD"))
                f4.write(
                    "{0:14}{1:14}{2:15}{3:20}{4:26}".format("f_kD", "f_kC", "f_kDC", "f_strat_ch", "f_strat_ch_final"))
                f4.write("{0:17}{1:17}{2:21}\n".format("f_cr_0s", "f_cr_1s", "optim_solut"))


            if not self.is_multi_run:
                # result-a
                f.write("\n\n\n#Experiment: " + str(i))
                f.write("\n\n#seed: " + str(self.automata[0]) + "")
                f.write(
                    "\n{0:10}{1:13}{2:18}{3:16}{4:16}{5:16}".format("#iter", "f_C", "f_C_corr", "av_sum", "f_allC",
                                                                    "f_allD"))
                f.write("{0:14}{1:14}{2:15}{3:20}{4:26}".format("f_kD", "f_kC", "f_kDC", "f_strat_ch",
                                                                "f_strat_ch_final"))
                f.write("{0:17}{1:17}{2:21}\n".format("f_cr_0s", "f_cr_1s", "optim_solut"))

                # result-b
                f2.write("\n\n\n#Experiment: " + str(i))
                f2.write("\n\n#seed: " + str(self.automata[0]) + "")
                f2.write("\n{0:10}{1:14}{2:14}".format("iter", "f_0D", "f_1D"))
                f2.write("{0:14}{1:14}{2:14}{3:14}{4:14}{5:14}{6:14}".format("f_2D", "f_3D", "f_4D", "f_5D", "f_6D",
                                                                             "f_7D",
                                                                             "f_8D"))
                f2.write("{0:14}{1:14}{2:14}{3:14}{4:14}{5:14}{6:14}".format("f_0C", "f_1C", "f_2C", "f_3C", "f_4C",
                                                                             "f_5C",
                                                                             "f_6C"))
                f2.write(
                    "{0:14}{1:14}{2:15}{3:15}{4:15}{5:15}{6:15}{7:15}{8:15}{9:15}{10:15}\n".format("f_7C", "f_8C",
                                                                                        "f_0DC", "f_1DC", "f_2DC",
                                                                        "f_3DC",
                                                                        "f_4DC", "f_5DC", "f_6DC", "f_7DC", "f_8DC"))

            stats_multirun_temp = []
            # maximum number of iterations written to files is 500
            if self.data.iterations.num_of_iter > 500:
                step = self.data.iterations.num_of_iter / 500
                for j in range(0, 500):
                    statistics = self.automata[1][round(j * step)]
                    if not self.is_multi_run:
                        statistics.write_stats_to_file_b(f2)
                        statistics.write_stats_to_file_a(f)

                    if self.is_multi_run:
                        statistics.write_stats_to_file_a(f3)
                        if statistics.max_f_C_corr is not None:
                            _iter, _ = statistics.max_f_C_corr
                            self.automata[1][_iter].write_stats_to_file_a(f4)
                        stats_multirun_temp.append(statistics)

            else:
                for statistics in self.automata[1]:
                    if not self.is_multi_run:
                        statistics.write_stats_to_file_b(f2)
                        statistics.write_stats_to_file_a(f)

                    if self.is_multi_run:
                        statistics.write_stats_to_file_a(f3)
                        if statistics.max_f_C_corr is not None:
                            _iter, _ = statistics.max_f_C_corr
                            self.automata[1][_iter].write_stats_to_file_a(f4)
                        stats_multirun_temp.append(statistics)


            if self.is_multi_run:
                stats_multirun.append((i, stats_multirun_temp))

            if 0 < self.data.iterations.num_of_exper - 1 == i:
                statistics_multirun = StatisticsMultirun(stats_multirun, self.data.iterations.num_of_iter, self.data.iterations.num_of_exper)
                f3 = open("m-RESULTS//std_results_a.txt", "w")
                self.save_parameters(f3)
                f3.write("\n\n{0:10}{1:16}{2:17}{3:20}{4:21}{5:19}".format("#iter", "av_f_C", "std_f_C", "av_f_C_corr", "std_f_C_corr",
                                                                           "av_av_pay"))
                f3.write("{0:20}{1:20}{2:21}{3:20}{4:21}".format("std_av_pay", "av_f_cr_0s", "std_f_cr_0s", "av_f_cr_1s", "std_f_cr_1s"))
                f3.write("{0:19}{1:20}{2:19}{3:20}{4:18}".format("av_f_allC", "std_f_allC", "av_f_allD", "std_f_allD",
                         "av_f_kD"))
                f3.write("{0:19}{1:18}{2:19}{3:19}{4:20}".format("std_f_kD", "av_f_kC", "std_f_kC", "av_f_kDC",
                         "std_f_kDC"))
                f3.write("{0:23}{1:24}{2:29}{3:30}\n".format("av_f_strat_ch", "std_f_strat_ch", "av_f_strat_ch_final", "std_f_strat_ch_final"))
                statistics_multirun.write_to_file(f3)

        f.close()
        f2.close()
        f3.close()
        f4.close()

        self.simulationDoneMessage()
        self.enableStartButton()


    # update display of CA depending on iteration
    # visualization mode defines what type of visualization is chosen (state/strategy)
    def change_iter_display(self):
        if self.visualization_mode == 0:
            self.state_color_handler()
        elif self.visualization_mode == 1:  # strategies
            self.strategies_color_handler()
        elif self.visualization_mode == 2:  # kD
            self.kD_strategies_color_handler()
        elif self.visualization_mode == 3:  # kC
            self.kC_strategies_color_handler()
        elif self.visualization_mode == 4:  # kDC
            self.kDC_strategies_color_handler()
        else:  # action
            self.action_color_handler()

    def enableStartButton(self):
        self.ui.pushButton_start.setEnabled(True)
        self.ui.pushButton_start_anim.setDisabled(False)



    def pause_animation(self):
        self.animation.stop()
        self.enableStartButton()

    def isRunning_false(self):
        self.isAnimationRunning = False
        self.enableStartButton()

    def calculateSleepTime(self):
        rows = self.data.canvas.rows
        cols = self.data.canvas.cols
        cells = rows * cols
        if cells < 5000:
            return 0.2
        elif cells < 7000:
            return 0.5
        elif cells < 9000:
            return 0.8
        else:
            return 1.0


    # create a new seperate thread for simulation
    def start_animation_thread(self):
        if self.isAnimationRunning == True:
            self.animation.play()
        else:
            self.isAnimationRunning = True
            self.ui.disableStartButton()
            numOfIters = self.iterations.num_of_iter
            self.animation.numofIters = numOfIters
            self.animation.iter = 0
            time = self.calculateSleepTime()
            self.animation.setSleepTime(time)
            self.animation_thread.start()
            self.anim_start_signal.emit()


    def start_animation(self):
        iter = self.ui.spinBox_iters.value()
        self.ui.spinBox_iters.setValue(iter + 1)
        # self.ui.graphicsView_CA.repaint(

    @Slot(int)
    def animation_signal_handler(self, iter):
        # self.ui.spinBox_iters.blockSignals(True)
        self.ui.spinBox_iters.setValue(iter)

        # self.ui.spinBox_iters.blockSignals(False)


    def create_graph(self):
        scene = QGraphicsScene()
        x = self.ui.spinBox_num_of_iter.value()
        self.gnuplot = GnuplotCanvas(self, x_len=x, y_range=[0, 1])
        scene.addWidget(self.gnuplot)
        self.ui.graphicsView_gnuplot.setScene(scene)

    # method to update graph after automata finished calculating
    @Slot(int)
    def update_graph(self, iter):
        for statistics in self.automata[1]:
            if (statistics.get_iter() == iter):
                f_C = statistics.get_f_C()
                f_C_corr = statistics.get_f_C_corr()
                f_strat_ch = statistics.get_f_strat_ch()
                f_strat_ch_final = statistics.get_f_strat_ch_final()
                avg_payoff = statistics.av_sum
                break

        self.gnuplot.updateCanvas(f_C, f_C_corr, avg_payoff, f_strat_ch, f_strat_ch_final)

        # method to update graph while automata is still calculating
    def update_graph_async(self, f_C, f_C_corr, avg_payoff, f_strat_ch, f_strat_ch_final):
        self.gnuplot.updateCanvas(f_C, f_C_corr, avg_payoff, f_strat_ch, f_strat_ch_final)

    def simulationDoneMessage(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Finished calculating.")
        self.end = time.time()
        self.calculate_exec_time()
        msg.setWindowTitle("Done!")
        msg.exec_()



def run_process(rows, cols, p_init_C, all_C,
                all_D, k_D, k_C,
                k_var_min, k_var_max,
                num_of_iter,
                d, c, b, a,
                isSharing,
                synch_prob, isTournament,
                p_state_mut,
                p_strat_mut, p_0_neighb_mut,
                p_1_neighb_mut,
                isDebug, is_test1, is_test2, f,
                optimal_num_1s, is_payoff_1, u, is_multi_run, seed, is_LA, memoryh, epsilon, min_payoff):
    if not is_LA:
        automata_multirun = (CA(rows, cols, p_init_C, all_C,
                                 all_D, k_D, k_C,
                                 k_var_min, k_var_max,
                                 num_of_iter,
                                 d, c, b, a,
                                 isSharing,
                                 synch_prob, isTournament,
                                 p_state_mut,
                                 p_strat_mut, p_0_neighb_mut,
                                 p_1_neighb_mut,
                                 isDebug, is_test1, is_test2, f,
                                 optimal_num_1s, is_payoff_1, u, is_multi_run,
                                 seed))
    else:
        automata_multirun = (LA(rows, cols, p_init_C, all_C,
                                 all_D, k_D, k_C,
                                 k_var_min, k_var_max,
                                 num_of_iter,
                                 d, c, b, a,
                                 isSharing,
                                 synch_prob, isTournament,
                                 p_state_mut,
                                 p_strat_mut, p_0_neighb_mut,
                                 p_1_neighb_mut,
                                 isDebug, is_test1, is_test2, f,
                                 optimal_num_1s, is_payoff_1, u, memoryh, epsilon, min_payoff, is_multi_run,
                                 seed))
    automata_multirun.evolution()
    return automata_multirun