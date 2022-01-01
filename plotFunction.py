import numpy as np
from PyQt5.QtWidgets import*
from PyQt5 import QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

#matplotlib class
class MPL(QWidget):
    
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        
        self.canvas = FigureCanvas(Figure())
        
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)


def clearPLot(MPL):
    MPL.canvas.axes.clear()
    MPL.canvas.draw()
# plotting function
def plot(functionEdit,maxEdit,minEdit,MPL ):

    #taking the input from the fields
    y = functionEdit.text()
    y=y.replace("^","**")
    maxX = float(maxEdit.text())
    minX = float(minEdit.text())

    #creating array of numbers from min to max
    x = np.linspace(minX, maxX, 1000)

    #catching math errors from inputed equation
    try:
        y=eval(y)
    except Exception:
        #Error message
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setWindowTitle("Error")
        error_dialog.setWindowIcon(QtGui.QIcon('logo.png'))
        error_dialog.setText('Math error!')
        error_dialog.exec_()
        return

    #manually creating y array for constant equations
    if("x" not in functionEdit.text()):
        y=np.full(1000,y)

    #clearing old plot and ploting new equation
    MPL.canvas.axes.clear()
    MPL.canvas.axes.plot(x, y)
    MPL.canvas.draw()

#validating fields
def validate(functionEdit,maxEdit,minEdit):
    #setting up the error message
    error_dialog = QMessageBox()
    error_dialog.setIcon(QMessageBox.Critical)
    error_dialog.setWindowTitle("Error")
    error_dialog.setWindowIcon(QtGui.QIcon('logo.png'))

    
    y = functionEdit

    #catching errors in min and max fields
    try:
        minX = float(minEdit)
    except:
        if(not minEdit):
            error_dialog.setText('Enter Min value')
        else :
            error_dialog.setText('Min x entry is invalid!')
        error_dialog.exec_()
        return 0

    try:
        maxX = float(maxEdit)
    except:
        if(not maxEdit):
            error_dialog.setText('Enter Max value')
        else :
            error_dialog.setText('Max x entry is invalid!')
        error_dialog.exec_()
        return 0        
    
     # handle empty function field
    if len(y) == 0 or y.isspace():
        error_dialog.setText('Function field is empty!')
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


        
