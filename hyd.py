from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import res
import sys

from LSteg import LSBSteg, SteganographyException

class Ui_theClass(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, theClass):
        theClass.setObjectName("theClass")
        theClass.resize(500, 500)
        theClass.setMinimumSize(QtCore.QSize(500, 500))
        theClass.setMaximumSize(QtCore.QSize(500, 500))
        self.label = QtWidgets.QLabel(theClass)
        self.label.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/img/solarized-mountains-light.png"))
        self.label.setScaledContents(True)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(theClass)
        self.label_2.setGeometry(QtCore.QRect(0, -150, 500, 500))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/img/imageedit_1_8783843535.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.rb_encrypt = QtWidgets.QRadioButton(theClass)
        self.rb_encrypt.setGeometry(QtCore.QRect(190, 200, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rb_encrypt.setFont(font)
        self.rb_encrypt.setObjectName("rb_encrypt")
        self.rb_decrypt = QtWidgets.QRadioButton(theClass)
        self.rb_decrypt.setGeometry(QtCore.QRect(190, 240, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rb_decrypt.setFont(font)
        self.rb_decrypt.setObjectName("rb_decrypt")
        self.btn_encrypt = QtWidgets.QPushButton(theClass)
        self.btn_encrypt.setGeometry(QtCore.QRect(200, 450, 93, 28))
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.getPass = QtWidgets.QLineEdit(theClass)
        self.getPass.setGeometry(QtCore.QRect(190, 290, 113, 22))
        self.getPass.setObjectName("getPass")
        self.btn_getFile = QtWidgets.QPushButton(theClass)
        self.btn_getFile.setGeometry(QtCore.QRect(200, 400, 93, 28))
        self.btn_getFile.setObjectName("btn_getFile")
        self.getImg = QtWidgets.QPushButton(theClass)
        self.getImg.setGeometry(QtCore.QRect(200, 350, 93, 28))
        self.getImg.setObjectName("getImg")
        self.btn_decrypt = QtWidgets.QPushButton(theClass)
        self.btn_decrypt.setGeometry(QtCore.QRect(200, 450, 93, 28))
        self.btn_decrypt.setObjectName("btn_decrypt")
        self.label.raise_()
        self.label_2.raise_()
        self.rb_encrypt.raise_()
        self.rb_decrypt.raise_()
        self.getPass.raise_()
        self.btn_getFile.raise_()
        self.getImg.raise_()
        self.btn_decrypt.raise_()
        self.btn_encrypt.raise_()

        self.retranslateUi(theClass)
        self.rb_decrypt.clicked.connect(self.btn_decrypt.show)
        self.rb_decrypt.clicked.connect(self.btn_encrypt.hide)
        self.rb_encrypt.clicked.connect(self.btn_decrypt.hide)
        self.rb_encrypt.clicked.connect(self.btn_encrypt.show)
        self.rb_decrypt.clicked.connect(self.btn_getFile.hide)
        self.rb_encrypt.clicked.connect(self.btn_getFile.show)
        QtCore.QMetaObject.connectSlotsByName(theClass)

    def retranslateUi(self, theClass):
        _translate = QtCore.QCoreApplication.translate
        theClass.setWindowTitle(_translate("theClass", "Hide Your Data"))
        self.rb_encrypt.setText(_translate("theClass", "Encrypt"))
        self.rb_decrypt.setText(_translate("theClass", "Decrypt"))
        self.btn_encrypt.setText(_translate("theClass", "Encrypt"))
        self.getPass.setPlaceholderText(_translate("theClass", "password"))
        self.btn_getFile.setText(_translate("theClass", "File to hide"))
        self.getImg.setText(_translate("theClass", "PNG"))
        self.btn_decrypt.setText(_translate("theClass", "Decrypt"))

        self.btn_decrypt.clicked.connect(self.decrypt)
        self.btn_encrypt.clicked.connect(self.encrypt)
        self.getImg.clicked.connect(self.getImage)
        self.btn_getFile.clicked.connect(self.getTheFile)

    def encrypt(self):

        # password = str(self.lineEdit.text())
        # Steg.embed(self.img, self.f, password)
        steg = LSBSteg(cv2.imread(self.img))
        data = open(self.f, "rb").read()
        new_img = steg.encode_binary(data)

        filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File To', '/', "PNG(*.png)")

        cv2.imwrite(filename[0], new_img)

        self.f = self.img = 0

    def decrypt(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File To', '/', "Text(*.txt)")
        steg = LSBSteg(cv2.imread(self.img))
        binary = steg.decode_binary()
        with open(str(filename[0]), "w") as f:
            f.write(binary.decode("latin-1"))

        self.f = self.img = 0

    def getTheFile(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', '/')
        self.f = filename[0]


    def getImage(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', '/')
        print (filename[0])
        self.img = filename[0]


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_theClass()
    ex.show()
    sys.exit(app.exec_())
