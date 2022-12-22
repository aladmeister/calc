import math
import sys
from PySide6 import QtCore
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from Интерфейсы.calc.calc import quadratic_equation, distance_between_points


class DistanceBetweenDotsWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.build()
        self.menu = MenuWindow()

    def build(self):
        self.setWindowTitle("Distance between dots")

        self.setFixedSize(QSize(350, 700))
        self.layout = QGridLayout(self)

        self.GroshCalculatorLabel = QLabel('GroshCalculator', self)
        self.GroshCalculatorLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.GroshCalculatorLabel.setStyleSheet(
            "color: #007ba7; font: bold italic 24px; height: 50px; margin-left: 20px; margin-right: 20px;")
        self.layout.addWidget(self.GroshCalculatorLabel, 0, 0, 1, 3)

        self.menuButton = QPushButton('Назад', self)
        self.menuButton.clicked.connect(self.menuButton_clicked)
        self.menuButton.setStyleSheet(
            "background-color: #FFAF66; font: bold italic 24px; font-weight: 600; height: 78px; margin-left: 40px; margin-right: 40px;")
        self.layout.addWidget(self.menuButton, 1, 0, 1, 3)

        self.additionDivisionLabel = QLabel('Расстояние между\nточками', self)
        self.additionDivisionLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.additionDivisionLabel.setStyleSheet(
            "font: bold italic 24px; font-weight: 700; height: 50px; margin-left: 40px; margin-right: 40px;")
        self.layout.addWidget(self.additionDivisionLabel, 2, 0, 1, 3)

        self.xALabel = QLabel('xA', self)
        self.xALabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.xALabel.setStyleSheet("font: bold 40px; font-weight: 700; height: 50px;")
        self.xALabel.move(29, 430)
        self.layout.addWidget(self.xALabel, 3, 1, 1, 1)

        self.xALineEdit = QLineEdit()
        self.xALineEdit.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.xALineEdit.setValidator(QRegularExpressionValidator(QRegularExpression('^-?\d*\.?\d+$')))
        self.xALineEdit.setStyleSheet("font: bold italic 24px; font-weight: 700; height: 50px;")
        self.layout.addWidget(self.xALineEdit, 3, 2, 1, 1)

        self.yALabel = QLabel('yA', self)
        self.yALabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.yALabel.setStyleSheet("font: bold 40px; font-weight: 700; height: 50px;")
        self.yALabel.move(29, 430)
        self.layout.addWidget(self.yALabel, 4, 1, 1, 1)

        self.yALineEdit = QLineEdit()
        self.yALineEdit.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.yALineEdit.setValidator(QRegularExpressionValidator(QRegularExpression('^-?\d*\.?\d+$')))
        self.yALineEdit.setStyleSheet("font: bold italic 24px; font-weight: 700; height: 50px;")
        self.layout.addWidget(self.yALineEdit, 4, 2, 1, 1)

        self.xBLabel = QLabel('xB', self)
        self.xBLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.xBLabel.setStyleSheet("font: bold 40px; font-weight: 700; height: 50px;")
        self.layout.addWidget(self.xBLabel, 6, 1, 1, 1)

        self.xBLineEdit = QLineEdit()
        self.xBLineEdit.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.xBLineEdit.setValidator(QRegularExpressionValidator(QRegularExpression('^-?\d*\.?\d+$')))
        self.xBLineEdit.setStyleSheet("font: bold italic 24px; font-weight: 700; height: 50px;")
        self.layout.addWidget(self.xBLineEdit, 6, 2, 1, 1)

        self.yBLabel = QLabel('yB', self)
        self.yBLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.yBLabel.setStyleSheet("font: bold 40px; font-weight: 700; height: 50px;")
        self.layout.addWidget(self.yBLabel, 7, 1, 1, 1)

        self.yBLineEdit = QLineEdit()
        self.yBLineEdit.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.yBLineEdit.setValidator(QRegularExpressionValidator(QRegularExpression('^-?\d*\.?\d+$')))
        self.yBLineEdit.setStyleSheet("font: bold italic 24px; font-weight: 700; height: 50px;")
        self.layout.addWidget(self.yBLineEdit, 7, 2, 1, 1)

        self.distance_between_points = QPushButton('Вычислить', self)
        self.distance_between_points.clicked.connect(self.distance_between_points_clicked)
        self.distance_between_points.setStyleSheet(
            "font: bold italic 24px; font-weight: 700; height: 75px; margin-left: 50px; margin-right: 50px;")
        self.layout.addWidget(self.distance_between_points, 9, 0, 1, 3)

        self.DistanceResult = QLineEdit('', self)
        self.DistanceResult.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.DistanceResult.setStyleSheet(
            "background-color: #FF7A00; font: bold italic 24px; font-weight: 700; height: 75px; margin-left: 50px; margin-right: 50px;")
        self.layout.addWidget(self.DistanceResult, 10, 0, 1, 3)
        self.DistanceResult.setReadOnly(True)

    def distance_between_points_clicked(self):
        x1 = float(self.xALineEdit.text())
        y1 = float(self.yALineEdit.text())
        x2 = float(self.xBLineEdit.text())
        y2 = float(self.yBLineEdit.text())
        self.DistanceResult.setText(f'{distance_between_points(x1, y1, x2, y2)}')

    def distance_between_points(self, x1, y1, x2, y2):
        result = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return result

    def closeEvent(self, event):
        event.accept()
        menu_window.addition_division_button.setEnabled(True)
        menu_window.quadratic_equation_button.setEnabled(True)
        menu_window.distance_between_dots_button.setEnabled(True)

    def menuButton_clicked(self):
        self.close()

    def show_msg_box(self, msg):
        msgBox = QMessageBox(self)
        msgBox.setText(msg)
        msgBox.exec()


class QuadraticEquationWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.build()
        self.menu = MenuWindow()

    def build(self):
        self.setWindowTitle("Quadratic equation")

        self.setFixedSize(QSize(350, 700))

        self.layout = QGridLayout(self)

        self.GroshCalculatorLabel = QLabel('GroshCalculator', self)
        self.GroshCalculatorLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.GroshCalculatorLabel.setStyleSheet(
            "color: #007ba7; font: bold italic 24px; height: 50px; margin-left: 20px; margin-right: 20px;")
        self.layout.addWidget(self.GroshCalculatorLabel, 0, 0, 1, 3)

        self.menuButton = QPushButton('Назад', self)
        self.menuButton.clicked.connect(self.menuButton_clicked)
        self.menuButton.setStyleSheet(
            "background-color: #FFAF66; font: bold italic 24px; font-weight: 600; height: 78px; margin-left: 40px; margin-right: 40px;")
        self.layout.addWidget(self.menuButton, 1, 0, 1, 3)

        self.additionDivisionLabel = QLabel('Квадратное уравнение', self)
        self.additionDivisionLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.additionDivisionLabel.setStyleSheet(
            "font: bold italic 24px; font-weight: 700; height: 50px; margin-left: 20px; margin-right: 20px;")
        self.layout.addWidget(self.additionDivisionLabel, 2, 0, 1, 3)

        self.quadratic_equation = QPushButton('Вычислить ax^2 + bx + c', self)
        self.quadratic_equation.clicked.connect(self.quadratic_equation_clicked)
        self.quadratic_equation.setStyleSheet(
            "color: black; border-radius: 0px; font: bold italic 20px; font-weight: 700; height: 75px; margin-left: 10px; margin-right: 10px;")
        self.layout.addWidget(self.quadratic_equation, 3, 0, 1, 3)

        self.aLabel = QLabel('a', self)
        self.aLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.aLabel.setStyleSheet("font: bold italic 24px; font-weight: 700; height: 35px;")
        self.layout.addWidget(self.aLabel, 4, 0, 1, 1)

        self.bLabel = QLabel('b', self)
        self.bLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.bLabel.setStyleSheet("font: bold italic 24px; font-weight: 700; height: 35px;")
        self.layout.addWidget(self.bLabel, 4, 1, 1, 1)

        self.cLabel = QLabel('c', self)
        self.cLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.cLabel.setStyleSheet("font: bold italic 24px; font-weight: 700; height: 35px;")
        self.layout.addWidget(self.cLabel, 4, 2, 1, 1)

        self.aResultLabel = QLineEdit()  # a
        self.aResultLabel.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.aResultLabel.setMaxLength(3)
        self.aResultLabel.setStyleSheet("font: bold 24px; font-weight: 700; height: 50px;")
        self.aResultLabel.setValidator(QRegularExpressionValidator(QRegularExpression('^-?\d*\.?\d+$')))
        self.layout.addWidget(self.aResultLabel, 5, 0, 1, 1)

        self.bResultLabel = QLineEdit()
        self.bResultLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.aResultLabel.setMaxLength(3)
        self.bResultLabel.setStyleSheet(
            "font: bold italic 24px; font-weight: 700; height: 50px;")
        self.bResultLabel.setValidator(QRegularExpressionValidator(QRegularExpression('^-?\d*\.?\d+$')))
        self.layout.addWidget(self.bResultLabel, 5, 1, 1, 1)

        self.cResultLabel = QLineEdit()
        self.cResultLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.aResultLabel.setMaxLength(3)
        self.cResultLabel.setStyleSheet(
            "font: bold italic 24px; font-weight: 700; height: 50px;")
        self.cResultLabel.setValidator(QRegularExpressionValidator(QRegularExpression('^-?\d*\.?\d+$')))
        self.layout.addWidget(self.cResultLabel, 5, 2, 1, 1)

        self.DLabel = QLabel('D', self)
        self.DLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.DLabel.setStyleSheet("font: bold 40px; font-weight: 700; height: 70px;")
        self.layout.addWidget(self.DLabel, 6, 0, 1, 1)

        self.DResultLabel = QLineEdit('', self)
        self.DResultLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.DResultLabel.setStyleSheet("background-color: #FF7A00; font: bold 24px; font-weight: 700; height: 75px;")
        self.layout.addWidget(self.DResultLabel, 6, 1, 1, 2)
        self.DResultLabel.setReadOnly(True)

        self.x1Label = QLabel('x1', self)
        self.x1Label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.x1Label.setStyleSheet("font: bold 40px; font-weight: 700; height: 70px;")
        self.layout.addWidget(self.x1Label, 7, 0, 1, 1)

        self.x1ResultLabel = QLineEdit('', self)
        self.x1ResultLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.x1ResultLabel.setStyleSheet("background-color: #FF7A00; font: bold 24px; font-weight: 700; height: 75px;")
        self.layout.addWidget(self.x1ResultLabel, 7, 1, 1, 2)
        self.x1ResultLabel.setReadOnly(True)

        self.x2Label = QLabel('x2', self)
        self.x2Label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.x2Label.setStyleSheet("font: bold 40px; font-weight: 700; height: 70px;")
        self.layout.addWidget(self.x2Label, 8, 0, 1, 1)

        self.x2ResultLabel = QLineEdit('', self)
        self.x2ResultLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.x2ResultLabel.setStyleSheet("background-color: #FF7A00; font: bold 24px; font-weight: 700; height: 75px;")
        self.layout.addWidget(self.x2ResultLabel, 8, 1, 1, 2)
        self.x2ResultLabel.setReadOnly(True)

    def quadratic_equation_clicked(self):
        a = float(self.aResultLabel.text())
        b = float(self.bResultLabel.text())
        c = float(self.cResultLabel.text())
        self.DResultLabel.setText(f'{quadratic_equation(a, b, c)}')
        self.x1ResultLabel.setText(f'{self.find_root_x1(a, b, c)}')
        self.x2ResultLabel.setText(f'{self.find_root_x2(a, b, c)}')

    def quadratic_equation(self, a, b, c):
        # рассчитываем дискриминант
        discriminant = b ** 2 - 4 * a * c
        return discriminant

    def find_root_x1(self, a, b, c):
        discriminant = b ** 2 - 4 * a * c
        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            return x1
        elif discriminant == 0:
            x1 = -b / (2 * a)
            return x1
        else:
            return "Нет решений"

    def find_root_x2(self, a, b, c):
        discriminant = b ** 2 - 4 * a * c
        if discriminant > 0 and a != 0:
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
            return x2
        elif discriminant == 0:
            return ''
        else:
            return "Нет решений"

    def closeEvent(self, event):
        event.accept()
        menu_window.addition_division_button.setEnabled(True)
        menu_window.quadratic_equation_button.setEnabled(True)
        menu_window.distance_between_dots_button.setEnabled(True)

    def menuButton_clicked(self):
        self.close()

    def show_msg_box(self, msg):
        msgBox = QMessageBox(self)
        msgBox.setText(msg)
        msgBox.exec()


class AdditionDivisionWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.build()
        self.menu = MenuWindow()

    def build(self):
        self.setWindowTitle("AdditionDivision")

        self.setFixedSize(QSize(350, 700))

        self.layout = QGridLayout(self)

        self.GroshCalculatorLabel = QLabel('GroshCalculator', self)
        self.GroshCalculatorLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.GroshCalculatorLabel.setStyleSheet(
            "color: #007ba7; font: bold italic 24px; height: 50px; margin-left: 20px; margin-right: 20px;")
        self.layout.addWidget(self.GroshCalculatorLabel, 0, 0, 1, 3)

        self.menuButton = QPushButton('Назад', self)
        self.menuButton.clicked.connect(self.menuButton_clicked)
        self.menuButton.setStyleSheet(
            "background-color: #FFAF66; font: bold italic 24px; font-weight: 600; height: 78px; margin-left: 40px; margin-right: 40px;")
        self.layout.addWidget(self.menuButton, 1, 0, 1, 3)

        self.additionDivisionLabel = QLabel('Сложение и деление', self)
        self.additionDivisionLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.additionDivisionLabel.setStyleSheet(
            "font: bold italic 24px; font-weight: 700; height: 50px; margin-left: 40px; margin-right: 40px;")
        self.layout.addWidget(self.additionDivisionLabel, 2, 0, 1, 3)

        self.numberOneLabel = QLabel('Число №1', self)
        self.numberOneLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.numberOneLabel.setStyleSheet(
            "font: bold italic 24px; font-weight: 700; height: 50px; margin-left: 40px; margin-right: 40px;")
        self.numberOneLabel.move(29, 430)
        self.layout.addWidget(self.numberOneLabel, 3, 0, 1, 3)

        self.numberOneLineEdit = QLineEdit()
        self.numberOneLineEdit.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.numberOneLineEdit.setMaxLength(10)
        self.numberOneLineEdit.setValidator(QRegularExpressionValidator(QRegularExpression('^-?\d*\.?\d+$')))
        self.numberOneLineEdit.setStyleSheet(
            "font: bold italic 24px; font-weight: 700; width: 250px; height: 75px; margin-left: 50px; margin-right: 50px;")
        self.layout.addWidget(self.numberOneLineEdit, 4, 0, 1, 3)

        self.additionButton = QPushButton('+', self)
        self.additionButton.clicked.connect(self.additionButton_clicked)
        self.additionButton.setStyleSheet(
            "background: rgba(255, 175, 102, 0.6); font: bold 40px; font-weight: 700; height: 50px;")
        self.layout.addWidget(self.additionButton, 5, 0, 1, 1)

        self.divisionButton = QPushButton('/', self)
        self.divisionButton.clicked.connect(self.divisionButton_clicked)
        self.divisionButton.setStyleSheet(
            "background: rgba(255, 175, 102, 0.6); font: bold 40px; font-weight: 700; height: 50px;")
        self.layout.addWidget(self.divisionButton, 5, 2, 1, 1)

        self.numberTwoLabel = QLabel('Число №2', self)
        self.numberTwoLabel.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.numberTwoLabel.setStyleSheet(
            "font: bold italic 24px; font-weight: 700; height: 50px; margin-left: 90px; margin-right: 40px;")
        self.layout.addWidget(self.numberTwoLabel, 6, 0, 1, 3)

        self.numberTwoLineEdit = QLineEdit()
        self.numberTwoLineEdit.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.numberTwoLineEdit.setMaxLength(10)
        self.numberTwoLineEdit.setValidator(QRegularExpressionValidator(QRegularExpression('^-?\d*\.?\d+$')))
        self.numberTwoLineEdit.setStyleSheet(
            "font: bold italic 24px; font-weight: 700; width: 250px; height: 75px; margin-left: 50px; margin-right: 50px;")
        self.layout.addWidget(self.numberTwoLineEdit, 7, 0, 1, 3)

        self.resultLabel = QLabel('Результат', self)
        self.resultLabel.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.resultLabel.setStyleSheet(
            "font: bold italic 24px; font-weight: 700; height: 50px; margin-left: 90px; margin-right: 40px;")
        self.layout.addWidget(self.resultLabel, 8, 0, 1, 3)

        self.resultValueLabel = QLineEdit('', self)
        self.resultValueLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.resultValueLabel.setStyleSheet(
            "background-color: #FF7A00; font: bold italic 24px; font-weight: 700; width: 250px; height: 75px; margin-left: 50px; margin-right: 50px;")
        self.layout.addWidget(self.resultValueLabel, 9, 0, 1, 3)
        self.resultValueLabel.setReadOnly(True)

    def additionButton_clicked(self):
        a = float(self.numberOneLineEdit.text())
        b = float(self.numberTwoLineEdit.text())
        self.resultValueLabel.setText(f'{self.addition(a, b)}')

    def addition(self, a, b):
        result = a + b
        return result

    def division(self, a, b):
        result = a / b
        return result

    def divisionButton_clicked(self):
        a = float(self.numberOneLineEdit.text())
        b = float(self.numberTwoLineEdit.text())
        self.resultValueLabel.setText(f'{self.division(a, b)}')

    def closeEvent(self, event):
        event.accept()
        menu_window.addition_division_button.setEnabled(True)
        menu_window.quadratic_equation_button.setEnabled(True)
        menu_window.distance_between_dots_button.setEnabled(True)

    def menuButton_clicked(self):
        self.close()

    def show_msg_box(self, msg):
        msgBox = QMessageBox(self)
        msgBox.setText(msg)
        msgBox.exec()


