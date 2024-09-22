from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QTextEdit, QLineEdit

from .data import cv, db


class MyTextLine(QLineEdit):
    def __init__(self, pos_x, pos_y, field_type, dic_key, sub_key, sub_key_2nd = None):
        super().__init__()
        self.dic_key = dic_key
        self.sub_key = sub_key
        self.sub_key_2nd = sub_key_2nd
        self.setParent(cv.window_widgets)
        self.setCursor(Qt.CursorShape.IBeamCursor)
        self.setFont(QFont(cv.TEXT_FIELD_FONT_STYLE, cv.TEXT_FIELD_FONT_SIZE, 500))
        self.setStyleSheet(
                        f"background-color: {cv.FIELD_BACKGROUND_COLOR};"
                        "border-radius: 2px;"
                        "border: 2px solid black;"
                        f"color: {cv.TEXT_FIELD_FONT_COLOR};"
                        )
        field_height = cv.BUTTON_AND_LINE_FIELD_HEIGHT
        size_dic = {
            'name': [100, field_height],
            'date': [100, field_height],
            'long': [250, field_height],    # job title, company, school
        }
        self.setGeometry(pos_x, pos_y, size_dic[field_type][0], size_dic[field_type][1])
        self.set_text_and_place_object_to_dic()

    
    def set_text_and_place_object_to_dic(self):
        if self.sub_key_2nd:
            text = db[self.dic_key][self.sub_key][self.sub_key_2nd]
            cv.dic[self.dic_key][self.sub_key][self.sub_key_2nd] = self
        else:
            text = db[self.dic_key][self.sub_key]
            cv.dic[self.dic_key][self.sub_key] = self
        self.setText(text)



class MyTextField(QTextEdit):
    def __init__(self, pos_x, pos_y, field_type, dic_key, sub_key, sub_key_2nd = None):
        super().__init__()
        self.dic_key = dic_key
        self.sub_key = sub_key
        self.sub_key_2nd = sub_key_2nd
        self.setParent(cv.window_widgets)
        self.setCursor(Qt.CursorShape.IBeamCursor)
        self.setFont(QFont(cv.TEXT_FIELD_FONT_STYLE, cv.TEXT_FIELD_FONT_SIZE, 500))
        self.setStyleSheet(
                        f"background-color: {cv.FIELD_BACKGROUND_COLOR};"
                        "border-radius: 2px;"
                        "border: 2px solid black;"
                        f"color: {cv.TEXT_FIELD_FONT_COLOR};"
                        )
        size_dic = {
            'intro': [cv.INTRO_AND_JOBDESC_WIDTH, 105],
            'job_description': [cv.INTRO_AND_JOBDESC_WIDTH, 250],
            'bulk': [250, 200], # skills
            'bulk_tall': [250, 325] 
        }
        self.setGeometry(pos_x, pos_y, size_dic[field_type][0], size_dic[field_type][1])
        self.set_text_and_place_object_to_dic()

    
    def set_text_and_place_object_to_dic(self):
        if self.sub_key_2nd:
            text = db[self.dic_key][self.sub_key][self.sub_key_2nd]
            cv.dic[self.dic_key][self.sub_key][self.sub_key_2nd] = self
        else:
            text = db[self.dic_key][self.sub_key]
            cv.dic[self.dic_key][self.sub_key] = self
        self.setText(text)