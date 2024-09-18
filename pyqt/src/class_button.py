from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt

from .class_data import cv


class MyButton(QPushButton):
    def __init__(self, window, pos_x, pos_y, func):
        super().__init__()
        self.setParent(window)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.clicked.connect(lambda: func())
        self.setGeometry(pos_x, pos_y, 40, 40)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setStyleSheet(
                    "QPushButton"
                        "{"
                        f"background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 0.3 {cv.BACKGROUND_COLOR}, stop: 0.6 {cv.BACKGROUND_COLOR}, stop: 1 {cv.FIELD_BACKGROUND_COLOR} );"
                        "border-radius: 5px;"
                        "border: 2px solid black;"
                        "}"

                    "QPushButton::pressed"
                        "{"
                        f"background-color : {cv.FIELD_BACKGROUND_COLOR};"
                        "}"
                    )