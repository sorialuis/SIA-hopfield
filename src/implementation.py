import sys
import numpy as np

from src.gui.interface import Ui_MainWindow
from src.gui.weightMatrix import Ui_MatrizGeneralPesos
from src.gui.utils.table import TableModel
from src.gui.utils.fileDialog import openFileNameDialog

from src.funcs.hopfield import learn, searchPattern
from src.funcs.transforms import transformVector, transformVectors

from PyQt5 import QtCore, QtGui, QtWidgets

class UseHopfield(Ui_MainWindow):
    def __init__(self, patternWidth, patternHeight):
        self.vectors = []
        self.patternWidth = patternWidth
        self.patternHeight = patternHeight
        self.generalWeightMatrix = []
        self.incompletePattern = []

        self.app = QtWidgets.QApplication([])
        self.mainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.mainWindow)
        self.gridLayoutImages = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)

        self.disableBtns()
        self.actions()

    def actions(self):
        self.btnPatrones.clicked.connect(self.selectPatterns)
        self.btnAprender.clicked.connect(self.learn)
        self.btnPatronIncompleto.clicked.connect(self.selectIncompletePattern)
        self.btnResultado.clicked.connect(self.getResult)
        self.btnMatriz.clicked.connect(self.openMatrixGeneral)

    def selectPatterns(self):
        files = openFileNameDialog(1)
        if files:
            self.showImages(files)
            self.vectors = transformVectors(files)
            self.btnAprender.setDisabled(False)

    def learn(self):
        self.generalWeightMatrix = learn(self.patternWidth, self.patternHeight, np.array(self.vectors))
        self.btnMatriz.setDisabled(False)
        self.btnPatronIncompleto.setDisabled(False)

    def getResult(self):
        self.mplResultado.getPattern().updateGraph(searchPattern(self.incompletePattern, self.generalWeightMatrix))

    def selectIncompletePattern(self):
        file = openFileNameDialog(0)
        if file:
            self.incompletePattern = transformVector(file)
            self.mplPatronIncompleto.getPattern().updateGraph(self.incompletePattern)
            self.btnResultado.setDisabled(False)

    def openMatrixGeneral(self):
        self.window = QtWidgets.QWidget()
        self.matrixWindow = Ui_MatrizGeneralPesos()
        self.matrixWindow.setupUi(self.window)
        self.model = TableModel(self.generalWeightMatrix.tolist())
        self.matrixWindow.matrizGeneralPesos.setModel(self.model)
        self.window.show()

    def showImages(self, files):
        self.clearImages()
        amount = int(len(files)/2) + 1
        positions = [(i,j) for i in range(amount) for j in range(amount)]
        for position, file in zip(positions, files):
            im = QtGui.QPixmap(file)
            pixi = im.scaled(32, 32, QtCore.Qt.KeepAspectRatio)
            label = QtWidgets.QLabel()
            label.setPixmap(pixi)
            self.gridLayoutImages.addWidget(label,*position)

    def clearImages(self):
        while self.gridLayoutImages.count():
            child = self.gridLayoutImages.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def disableBtns(self):
        self.btnAprender.setDisabled(True)
        self.btnMatriz.setDisabled(True)
        self.btnPatronIncompleto.setDisabled(True)
        self.btnResultado.setDisabled(True)

    def showUi(self):
        self.mainWindow.show()
        sys.exit(self.app.exec_())

def run():
    app = UseHopfield(5, 5)
    app.showUi()