class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Menu")

        self.setFixedSize(QSize(350, 700))

        self.layout = QGridLayout(self)

        self.GroshCalculatorLabel = QLabel('GroshCalculator', self)
        self.GroshCalculatorLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.GroshCalculatorLabel.setFixedSize(QSize(300, 50))
        self.GroshCalculatorLabel.setStyleSheet("color: #007ba7; font: bold italic 24px;")
        self.layout.addWidget(self.GroshCalculatorLabel, 0, 0)

        self.chooseActionLabel = QLabel('Выберите\nоперацию', self)
        self.chooseActionLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.chooseActionLabel.setFixedSize(QSize(300, 75))
        self.chooseActionLabel.setStyleSheet("font: italic 32px; font-weight: 300px")
        self.layout.addWidget(self.chooseActionLabel, 1, 0)

        self.emptyLabel2 = QLabel('', self)
        self.layout.addWidget(self.emptyLabel2, 2, 0)

        self.addition_division_button = QPushButton('Сложение\nДеление', self)
        self.addition_division_button.clicked.connect(self.show_addition_division_window)
        self.addition_division_button.setFixedSize(QSize(300, 100))
        self.addition_division_button.setStyleSheet("font: bold italic 32px;")
        self.layout.addWidget(self.addition_division_button, 3, 0, 1, 1)

        self.emptyLabel1 = QLabel('', self)
        self.layout.addWidget(self.emptyLabel1, 4, 0)

        self.quadratic_equation_button = QPushButton('Квадратное\nуравнение', self)
        self.quadratic_equation_button.clicked.connect(self.show_quadratic_equation_window)
        self.quadratic_equation_button.setFixedSize(QSize(300, 100))
        self.quadratic_equation_button.setStyleSheet("font: bold italic 32px")
        self.layout.addWidget(self.quadratic_equation_button, 5, 0)

        self.emptyLabel2 = QLabel('', self)
        self.layout.addWidget(self.emptyLabel2, 6, 0)

        self.distance_between_dots_button = QPushButton('Расстояние\nмежду точками', self)
        self.distance_between_dots_button.clicked.connect(self.show_distance_between_dots_window)
        self.distance_between_dots_button.setFixedSize(QSize(300, 100))
        self.distance_between_dots_button.setStyleSheet("font: bold italic 32px")
        self.layout.addWidget(self.distance_between_dots_button, 7, 0)

        self.emptyLabel2 = QLabel('', self)
        self.layout.addWidget(self.emptyLabel2, 8, 0)

    def show_addition_division_window(self):
        self.addition_division_window = AdditionDivisionWindow(self)
        self.addition_division_window.show()
        self.disable_buttons()

    def show_quadratic_equation_window(self):
        self.quadratic_equation_window = QuadraticEquationWindow(self)
        self.quadratic_equation_window.show()
        self.disable_buttons()

    def show_distance_between_dots_window(self):
        self.distance_between_dots_window = DistanceBetweenDotsWindow(self)
        self.distance_between_dots_window.show()
        self.disable_buttons()

    def disable_buttons(self):
        self.addition_division_button.setEnabled(False)
        self.quadratic_equation_button.setEnabled(False)
        self.distance_between_dots_button.setEnabled(False)

    def show_msg_box(self, msg):
        msgBox = QMessageBox(self)
        msgBox.setText(msg)
        msgBox.exec()


