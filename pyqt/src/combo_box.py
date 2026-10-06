from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QComboBox

import pyperclip

from .data import cv


class MyComboBox(QComboBox):
    def __init__(self, pos_x, pos_y, width, height):
        super().__init__()
        self.setParent(cv.window_widgets)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setGeometry(pos_x, pos_y, width, height)
        self.setFont(QFont(cv.TEXT_FIELD_FONT_STYLE, cv.TEXT_FIELD_FONT_SIZE - 2, 600))
        self.items_list = list(cv.dic['contacts'].keys())
        self.items_list.append('-')
        self.addItems(self.items_list)
        self.setCurrentIndex(self.items_list.index(cv.dic['selected_contact_to_clipboard_at_startup']))
        self.setToolTip('At startup it copies the selected CONTACTS field value to clipboard')
        if self.currentText() != '-':
            pyperclip.copy(cv.dic['contacts'][self.currentText()].text())
        cv.dic['selected_contact_object'] = self
        self.setEditable(True)
        self.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit().setReadOnly(True)
        self.setStyleSheet(
            "QComboBox"
                "{"
                f"background: {cv.FIELD_BACKGROUND_COLOR};"
                "border-radius: 2px;"
                "border: 2px solid black;"
                f"color: {cv.TEXT_FIELD_FONT_COLOR};"
                "}"
            "QListView::item:hover"  # after roll-down - menu
                "{"
                f"background-color: {cv.TEXT_FIELD_FONT_COLOR};"
                f"color: {cv.FIELD_BACKGROUND_COLOR};"
                "}"
            "QListView::item"  # after roll-down - menu
                "{"
                f"background: {cv.FIELD_BACKGROUND_COLOR};"
                f"color: {cv.TEXT_FIELD_FONT_COLOR};"
                "}"
            "QListView::item:selected"  # after roll-down - selected
                "{"
                f"background: {cv.TEXT_FIELD_FONT_COLOR};"
                f"color: {cv.FIELD_BACKGROUND_COLOR};"
                "}"
            "QAbstractItemView"  # after roll-down - selected
                "{"
                "outline: 0px;"
                "}"
        )