# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtWidgets import (QButtonGroup, QCheckBox, QDoubleSpinBox,
    QFrame, QGraphicsView, QTableWidget, QGroupBox, QLCDNumber,
    QLabel, QMenuBar, QPushButton, QRadioButton, QSpinBox, QStatusBar,
    QWidget, QAbstractItemView)

class Ui_MainWindow(object):

    def disableStartButton(self):
        self.pushButton_start.setEnabled(False)   

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(958, 686)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.graphicsView_CA = QTableWidget(self.centralwidget)
        self.graphicsView_CA.setObjectName(u"graphicsView_CA")
        self.graphicsView_CA.setGeometry(QRect(490, 80, 300, 300))
        self.graphicsView_CA.verticalHeader().setVisible(False)
        self.graphicsView_CA.horizontalHeader().setVisible(False)
        self.graphicsView_CA.horizontalHeader().setMinimumSectionSize(1)
        self.graphicsView_CA.setSelectionMode(QAbstractItemView.SingleSelection)
        self.graphicsView_CA.verticalHeader().setMinimumSectionSize(1)
        self.graphicsView_CA.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        self.pushButton_states = QPushButton(self.centralwidget)
        self.pushButton_states.setObjectName(u"pushButton_states")
        self.pushButton_states.setGeometry(QRect(380, 20, 80, 24))
        self.pushButton_states.clicked.connect(MainWindow.state_color_handler)
        
        self.pushButton_strategies = QPushButton(self.centralwidget)
        self.pushButton_strategies.setObjectName(u"pushButton_strategies")
        self.pushButton_strategies.setGeometry(QRect(470, 20, 80, 24))
        self.pushButton_strategies.clicked.connect(MainWindow.strategies_color_handler)
        
        self.pushButton_kD = QPushButton(self.centralwidget)
        self.pushButton_kD.setObjectName(u"pushButton_kD")
        self.pushButton_kD.setGeometry(QRect(560, 20, 80, 24))
        self.pushButton_kD.clicked.connect(MainWindow.kD_strategies_color_handler)

        
        self.pushButton_kC = QPushButton(self.centralwidget)
        self.pushButton_kC.setObjectName(u"pushButton_kC")
        self.pushButton_kC.setGeometry(QRect(650, 20, 80, 24))
        self.pushButton_kC.clicked.connect(MainWindow.kC_strategies_color_handler)
        
        self.pushButton_kDC = QPushButton(self.centralwidget)
        self.pushButton_kDC.setObjectName(u"pushButton_kDC")
        self.pushButton_kDC.setGeometry(QRect(740, 20, 80, 24))
        self.pushButton_kDC.clicked.connect(MainWindow.kDC_strategies_color_handler)

        self.pushButton_actions = QPushButton(self.centralwidget)
        self.pushButton_actions.setObjectName(u"pushButton_actions")
        self.pushButton_actions.setGeometry(QRect(830, 20, 80, 24))
        self.pushButton_actions.clicked.connect(MainWindow.action_color_handler)
        
        # disabling buttons before simulation has started
        self.pushButton_states.setDisabled(1)
        self.pushButton_strategies.setDisabled(1)
        self.pushButton_kD.setDisabled(1)
        self.pushButton_kC.setDisabled(1)
        self.pushButton_kDC.setDisabled(1)
        self.pushButton_actions.setDisabled(1)
        self.pushButton_states.setDisabled(1)
       
        
        self.groupBox_simul = QGroupBox(self.centralwidget)
        self.groupBox_simul.setObjectName(u"groupBox_simul")
        self.groupBox_simul.setGeometry(QRect(10, 0, 361, 511))
        self.spinBox_Ncols = QSpinBox(self.groupBox_simul)
        self.spinBox_Ncols.setObjectName(u"spinBox_Ncols")
        self.spinBox_Ncols.setGeometry(QRect(60, 60, 61, 25))
        self.spinBox_Ncols.setValue(51)
        self.spinBox_Ncols.setMaximum(999)
        self.doubleSpinBox_p_init_C = QDoubleSpinBox(self.groupBox_simul)
        self.doubleSpinBox_p_init_C.setObjectName(u"doubleSpinBox_p_init_C")
        self.doubleSpinBox_p_init_C.setGeometry(QRect(60, 90, 62, 25))
        self.doubleSpinBox_p_init_C.setMaximum(1.000000000000000)
        self.doubleSpinBox_p_init_C.setSingleStep(0.100000000000000)
        self.doubleSpinBox_p_init_C.setValue(0.500000000000000)
        self.label_24 = QLabel(self.groupBox_simul)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(10, 30, 51, 21))
        self.label_23 = QLabel(self.groupBox_simul)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 90, 49, 21))
        self.spinBox_Mrows = QSpinBox(self.groupBox_simul)
        self.spinBox_Mrows.setObjectName(u"spinBox_Mrows")
        self.spinBox_Mrows.setGeometry(QRect(60, 30, 61, 25))
        self.spinBox_Mrows.setValue(51)
        self.spinBox_Mrows.setMaximum(999)
        self.label_22 = QLabel(self.groupBox_simul)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 60, 51, 21))
        self.checkBox_sharing = QCheckBox(self.groupBox_simul)
        self.checkBox_sharing.setObjectName(u"checkBox_sharing")
        self.checkBox_sharing.setGeometry(QRect(10, 120, 78, 22))
        self.groupBox_competition = QGroupBox(self.groupBox_simul)
        self.groupBox_competition.setObjectName(u"groupBox_competition")
        self.groupBox_competition.setGeometry(QRect(10, 140, 171, 61))
        self.radioButton_roulette = QRadioButton(self.groupBox_competition)
        self.competition_group = QButtonGroup(MainWindow)
        self.competition_group.setObjectName(u"competition_group")
        self.competition_group.addButton(self.radioButton_roulette)
        self.radioButton_roulette.setObjectName(u"radioButton_roulette")
        self.radioButton_roulette.setGeometry(QRect(10, 20, 91, 22))
        self.radioButton_roulette.setChecked(False)
        self.radioButton_tournament = QRadioButton(self.groupBox_competition)
        self.competition_group.addButton(self.radioButton_tournament)
        self.radioButton_tournament.setObjectName(u"radioButton_tournament")
        self.radioButton_tournament.setEnabled(True)
        self.radioButton_tournament.setGeometry(QRect(10, 40, 91, 19))
        self.radioButton_tournament.setChecked(True)
        self.groupBox_mutation = QGroupBox(self.groupBox_simul)
        self.groupBox_mutation.setObjectName(u"groupBox_mutation")
        self.groupBox_mutation.setGeometry(QRect(10, 200, 171, 151))
        self.doubleSpinBox_p_state_mut = QDoubleSpinBox(self.groupBox_mutation)
        self.doubleSpinBox_p_state_mut.setObjectName(u"doubleSpinBox_p_state_mut")
        self.doubleSpinBox_p_state_mut.setGeometry(QRect(100, 30, 62, 25))
        self.doubleSpinBox_p_state_mut.setMaximum(1.000000000000000)
        self.doubleSpinBox_p_state_mut.setSingleStep(0.0001)
        self.doubleSpinBox_p_state_mut.setDecimals(4)
        self.doubleSpinBox_p_0_neigh_mut = QDoubleSpinBox(self.groupBox_mutation)
        self.doubleSpinBox_p_0_neigh_mut.setObjectName(u"doubleSpinBox_p_0_neigh_mut")
        self.doubleSpinBox_p_0_neigh_mut.setGeometry(QRect(100, 90, 62, 25))
        self.doubleSpinBox_p_0_neigh_mut.setMaximum(1.000000000000000)
        self.doubleSpinBox_p_0_neigh_mut.setSingleStep(0.0001)
        self.doubleSpinBox_p_0_neigh_mut.setValue(0.300000000000000)
        self.doubleSpinBox_p_0_neigh_mut.setDecimals(4)
        self.label_16 = QLabel(self.groupBox_mutation)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 30, 71, 21))
        self.label_19 = QLabel(self.groupBox_mutation)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 120, 101, 21))
        self.label_17 = QLabel(self.groupBox_mutation)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 60, 71, 21))
        self.doubleSpinBox_p_1_neigh_mut = QDoubleSpinBox(self.groupBox_mutation)
        self.doubleSpinBox_p_1_neigh_mut.setObjectName(u"doubleSpinBox_p_1_neigh_mut")
        self.doubleSpinBox_p_1_neigh_mut.setGeometry(QRect(100, 120, 62, 25))
        self.doubleSpinBox_p_1_neigh_mut.setMaximum(1.000000000000000)
        self.doubleSpinBox_p_1_neigh_mut.setSingleStep(0.0001)
        self.doubleSpinBox_p_1_neigh_mut.setValue(0.100000000000000)
        self.doubleSpinBox_p_1_neigh_mut.setDecimals(4)
        self.label_18 = QLabel(self.groupBox_mutation)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 90, 91, 21))
        self.doubleSpinBox_p_strat_mut = QDoubleSpinBox(self.groupBox_mutation)
        self.doubleSpinBox_p_strat_mut.setObjectName(u"doubleSpinBox_p_strat_mut")
        self.doubleSpinBox_p_strat_mut.setGeometry(QRect(100, 60, 62, 25))
        self.doubleSpinBox_p_strat_mut.setMaximum(1.000000000000000)
        self.doubleSpinBox_p_strat_mut.setSingleStep(0.0001)
        self.doubleSpinBox_p_strat_mut.setDecimals(4)
        self.groupBox_strategies = QGroupBox(self.groupBox_simul)
        self.groupBox_strategies.setObjectName(u"groupBox_strategies")
        self.groupBox_strategies.setGeometry(QRect(200, 20, 151, 241))
        self.spinBox_kMin = QSpinBox(self.groupBox_strategies)
        self.spinBox_kMin.setObjectName(u"spinBox_kMin")
        self.spinBox_kMin.setGeometry(QRect(10, 210, 42, 25))
        self.label_14 = QLabel(self.groupBox_strategies)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(70, 190, 49, 16))
        self.label_11 = QLabel(self.groupBox_strategies)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 140, 51, 21))
        self.spinBox_kMax = QSpinBox(self.groupBox_strategies)
        self.spinBox_kMax.setObjectName(u"spinBox_kMax")
        self.spinBox_kMax.setGeometry(QRect(70, 210, 42, 25))
        self.spinBox_kMax.setValue(8)
        self.label_12 = QLabel(self.groupBox_strategies)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 170, 91, 21))
        self.doubleSpinBox_kDC = QDoubleSpinBox(self.groupBox_strategies)
        self.doubleSpinBox_kDC.setObjectName(u"doubleSpinBox_kDC")
        self.doubleSpinBox_kDC.setGeometry(QRect(40, 140, 62, 25))
        self.doubleSpinBox_kDC.setMaximum(1.000000000000000)
        self.doubleSpinBox_kDC.setSingleStep(0.100000000000000)
        self.doubleSpinBox_kDC.setValue(0.200000000000000)
        self.doubleSpinBox_allC = QDoubleSpinBox(self.groupBox_strategies)
        self.doubleSpinBox_allC.setObjectName(u"doubleSpinBox_allC")
        self.doubleSpinBox_allC.setGeometry(QRect(40, 20, 62, 25))
        self.doubleSpinBox_allC.setMaximum(1.000000000000000)
        self.doubleSpinBox_allC.setSingleStep(0.100000000000000)
        self.doubleSpinBox_allC.setValue(0.200000000000000)
        self.label_10 = QLabel(self.groupBox_strategies)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 110, 51, 21))
        self.label_9 = QLabel(self.groupBox_strategies)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 80, 51, 21))
        self.label_7 = QLabel(self.groupBox_strategies)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 20, 51, 21))
        self.label_13 = QLabel(self.groupBox_strategies)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 190, 49, 16))
        self.doubleSpinBox_kC = QDoubleSpinBox(self.groupBox_strategies)
        self.doubleSpinBox_kC.setObjectName(u"doubleSpinBox_kC")
        self.doubleSpinBox_kC.setGeometry(QRect(40, 110, 62, 25))
        self.doubleSpinBox_kC.setMaximum(1.000000000000000)
        self.doubleSpinBox_kC.setSingleStep(0.100000000000000)
        self.doubleSpinBox_kC.setValue(0.200000000000000)
        self.label_8 = QLabel(self.groupBox_strategies)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 50, 51, 21))
        self.doubleSpinBox_allD = QDoubleSpinBox(self.groupBox_strategies)
        self.doubleSpinBox_allD.setObjectName(u"doubleSpinBox_allD")
        self.doubleSpinBox_allD.setGeometry(QRect(40, 50, 62, 25))
        self.doubleSpinBox_allD.setMaximum(1.000000000000000)
        self.doubleSpinBox_allD.setSingleStep(0.100000000000000)
        self.doubleSpinBox_allD.setValue(0.200000000000000)
        self.doubleSpinBox_kD = QDoubleSpinBox(self.groupBox_strategies)
        self.doubleSpinBox_kD.setObjectName(u"doubleSpinBox_kD")
        self.doubleSpinBox_kD.setGeometry(QRect(40, 80, 62, 25))
        self.doubleSpinBox_kD.setMaximum(1.000000000000000)
        self.doubleSpinBox_kD.setSingleStep(0.100000000000000)
        self.doubleSpinBox_kD.setValue(0.200000000000000)
        self.label_20 = QLabel(self.groupBox_simul)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(210, 270, 71, 21))
        self.doubleSpinBox_synch_prob = QDoubleSpinBox(self.groupBox_simul)
        self.doubleSpinBox_synch_prob.setObjectName(u"doubleSpinBox_synch_prob")
        self.doubleSpinBox_synch_prob.setGeometry(QRect(290, 270, 62, 25))
        self.doubleSpinBox_synch_prob.setMaximum(1.000000000000000)
        self.doubleSpinBox_synch_prob.setSingleStep(0.100000000000000)
        self.doubleSpinBox_synch_prob.setValue(1.000000000000000)
        self.label_21 = QLabel(self.groupBox_simul)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(200, 300, 101, 21))
        self.groupBox_seed = QGroupBox(self.groupBox_simul)
        self.groupBox_seed.setObjectName(u"groupBox_seed")
        self.groupBox_seed.setGeometry(QRect(200, 330, 151, 81))
        self.radioButton_clock = QRadioButton(self.groupBox_seed)
        self.radioButton_clock.setObjectName(u"radioButton_clock")
        self.radioButton_clock.setGeometry(QRect(10, 10, 82, 22))
        self.radioButton_clock.setChecked(True)
        self.spinBox_custom_seed = QSpinBox(self.groupBox_seed)
        self.spinBox_custom_seed.setObjectName(u"spinBox_custom_seed")
        self.spinBox_custom_seed.setEnabled(False)
        self.spinBox_custom_seed.setGeometry(QRect(10, 50, 89, 25))
        self.radioButton_custom = QRadioButton(self.groupBox_seed)
        self.radioButton_custom.setObjectName(u"radioButton_custom")
        self.radioButton_custom.setGeometry(QRect(10, 30, 94, 22))
        self.label_25 = QLabel(self.groupBox_simul)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(10, 360, 71, 21))
        self.label_26 = QLabel(self.groupBox_simul)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(10, 390, 81, 21))
        self.spinBox_num_of_iter = QSpinBox(self.groupBox_simul)
        self.spinBox_num_of_iter.setObjectName(u"spinBox_num_of_iter")
        self.spinBox_num_of_iter.setGeometry(QRect(90, 360, 51, 25))
        self.spinBox_num_of_iter.setMaximum(500)
        self.spinBox_num_of_iter.setValue(100)
        self.spinBox_num_of_exper = QSpinBox(self.groupBox_simul)
        self.spinBox_num_of_exper.setObjectName(u"spinBox_num_of_exper")
        self.spinBox_num_of_exper.setGeometry(QRect(90, 390, 51, 25))
        self.spinBox_num_of_exper.setValue(1)
        self.groupBox_debug = QGroupBox(self.groupBox_simul)
        self.groupBox_debug.setObjectName(u"groupBox_debug")
        self.groupBox_debug.setEnabled(False)
        self.groupBox_debug.setGeometry(QRect(10, 440, 171, 61))
        self.radioButton_CA_state = QCheckBox(self.groupBox_debug)
        self.radioButton_CA_state.setObjectName(u"radioButton_CA_state")
        self.radioButton_CA_state.setGeometry(QRect(10, 10, 141, 22))
        self.radioButton_CA_strat = QCheckBox(self.groupBox_debug)
        self.radioButton_CA_strat.setObjectName(u"radioButton_CA_strat")
        self.radioButton_CA_strat.setGeometry(QRect(10, 30, 121, 22))
        self.radioButton_debug = QCheckBox(self.groupBox_simul)
        self.radioButton_debug.setObjectName(u"radioButton_debug")
        self.radioButton_debug.setGeometry(QRect(10, 420, 82, 22))
        self.radioButton_test1 = QCheckBox(self.groupBox_simul)
        # self.buttonGroup = QButtonGroup(MainWindow)
        # self.buttonGroup.setObjectName(u"buttonGroup")
        # self.buttonGroup.addButton(self.radioButton_test1)
        self.radioButton_test1.setObjectName(u"radioButton_test1")
        self.radioButton_test1.setGeometry(QRect(200, 410, 91, 22))
        self.radioButton_test2 = QCheckBox(self.groupBox_simul)
        # self.buttonGroup.addButton(self.radioButton_test2)
        self.radioButton_test2.setObjectName(u"radioButton_test2")
        self.radioButton_test2.setGeometry(QRect(200, 430, 91, 21))
        self.radioButton_test3 = QCheckBox(self.groupBox_simul)
        # self.buttonGroup.addButton(self.radioButton_test3)
        self.radioButton_test3.setObjectName(u"radioButton_test3")
        self.radioButton_test3.setGeometry(QRect(200, 450, 91, 22))
        self.spinBox_optimal_num_1s = QSpinBox(self.groupBox_simul)
        self.spinBox_optimal_num_1s.setObjectName(u"spinBox_optimal_num_1s")
        self.spinBox_optimal_num_1s.setGeometry(QRect(290, 300, 61, 25))
        self.spinBox_optimal_num_1s.setMaximum(10000)
        self.spinBox_optimal_num_1s.setValue(676)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 510, 91, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 530, 81, 16))
        self.radiobutton_pay_fun_1 = QRadioButton(self.centralwidget)
        self.radiobutton_pay_fun_1.setObjectName(u"pay_fun_1")
        self.radiobutton_pay_fun_1.setGeometry(QRect(240, 515, 81, 16))
        self.radiobutton_pay_fun_1.setChecked(True)
        self.radiobutton_pay_fun_2 = QRadioButton(self.centralwidget)
        self.radiobutton_pay_fun_2.setObjectName(u"pay_fun_2")
        self.radiobutton_pay_fun_2.setGeometry(QRect(240, 535, 81, 16))
        self.groupBox_payoff = QGroupBox(self.centralwidget)
        self.groupBox_payoff.setObjectName(u"groupBox_payoff")
        self.groupBox_payoff.setGeometry(QRect(50, 560, 181, 71))
        self.button_group_payoff = QButtonGroup(self.centralwidget)
        self.button_group_payoff.addButton(self.radiobutton_pay_fun_1)
        self.button_group_payoff.addButton(self.radiobutton_pay_fun_2)
        self.label_3 = QLabel(self.groupBox_payoff)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 49, 20))
        self.doubleSpinBox_d = QDoubleSpinBox(self.groupBox_payoff)
        self.doubleSpinBox_d.setObjectName(u"doubleSpinBox_d")
        self.doubleSpinBox_d.setGeometry(QRect(20, 10, 62, 25))
        self.doubleSpinBox_d.setMaximum(99.989999999999995)
        self.doubleSpinBox_d.setSingleStep(0.100000000000000)
        self.doubleSpinBox_d.setValue(1.000000000000000)
        self.label_4 = QLabel(self.groupBox_payoff)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 40, 49, 20))
        self.doubleSpinBox_b = QDoubleSpinBox(self.groupBox_payoff)
        self.doubleSpinBox_b.setObjectName(u"doubleSpinBox_b")
        self.doubleSpinBox_b.setGeometry(QRect(20, 40, 62, 25))
        self.doubleSpinBox_b.setSingleStep(0.100000000000000)
        self.doubleSpinBox_b.setValue(1.200000000000000)
        self.label_5 = QLabel(self.groupBox_payoff)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(90, 10, 49, 20))
        self.label_6 = QLabel(self.groupBox_payoff)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(90, 40, 49, 16))
        self.doubleSpinBox_c = QDoubleSpinBox(self.groupBox_payoff)
        self.doubleSpinBox_c.setObjectName(u"doubleSpinBox_c")
        self.doubleSpinBox_c.setGeometry(QRect(100, 10, 62, 25))
        self.doubleSpinBox_c.setSingleStep(0.100000000000000)
        self.doubleSpinBox_a = QDoubleSpinBox(self.groupBox_payoff)
        self.doubleSpinBox_a.setObjectName(u"doubleSpinBox_a")
        self.doubleSpinBox_a.setGeometry(QRect(100, 40, 62, 25))
        self.doubleSpinBox_a.setSingleStep(0.100000000000000)
        self.doubleSpinBox_a.setValue(0.100000000000000)
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(490, 50, 49, 16))

        self.lcdNumber_iters = QLCDNumber(self.centralwidget)
        self.lcdNumber_iters.setObjectName(u"lcdNumber_iters")
        self.lcdNumber_iters.setGeometry(QRect(540, 50, 51, 21))

        self.label_27 = QLabel(self.centralwidget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(90, 540, 49, 21))
        self.label_28 = QLabel(self.centralwidget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(30, 570, 21, 21))
        self.label_29 = QLabel(self.centralwidget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(170, 540, 49, 21))
        self.label_30 = QLabel(self.centralwidget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(30, 600, 49, 21))
        self.label_31 = QLabel(self.centralwidget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(0, 580, 49, 31))
        self.label_32 = QLabel(self.centralwidget)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(620, 50, 49, 16))
        self.pushButton_start_anim = QPushButton(self.centralwidget)
        self.pushButton_start_anim.setObjectName(u"pushButton_start_anim")
        self.pushButton_start_anim.setGeometry(QRect(580, 400, 61, 21))
        self.pushButton_start_anim.clicked.connect(MainWindow.start_animation_thread)
        self.spinBox_iters = QSpinBox(self.centralwidget)
        self.spinBox_iters.setObjectName(u"spinBox_iters")
        self.spinBox_iters.setGeometry(QRect(510, 400, 61, 25))
        self.spinBox_iters.setMaximum(1000)
        self.spinBox_iters.setValue(0)
        self.label_33 = QLabel(self.centralwidget)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(460, 400, 51, 20))
        self.pushButton_stop = QPushButton(self.centralwidget)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        self.pushButton_stop.setGeometry(QRect(650, 400, 61, 21))
        self.pushButton_stop.clicked.connect(MainWindow.pause_animation)
        self.pushButton_save = QPushButton(self.centralwidget)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setGeometry(QRect(720, 400, 81, 21))
        self.pushButton_save.clicked.connect(MainWindow.saveImage)
        self.graphicsView_gnuplot = QGraphicsView(self.centralwidget)
        self.graphicsView_gnuplot.setObjectName(u"graphicsView_gnuplot")
        self.graphicsView_gnuplot.setGeometry(QRect(380, 440, 571, 192))
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(370, 420, 651, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.pushButton_start = QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setGeometry(QRect(240, 560, 111, 71))
        self.pushButton_start.clicked.connect(MainWindow.startSimulation)
        self.pushButton_start.clicked.connect(MainWindow.create_graph)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 958, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.label_24.setBuddy(self.spinBox_Mrows)
        self.label_23.setBuddy(self.doubleSpinBox_p_init_C)
        self.label_22.setBuddy(self.spinBox_Ncols)
        self.label_16.setBuddy(self.doubleSpinBox_p_state_mut)
        self.label_19.setBuddy(self.doubleSpinBox_p_1_neigh_mut)
        self.label_17.setBuddy(self.doubleSpinBox_p_strat_mut)
        self.label_18.setBuddy(self.doubleSpinBox_p_0_neigh_mut)
        self.label_14.setBuddy(self.spinBox_kMax)
        self.label_11.setBuddy(self.doubleSpinBox_kDC)
        self.label_10.setBuddy(self.doubleSpinBox_kC)
        self.label_9.setBuddy(self.doubleSpinBox_kD)
        self.label_7.setBuddy(self.doubleSpinBox_allC)
        self.label_13.setBuddy(self.spinBox_kMin)
        self.label_8.setBuddy(self.doubleSpinBox_allD)
        self.label_20.setBuddy(self.doubleSpinBox_synch_prob)
        self.label_25.setBuddy(self.spinBox_num_of_iter)
        self.label_26.setBuddy(self.spinBox_num_of_exper)
        self.label_3.setBuddy(self.doubleSpinBox_d)
        self.label_4.setBuddy(self.doubleSpinBox_b)
        self.label_5.setBuddy(self.doubleSpinBox_c)
        self.label_6.setBuddy(self.doubleSpinBox_a)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)
        self.radioButton_custom.toggled.connect(self.spinBox_custom_seed.setEnabled)
        self.radioButton_debug.toggled.connect(self.groupBox_debug.setEnabled)
        self.radioButton_debug.toggled.connect(self.radioButton_debug.setChecked)
        self.radioButton_debug.toggled.connect(self.radioButton_CA_state.setChecked)
        self.radioButton_debug.toggled.connect(self.radioButton_CA_strat.setChecked)
        self.radioButton_CA_state.setEnabled(False)
        self.radioButton_CA_strat.setEnabled(False)


        self.spinBox_iters.valueChanged.connect(self.lcdNumber_iters.display)
        self.spinBox_iters.valueChanged.connect(MainWindow.change_iter_display)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_states.setText(QCoreApplication.translate("MainWindow", u"states", None))
        self.pushButton_strategies.setText(QCoreApplication.translate("MainWindow", u"strategies", None))
        self.pushButton_kD.setText(QCoreApplication.translate("MainWindow", u"k-D strat", None))
        self.pushButton_kC.setText(QCoreApplication.translate("MainWindow", u"k-C strat", None))
        self.pushButton_kDC.setText(QCoreApplication.translate("MainWindow", u"k-DC strat", None))
        self.pushButton_actions.setText(QCoreApplication.translate("MainWindow", u"actions C/D", None))
        self.groupBox_simul.setTitle(QCoreApplication.translate("MainWindow", u"Simulation parameteres:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"M rows:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"p_init_C", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"N cols:", None))
        self.checkBox_sharing.setText(QCoreApplication.translate("MainWindow", u"sharing", None))
        self.groupBox_competition.setTitle(QCoreApplication.translate("MainWindow", u"Competition type:", None))
        self.radioButton_roulette.setText(QCoreApplication.translate("MainWindow", u"roulette", None))
        self.radioButton_tournament.setText(QCoreApplication.translate("MainWindow", u"tournament", None))
        self.groupBox_mutation.setTitle(QCoreApplication.translate("MainWindow", u"Mutation:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"p_state_mut", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"p_1_neigh_mut", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"p_strat_mut", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"p_0_neigh_mut", None))
        self.groupBox_strategies.setTitle(QCoreApplication.translate("MainWindow", u"Strategies:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"k-DC", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"k-var (from-to) ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"k-C", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"k-D", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"all-C", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"all-D", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"synch_prob", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"optimal_num_1s", None))
        self.groupBox_seed.setTitle("")
        self.radioButton_clock.setText(QCoreApplication.translate("MainWindow", u"clock_seed", None))
        self.radioButton_custom.setText(QCoreApplication.translate("MainWindow", u"custom_seed", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"num_of_iter", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"num_of_exper", None))
        self.groupBox_debug.setTitle("")
        self.radioButton_CA_state.setText(QCoreApplication.translate("MainWindow", u"read_CA_state_deb", None))
        self.radioButton_CA_strat.setText(QCoreApplication.translate("MainWindow", u"read_CA_strat_deb", None))
        self.radioButton_debug.setText(QCoreApplication.translate("MainWindow", u"debug", None))
        self.radioButton_test1.setText(QCoreApplication.translate("MainWindow", u"test_1", None))
        self.radioButton_test2.setText(QCoreApplication.translate("MainWindow", u"test_2", None))
        self.radioButton_test3.setText(QCoreApplication.translate("MainWindow", u"test_3", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Payoff function:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"neighbour", None))
        self.radiobutton_pay_fun_1.setText(QCoreApplication.translate("MainWindow", u"pay_fun_1", None))
        self.radiobutton_pay_fun_2.setText(QCoreApplication.translate("MainWindow", u"pay_fun_2", None))
        self.groupBox_payoff.setTitle("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"d:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"b:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"c:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"a:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Iteration: ", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"C*", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"C*", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"D*", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"D*", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"player", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Mode:", None))
        self.pushButton_start_anim.setText(QCoreApplication.translate("MainWindow", u"start anim", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"iter_step:", None))
        self.pushButton_stop.setText(QCoreApplication.translate("MainWindow", u"stop anim", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"save pictures", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"START", None))
    # retranslateUi



