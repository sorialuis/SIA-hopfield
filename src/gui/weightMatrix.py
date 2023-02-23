from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MatrizGeneralPesos(object):
    def setupUi(self, MatrizGeneralPesos):
        MatrizGeneralPesos.setObjectName("MatrizGeneralPesos")
        MatrizGeneralPesos.resize(900, 560)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MatrizGeneralPesos.sizePolicy().hasHeightForWidth())
        MatrizGeneralPesos.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(MatrizGeneralPesos)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.matrizGeneralPesos = QtWidgets.QTableView(MatrizGeneralPesos)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.matrizGeneralPesos.sizePolicy().hasHeightForWidth())
        self.matrizGeneralPesos.setSizePolicy(sizePolicy)
        self.matrizGeneralPesos.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.matrizGeneralPesos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.matrizGeneralPesos.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.matrizGeneralPesos.setMidLineWidth(0)
        self.matrizGeneralPesos.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.matrizGeneralPesos.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.matrizGeneralPesos.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.matrizGeneralPesos.setAutoScrollMargin(10)
        self.matrizGeneralPesos.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.matrizGeneralPesos.setGridStyle(QtCore.Qt.SolidLine)
        self.matrizGeneralPesos.setObjectName("matrizGeneralPesos")
        self.matrizGeneralPesos.horizontalHeader().setVisible(False)
        self.matrizGeneralPesos.horizontalHeader().setDefaultSectionSize(20)
        self.matrizGeneralPesos.horizontalHeader().setHighlightSections(False)
        self.matrizGeneralPesos.horizontalHeader().setMinimumSectionSize(10)
        self.matrizGeneralPesos.verticalHeader().setVisible(False)
        self.matrizGeneralPesos.verticalHeader().setDefaultSectionSize(20)
        self.matrizGeneralPesos.verticalHeader().setHighlightSections(False)
        self.matrizGeneralPesos.verticalHeader().setMinimumSectionSize(10)
        self.verticalLayout_3.addWidget(self.matrizGeneralPesos)

        self.retranslateUi(MatrizGeneralPesos)
        QtCore.QMetaObject.connectSlotsByName(MatrizGeneralPesos)

    def retranslateUi(self, MatrizGeneralPesos):
        _translate = QtCore.QCoreApplication.translate
        MatrizGeneralPesos.setWindowTitle(_translate("MatrizGeneralPesos", "Matriz general de pesos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MatrizGeneralPesos = QtWidgets.QDialog()
    ui = Ui_MatrizGeneralPesos()
    ui.setupUi(MatrizGeneralPesos)
    MatrizGeneralPesos.show()
    sys.exit(app.exec_())
