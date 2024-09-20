from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTextEdit

from .data import cv


class MyTextField(QTextEdit):
    def __init__(self, pos_x, pos_y, field_type, text):
        super().__init__()
        self.setParent(cv.window_widgets)
        self.setCursor(Qt.CursorShape.IBeamCursor)
        self.setFont(QFont(cv.TEXT_FIELD_FONT_STYLE, cv.TEXT_FIELD_FONT_SIZE, 500))
        self.setText(text)
        self.setStyleSheet(
                        f"background-color: {cv.FIELD_BACKGROUND_COLOR};"
                        "border-radius: 2px;"
                        "border: 2px solid black;"
                        f"color: {cv.TEXT_FIELD_FONT_COLOR};"
                        )
        field_height = 40
        size_dic = {
            'intro': [cv.WINDOW_WIDTH-pos_x*2, 150],
            'name': [150, field_height],
            'date': [120, field_height],
            'long': [200, field_height],    # job title, company, school
            'job_description': [200, 150],
            'bulk': [200, 150], # skills, achivements, extra 
        }
        self.setGeometry(pos_x, pos_y, size_dic[field_type][0], size_dic[field_type][1])