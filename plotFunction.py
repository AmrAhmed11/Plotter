import numpy as np
from PyQt5.QtWidgets import*
from PyQt5 import QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

class MPL(QWidget):
    
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        
        self.canvas = FigureCanvas(Figure())
        
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)

def plot(functionEdit,maxEdit,minEdit,MPL ):

    y = functionEdit.text()
    y=y.replace("^","**")

    maxX = float(maxEdit.text())
    minX = float(minEdit.text())
    
    x = np.linspace(minX, maxX, 1000)

    try:
        y=eval(y)
    except Exception:
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setWindowTitle("Error")
        error_dialog.setWindowIcon(QtGui.QIcon('logo.png'))
        error_dialog.setText('Math error!')
        error_dialog.exec_()
        return

    if("x" not in functionEdit.text()):
        y=np.full(1000,y)


    MPL.canvas.axes.clear()
    MPL.canvas.axes.plot(x, y)
    MPL.canvas.draw()

def validate(functionEdit,maxEdit,minEdit):
    error_dialog = QMessageBox()
    error_dialog.setIcon(QMessageBox.Critical)
    error_dialog.setWindowTitle("Error")
    error_dialog.setWindowIcon(QtGui.QIcon('logo.png'))

    y = functionEdit.text()

    try:
        minX = float(minEdit.text())
    except:
        error_dialog.setText('Min x entry is invalid!')
        error_dialog.exec_()
        return 0

    try:
        maxX = float(maxEdit.text())
    except:
        error_dialog.setText('Max x entry is invalid!')
        error_dialog.exec_()
        return 0        
    
     # handle empty function field
    if len(y) == 0 or y.isspace():
        error_dialog.setText('Function field is empty!')
        error_dialog.exec_()
        return 0
    # handle empty minimum field
    elif len(minEdit.text()) == 0:
        error_dialog.setText('Minimum x field is empty!')
        error_dialog.exec_()
        return 0
    # handle empty maximum field
    elif len(maxEdit.text()) == 0:
        error_dialog.setText('Maximum x field is empty!')
        error_dialog.exec_()
        return 0
    # handle max x is bigger or equal to min x
    elif maxX <= minX:
        error_dialog.setText('Maximum x field cannot be smaller or equal to minimum')
        error_dialog.exec_()
        return 0
    # handle function field contains a non valid character.
    for i in y:
        if not i.isdigit() and i not in ["x","*","+","-","/","^"," ",".","(",")"]:
            error_dialog.setText('function field contains a non-equation symbol')
            error_dialog.exec_()
            return 0
        
    return 1


        
