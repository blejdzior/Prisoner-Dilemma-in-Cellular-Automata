import time
from PySide6.QtCore import QRunnable, QMutex, Signal, QObject


class Animation(QObject):
    signal = Signal(int)
    signalFinished = Signal()
    def __init__(self, iter, numOfIters, sleepTime):

        super().__init__()
        # self.mainWindow = MainWindow
        self.iter = iter
        self.numofIters = numOfIters
        self.sleepTime = 0.2
        self.isPaused = False
        self.isRunning = True

    def run(self):

        print("Running a new thread")
        while self.iter < self.numofIters:
            if self.isPaused == True:
                time.sleep(0.1)
                continue
            self.signal.emit(self.iter)
            # self.mainWindow.start_animation()
            # self.mainWindow.update_graph(self.iter)
            self.iter += 1
            time.sleep(self.sleepTime)
        # self.mainWindow.enableStartButton()
        self.isRunning = False
        self.signalFinished.emit()
        print("Thread done")

        # self.mainWindow.isAnimationRunning = False

    def setSleepTime(self, time):
        self.sleepTime = time

    def stop(self):
        self.isPaused = True

    def play(self):
        self.isPaused = False

    def stillRunning(self):
        return self.isRunning

    def terminate(self):
        self.iter = self.numofIters
