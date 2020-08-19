import time
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QTimer, QCoreApplication, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPixmap, QTextFormat
from Typify_ui import *
import keyboard
from Audio_io import listen, StartWriting, record_active
import ctypes

kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
SW_HIDE = 0
hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, SW_HIDE)

__author__ = "Rooney3110"
__version__ = "2.0"


class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.info_alternator = 1 
        self.text_update_timer = QTimer()
        self.timer = QTimer()
        self.ui.pushButton_record.clicked.connect(self.check_enable)
        self.ui.pushButton_stop.clicked.connect(self.stop_au)
        self.text_update_timer.timeout.connect(self.update_info)
        self.timer.timeout.connect(self.record_au)
        self.text_update_timer.start(2000)
        self.auwave_green = QPixmap("auwave_green.png")
        self.auwave_black = QPixmap("auwave_black.png")
        self.show()
    
    def check_enable(self):
        self.ui.label_display.setPixmap(self.auwave_green)
        self.timer.start(100)

    def record_au(self):
        self.ui.label_display.setPixmap(self.auwave_green)
        if keyboard.is_pressed('down'):
            strobj = listen()
            #print(strobj)
            self.ui.label_inform.setText(self._beautify_("Done listening! (ctrl+down to continue)"))
            StartWriting(strobj)
    
    def stop_au(self):
        self.ui.label_display.setPixmap(self.auwave_black)
        self.timer.stop()

    def update_info(self):
        if self.info_alternator%2 == 0:
            self.ui.label_inform.setText(self._beautify_("Press Enable to start Typifying."))
        else:
            self.ui.label_inform.setText(self._beautify_("Press down arrow before speaking."))
        self.info_alternator += 1
 
    def _beautify_(self, text):
        return str("<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#d0d0d0;\">"+text+"</span></p><p><span style=\" font-size:10pt; color:#d0d0d0;\"><br/></span></p></body></html>")

if __name__ == "__main__":
    App = QApplication(sys.argv)
    app = MyForm()
    app.show()
    sys.exit(App.exec_())
    
 