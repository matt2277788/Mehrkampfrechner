import data
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic


qtcreator_file  = "mainWindow.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.getInputFromInput) # connect button clicked with action


    def getInputFromInput(self):

        p1 = data.P100M(float(self.Input100.text()))
        p2 = data.PWeit(float(self.InputWeit.text()))
        p3 = data.PKugel(float(self.InputKugel.text()))
        p4 = data.PHoch(float(self.InputHoch.text()))
        p5 = data.P400M(float(self.Input400.text()))
        p6 = data.P110H(float(self.Input110H.text()))
        p7 = data.PDiskus(float(self.InputDiskus.text()))
        p8 = data.PStab(float(self.InputStab.text()))
        p9 = data.PSpeer(float(self.InputSpeer.text()))
        p10 = data.P1500(float(self.Input1500.text()))

        self.Points100.setText(str(p1))
        self.PointsWeit.setText(str(p2))
        self.PointsKugel.setText(str(p3))
        self.PointsHoch.setText(str(p4))
        self.Points400.setText(str(p5))
        self.Points110H.setText(str(p6))
        self.PointsDiskus.setText(str(p7))
        self.PointsStab.setText(str(p8))
        self.PointsSpeer.setText(str(p9))
        self.Points1500.setText(str(p10))
        self.PointsSum.setText(str(p1+p2+p3+p4+p5+p6+p7+p8+p9+p10))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())