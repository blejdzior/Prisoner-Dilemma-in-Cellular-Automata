import time
from PySide6.QtCore import QRunnable

class Animation(QRunnable):
      def __init__(self, MainWindow, iter, numOfIters, sleepTime):
         super().__init__()
         self.mainWindow = MainWindow
         self.iter = iter
         self.numofIters = numOfIters
         if sleepTime > 0.3:
            self.sleepTime = sleepTime
            self.extendedSleepTime = 1.3 * sleepTime
         else:
             self.sleepTime = 0.3
             self.extendedSleepTime = 0.4
         self.isPaused = False
         self.isRunning = True

      def run(self):
         print("Running a new thread")
         while self.iter < self.numofIters - 1:
            if self.isPaused == True:
                time.sleep(0.1)
                continue
            self.mainWindow.start_animation()
            self.mainWindow.update_graph(self.iter)
            self.iter += 1
            time.sleep(self.sleepTime)
         self.mainWindow.enableStartButton()
         self.isRunning = False
         print("Thread done")

      def extendSleepTime(self):
          self.sleepTime = self.extendedSleepTime

      def stop(self):
         self.isPaused = True

      def play(self):
          self.isPaused = False

      def stillRunning(self):
          return self.isRunning
      
      def terminate(self):
          self.iter = self.numofIters

