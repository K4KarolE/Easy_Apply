from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel

from .data import cv


class MyTitle(QLabel):
    def __init__(self, pos_x, pos_y, text):
        super().__init__()
        self.setParent(cv.window_widgets)
        self.setText(text)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.move(pos_x, pos_y)
        self.setStyleSheet(
            "color:white;"
            "font: 20pt Candara;"
            "font-weight: bold;"
            )