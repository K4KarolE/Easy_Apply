from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt

import pyperclip

from .data import cv
from .message_box import MyMessageBox


class MyButton(QPushButton):
    def __init__(self, pos_x, pos_y, input_field):
        super().__init__()
        self.input_field = input_field
        self.setParent(cv.window_widgets)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        button_size = 30
        self.setGeometry(pos_x, pos_y, button_size, button_size)
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
        self.clicked.connect(lambda: pyperclip.copy(self.input_field.toPlainText()))
    


    def copy_skills_separately(self):
        '''
            Used for the 2nd button of the Skills text field
            when the skills copied to the clipboard separately
        '''
        skill_list = self.input_field.toPlainText().split('\n')
        for skill in skill_list:
            if skill != '':
                skill = skill.strip('\u2022')
                pyperclip.copy(skill)
                MyMessageBox(skill)
