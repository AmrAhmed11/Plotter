import numpy as np
from PyQt5.QtWidgets import*
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

def plot(functionEdit,maxEdit,minEdit,MPL ):
    y = functionEdit.text()
    maxX = float(maxEdit.text())
    minX = float(minEdit.text())

    y=y.replace("^","**")

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
        y=np.full(x.shape,y)


    MPL.canvas.axes.clear()
    MPL.canvas.axes.plot(x, y)
    MPL.canvas.draw()

def validate(functionEdit,maxEdit,minEdit):
    y = functionEdit.text()
    minX = minEdit.text()
    maxX = maxEdit.text()
     # handle empty function field
    if len(y) == 0 or y.isspace():
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setWindowTitle("Error")
        error_dialog.setWindowIcon(QtGui.QIcon('logo.png'))
        error_dialog.setText('Function field is empty!')
        error_dialog.exec_()
        return 0
    # handle empty minimum field
    elif len(minX) == 0:
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setWindowTitle("Error")
        error_dialog.setWindowIcon(QtGui.QIcon('logo.png'))
        error_dialog.setText('Minimum x field is empty!')
        error_dialog.exec_()
        return 0
    # handle empty maximum field
    elif len(maxX) == 0:
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setWindowTitle("Error")
        error_dialog.setWindowIcon(QtGui.QIcon('logo.png'))
        error_dialog.setText('Maximum x field is empty!')
        error_dialog.exec_()
        return 0
    # handle max x is bigger or equal to min x
    elif float(minX) >= float(maxX):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setWindowTitle("Error")
        error_dialog.setWindowIcon(QtGui.QIcon('logo.png'))
        error_dialog.setText('Maximum x field cannot be smaller or equal to minimum')
        error_dialog.exec_()
        return 0
    # handle function field contains a non valid character.
    for i in y:
        if not i.isdigit() and i not in ["x","*","+","-","/","^"," ",".","(",")"]:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Critical)
            error_dialog.setWindowTitle("Error")
            error_dialog.setWindowIcon(QtGui.QIcon('logo.png'))
            error_dialog.setText('function field contains a non-equation symbol')
            error_dialog.exec_()
            return 0
        
    return 1


        
