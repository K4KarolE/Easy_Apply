from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLineEdit, QTextEdit

from .data import cv


class MyTextField(QTextEdit):
    def __init__(self, pos_x, pos_y, field_type, text):
        super().__init__()
        self.setParent(cv.window_widgets)
        self.setCursor(Qt.CursorShape.IBeamCursor)
        self.setFont(QFont('Times', 15, 500))
        self.setText(text)
        self.setStyleSheet(
                        f"background-color: {cv.FIELD_BACKGROUND_COLOR};"
                        "border-radius: 2px;"
                        "border: 2px solid black;"
                        "color: white;"
                        )
        _field_height = 40
        _size_dic = {
            "intro": [cv.WINDOW_WIDTH-pos_x*2, 150],
            "name": [150, _field_height],
            "date": [120, _field_height],
            "job_description": [200, 150],
        }
        self.setGeometry(pos_x, pos_y, _size_dic[field_type][0], _size_dic[field_type][1])