FONT_FAMILY = "Inter"
BUTTON_STYLE = (
    "background-color: #FFAF66;"
    "border-style: outset;"
    "border-width: 2px;"
    "border-color: beige;"
)
HOVER_STYLE = "background-color: #FFAF66;"
PRESSED_STYLE = "background-color: #FFAF66;"
DISABLED_STYLE = "background-color: ;"
LINE_EDIT_STYLE = (
    "background-color: #FFC700;"
    "border-style: outset;"
    "border-width: 0px;"
    "border-radius: 0px;"
    "border-color: black;"
    "padding: 6px;"
)
STYLE_SHEET = (
    f"* {{ font-family: {FONT_FAMILY}; }}"
    f"QPushButton {{ {BUTTON_STYLE} }}"
    f"QPushButton:hover {{ {HOVER_STYLE} }}"
    f"QPushButton:pressed {{ {PRESSED_STYLE} }}"
    f"QPushButton:disabled {{ {DISABLED_STYLE} }}"
    f"QLineEdit {{ {LINE_EDIT_STYLE} }}"
)

if __name__ == "__main__":
    application = QApplication(sys.argv)
    application.setStyleSheet(STYLE_SHEET)
    menu_window = MenuWindow()
    menu_window.show()
    sys.exit(application.exec())
