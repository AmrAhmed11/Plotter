from PyQt5 import QtCore, QtGui, QtWidgets
from plotFunction import plot,validate,clearPLot,MPL


# Generated code by QtDesigner Tool
class Ui_Plotter(object):
    def setupUi(self, Plotter):
        Plotter.setObjectName("Plotter")
        Plotter.resize(879, 477)
        self.centralwidget = QtWidgets.QWidget(Plotter)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.functionEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.functionEdit.setObjectName("functionEdit")
        self.verticalLayout.addWidget(self.functionEdit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.minEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.minEdit.setObjectName("minEdit")
        self.verticalLayout.addWidget(self.minEdit)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.maxEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.maxEdit.setObjectName("maxEdit")
        self.verticalLayout.addWidget(self.maxEdit)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.plotBtn = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotBtn.sizePolicy().hasHeightForWidth())
        self.plotBtn.setSizePolicy(sizePolicy)
        self.plotBtn.setObjectName("plotBtn")
        self.verticalLayout.addWidget(self.plotBtn)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.MPL = MPL(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MPL.sizePolicy().hasHeightForWidth())
        self.MPL.setSizePolicy(sizePolicy)
        self.MPL.setMinimumSize(QtCore.QSize(500, 0))
        self.MPL.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.MPL.setObjectName("MPL")
        self.gridLayout.addWidget(self.MPL, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        Plotter.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Plotter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 879, 21))
        self.menubar.setObjectName("menubar")
        Plotter.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Plotter)
        self.statusbar.setObjectName("statusbar")
        Plotter.setStatusBar(self.statusbar)

        self.retranslateUi(Plotter)
        QtCore.QMetaObject.connectSlotsByName(Plotter)

    #Plot Button Pressed Function
    def pressed(self):
        clearPLot(self.MPL)
        #validating the fields before ploting
        valid = validate(self.functionEdit.text(),self.maxEdit.text(),self.minEdit.text())
        if(valid==1):
            #ploting the equation
            plot(self.functionEdit,self.maxEdit,self.minEdit,self.MPL)

        
    def retranslateUi(self, Plotter):
        _translate = QtCore.QCoreApplication.translate
        Plotter.setWindowTitle(_translate("Plotter", "Plotter"))
        Plotter.setWindowIcon(QtGui.QIcon('logo.png'))
        self.label.setText(_translate("Plotter", "Enter Function"))
        self.label_3.setText(_translate("Plotter", "Min x"))
        self.label_2.setText(_translate("Plotter", "Max x"))
        self.plotBtn.setText(_translate("Plotter", "Plot"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Plotter = QtWidgets.QMainWindow()
    ui = Ui_Plotter()
    ui.setupUi(Plotter)
    Plotter.show()
    sys.exit(app.exec_())
