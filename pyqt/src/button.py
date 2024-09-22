from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt

import pyperclip

from .data import cv, db, save_db
from .message_box import MyMessageBox, MyWarningMessageBox


class MyButton(QPushButton):
    def __init__(self, pos_x, pos_y, input_field):
        super().__init__()
        button_size = cv.BUTTON_AND_LINE_FIELD_HEIGHT
        self.input_field = input_field
        self.setParent(cv.window_widgets)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setGeometry(pos_x, pos_y, button_size, button_size)
        self.setStyleSheet(
                    "QPushButton"
                        "{"
                        f"background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 0.3 {cv.BACKGROUND_COLOR}, stop: 0.6 {cv.BACKGROUND_COLOR}, stop: 1 {cv.FIELD_BACKGROUND_COLOR} );"
                        "border-radius: 2px;"
                        "border: 2px solid black;"
                        "}"

                    "QPushButton::pressed"
                        "{"
                        f"background-color : {cv.FIELD_BACKGROUND_COLOR};"
                        "}"
                    )
        # MyTextLine(QLineEdit), MyTextField(QTextEdit) have diff. copy methods
        if "MyTextLine" in str(input_field.__class__):
            self.clicked.connect(lambda: pyperclip.copy(self.input_field.text()))
        else:
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



class MySaveButton(QPushButton):
    def __init__(self, pos_x, pos_y, width, height):
        super().__init__()
        self.obj: object = None
        self.setText("SAVE")
        self.setParent(cv.window_widgets)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setGeometry(pos_x, pos_y, width, height)
        self.setStyleSheet(
                    "QPushButton"
                        "{"
                        f"background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 0.2 {cv.BACKGROUND_COLOR}, stop: 0.7 {cv.BACKGROUND_COLOR}, stop: 1 {cv.FIELD_BACKGROUND_COLOR} );"
                        "border-radius: 2px;"
                        "border: 2px solid black;"
                        "color:white;"
                        "font: 12pt Candara;"
                        "font-weight: bold;"
                        "}"

                    "QPushButton::pressed"
                        "{"
                        f"background-color : {cv.FIELD_BACKGROUND_COLOR};"
                        "}"
                    )
        self.clicked.connect(lambda: self.save())
 

    def save(self):
        try:
            for key in cv.dic:
                if key in 'mixed contacts'.split():
                    for sub_key in cv.dic[key]:
                        self.obj = cv.dic[key][sub_key]
                        db[key][sub_key] = self.get_text()
                
                else:
                    for sub_key in cv.dic[key]:
                        for sub_key_snd in cv.dic[key][sub_key]:
                            self.obj = cv.dic[key][sub_key][sub_key_snd]
                            db[key][sub_key][sub_key_snd] = self.get_text()
            save_db()
        except:
            MyWarningMessageBox()


    def get_text(self):
        if "MyTextLine" in str(self.obj.__class__):
            return self.obj.text()
        else:
            return self.obj.toPlainText()


    
