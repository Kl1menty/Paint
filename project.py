from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Paint(object):
    def setupUi(self, Paint):
        Paint.setObjectName("Paint")
        Paint.resize(1080, 720)
        Paint.setMinimumSize(QtCore.QSize(0, 0))
        Paint.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Paint.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Paint)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.grp_parameters = QtWidgets.QGroupBox(self.centralwidget)
        self.grp_parameters.setMinimumSize(QtCore.QSize(300, 0))
        self.grp_parameters.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.grp_parameters.setFont(font)
        self.grp_parameters.setStyleSheet("background-color: rgb(3, 134, 129);\n"
"color: rgb(255, 255, 255);")
        self.grp_parameters.setObjectName("grp_parameters")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.grp_parameters)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_pen_color = QtWidgets.QPushButton(self.grp_parameters)
        self.btn_pen_color.setMinimumSize(QtCore.QSize(0, 60))
        self.btn_pen_color.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 30px;")
        self.btn_pen_color.setText("")
        self.btn_pen_color.setObjectName("btn_pen_color")
        self.verticalLayout_2.addWidget(self.btn_pen_color)
        self.lbl_pen = QtWidgets.QLabel(self.grp_parameters)
        self.lbl_pen.setMaximumSize(QtCore.QSize(16777215, 60))
        self.lbl_pen.setStyleSheet("font: 16px Arial;")
        self.lbl_pen.setObjectName("lbl_pen")
        self.verticalLayout_2.addWidget(self.lbl_pen, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_1.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_canvas_color = QtWidgets.QPushButton(self.grp_parameters)
        self.btn_canvas_color.setMinimumSize(QtCore.QSize(0, 60))
        self.btn_canvas_color.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.btn_canvas_color.setText("")
        self.btn_canvas_color.setObjectName("btn_canvas_color")
        self.verticalLayout_3.addWidget(self.btn_canvas_color)
        self.lbl_canvas = QtWidgets.QLabel(self.grp_parameters)
        self.lbl_canvas.setMaximumSize(QtCore.QSize(16777215, 60))
        self.lbl_canvas.setStyleSheet("font: 16px Arial;")
        self.lbl_canvas.setObjectName("lbl_canvas")
        self.verticalLayout_3.addWidget(self.lbl_canvas, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_1.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, 10, 0, -1)
        self.horizontalLayout_4.setSpacing(7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_set_image = QtWidgets.QPushButton(self.grp_parameters)
        self.btn_set_image.setMinimumSize(QtCore.QSize(135, 60))
        self.btn_set_image.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_set_image.setFont(font)
        self.btn_set_image.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 64, 65);\n"
"    border-radius: 20px;\n"
"    font: 23px Arial;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 89, 92);\n"
"    border-radius: 20px;\n"
"    font: 23px Arial;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(3, 134, 129);\n"
"    border-radius: 20px;\n"
"    font: 23px Arial;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.btn_set_image.setObjectName("btn_set_image")
        self.horizontalLayout_4.addWidget(self.btn_set_image)
        self.btn_pen_width = QtWidgets.QPushButton(self.grp_parameters)
        self.btn_pen_width.setMinimumSize(QtCore.QSize(100, 60))
        self.btn_pen_width.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_pen_width.setFont(font)
        self.btn_pen_width.setStyleSheet("QPushButton{\n"
"    background-color: rgb(52, 255, 215);\n"
"    border-radius: 20px;\n"
"    font: 28px Arial;\n"
"    color: rgb(0, 47, 48);\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(42, 209, 176);\n"
"    border-radius: 20px;\n"
"    font: 28px Arial;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(3, 134, 129);\n"
"    border-radius: 20px;\n"
"    font: 28px Arial;\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.btn_pen_width.setObjectName("btn_pen_width")
        self.horizontalLayout_4.addWidget(self.btn_pen_width, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btn_eraser_width = QtWidgets.QPushButton(self.grp_parameters)
        self.btn_eraser_width.setMinimumSize(QtCore.QSize(100, 60))
        self.btn_eraser_width.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_eraser_width.setFont(font)
        self.btn_eraser_width.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"    font: 28px Arial;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(155, 214, 215);\n"
"    border-radius: 20px;\n"
"    font: 28px Arial;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(3, 134, 129);\n"
"    border-radius: 20px;\n"
"    font: 28px Arial;\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.btn_eraser_width.setObjectName("btn_eraser_width")
        self.horizontalLayout_6.addWidget(self.btn_eraser_width, 0, QtCore.Qt.AlignLeft)
        self.btn_eraser = QtWidgets.QPushButton(self.grp_parameters)
        self.btn_eraser.setMinimumSize(QtCore.QSize(100, 60))
        self.btn_eraser.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_eraser.setFont(font)
        self.btn_eraser.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"    font: 23px Arial;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(155, 214, 215);\n"
"    border-radius: 20px;\n"
"    font: 23px Arial;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(3, 134, 129);\n"
"    border-radius: 20px;\n"
"    font: 23px Arial;\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.btn_eraser.setObjectName("btn_eraser")
        self.horizontalLayout_6.addWidget(self.btn_eraser, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 25, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btn_back = QtWidgets.QPushButton(self.grp_parameters)
        self.btn_back.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_back.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet("QPushButton{\n"
"    background-color: rgb(52, 255, 215);\n"
"    border-radius: 20px;\n"
"    color: rgb(0, 47, 48);\n"
"    font: 18px Arial;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(42, 209, 176);\n"
"    border-radius: 20px;\n"
"    font: 18px Arial;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(3, 134, 129);\n"
"    border-radius: 20px;\n"
"    font: 18px Arial;\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout_7.addWidget(self.btn_back, 0, QtCore.Qt.AlignLeft)
        self.btn_clear = QtWidgets.QPushButton(self.grp_parameters)
        self.btn_clear.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_clear.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 64, 65);\n"
"    border-radius: 20px;\n"
"    font: 18px Arial;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 89, 92);\n"
"    border-radius: 20px;\n"
"    font: 18px Arial;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(3, 134, 129);\n"
"    border-radius: 20px;\n"
"    font: 18px Arial;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout_7.addWidget(self.btn_clear, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_forward = QtWidgets.QPushButton(self.grp_parameters)
        self.btn_forward.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_forward.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_forward.setFont(font)
        self.btn_forward.setStyleSheet("QPushButton{\n"
"    background-color: rgb(52, 255, 215);\n"
"    border-radius: 20px;\n"
"    color: rgb(0, 47, 48);\n"
"    font: 18px Arial;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(42, 209, 176);\n"
"    border-radius: 20px;\n"
"    font: 18px Arial;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(3, 134, 129);\n"
"    border-radius: 20px;\n"
"    font: 18px Arial;\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.btn_forward.setObjectName("btn_forward")
        self.horizontalLayout_8.addWidget(self.btn_forward, 0, QtCore.Qt.AlignLeft)
        self.btn_return = QtWidgets.QPushButton(self.grp_parameters)
        self.btn_return.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_return.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_return.setFont(font)
        self.btn_return.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 64, 65);\n"
"    border-radius: 20px;\n"
"    font: 18px Arial;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 89, 92);\n"
"    border-radius: 20px;\n"
"    font: 18px Arial;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(3, 134, 129);\n"
"    border-radius: 20px;\n"
"    font: 18px Arial;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.btn_return.setObjectName("btn_return")
        self.horizontalLayout_8.addWidget(self.btn_return, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.btn_save = QtWidgets.QPushButton(self.grp_parameters)
        self.btn_save.setMinimumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_save.setFont(font)
        self.btn_save.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 64, 65);\n"
"    border-radius: 30px;\n"
"    font: 28px Arial;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 89, 92);\n"
"    border-radius: 30px;\n"
"    font: 28px Arial;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(3, 134, 129);\n"
"    border-radius: 30px;\n"
"    font: 28px Arial;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.btn_save.setObjectName("btn_save")
        self.verticalLayout_5.addWidget(self.btn_save, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.grp_parameters, 0, QtCore.Qt.AlignRight)
        Paint.setCentralWidget(self.centralwidget)

        self.retranslateUi(Paint)
        QtCore.QMetaObject.connectSlotsByName(Paint)

    def retranslateUi(self, Paint):
        _translate = QtCore.QCoreApplication.translate
        Paint.setWindowTitle(_translate("Paint", "MainWindow"))
        self.grp_parameters.setTitle(_translate("Paint", "Параметры"))
        self.lbl_pen.setText(_translate("Paint", "Цвет кисти"))
        self.lbl_canvas.setText(_translate("Paint", "Цвет фона"))
        self.btn_set_image.setText(_translate("Paint", "Картинка"))
        self.btn_pen_width.setText(_translate("Paint", "5"))
        self.btn_eraser_width.setText(_translate("Paint", "50"))
        self.btn_eraser.setText(_translate("Paint", "Ластик"))
        self.btn_back.setText(_translate("Paint", "Назад"))
        self.btn_clear.setText(_translate("Paint", "Очистить"))
        self.btn_forward.setText(_translate("Paint", "Вперед"))
        self.btn_return.setText(_translate("Paint", "Вернуть"))
        self.btn_save.setText(_translate("Paint", "Сохранить"))
