from PyQt5 import QtCore, QtGui, QtWidgets

def openFileNameDialog(opt):
    options = QtWidgets.QFileDialog.Options()
    if opt == 0:
        files, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "QFileDialog.getOpenFileName()", "", "Image Files (*.png *.jpg *.jpeg)", options=options)
    else:
        files, _ = QtWidgets.QFileDialog.getOpenFileNames(
            None, "QFileDialog.getOpenFileNames()", "", "Image Files (*.png *.jpg *.jpeg)", options=options)
    if files:
        return files
    return []