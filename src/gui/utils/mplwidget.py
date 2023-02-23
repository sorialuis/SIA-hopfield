from PyQt5 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib

matplotlib.use('QT5Agg')

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=3, height=3, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)

    def graph(self, pattern):
        self.axes.matshow(pattern.reshape(5,5), cmap='binary')
    
    def updateGraph(self, pattern=[]):
        self.axes.clear()
        self.graph(pattern)
        self.draw()

class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.pattern = MplCanvas(self, width=3, height=3, dpi=100)
        self.vbl = QtWidgets.QVBoxLayout()
        self.vbl.addWidget(self.pattern)
        self.setLayout(self.vbl)

    def getPattern(self):
        return self.pattern