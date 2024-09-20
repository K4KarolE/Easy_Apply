from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QIcon

from .data import cv


class MyMessageBox(QMessageBox):
    '''
        Used for the 2nd button of the Skills text field
        when the skills copied to the clipboard separately
    '''
    def __init__(self, message):
        super().__init__()
        self.setWindowTitle('Skills')
        self.setWindowIcon(QIcon('pictures/icon.ico'))
        self.setIcon(QMessageBox.Icon.Information)
        self.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.move(cv.SKILLS_POP_UP_WINDOW_POS_X, cv.SKILLS_POP_UP_WINDOW_POS_Y)
        self.setText(f'Skill in the clipborad:  {message}        ')
        self.exec()
