from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QScrollArea,
    QScrollBar,
    QMainWindow
    )


import sys
import pyperclip


from src import (
    cv,
    MyButton
)




''' APP '''
app = QApplication(sys.argv)


'''
QSCROLLAREA WINDOW <-- QWIDGET WINDOW <-- QWIDGETS
'''
# MAIN / QSCROLL AREA WINDOW
window_main = QScrollArea()
window_main.setWindowTitle(cv.WINDOW_TITLE)
window_main.setWindowIcon(QIcon('pictures/icon.ico'))
window_main.setStyleSheet(f"background-color: {cv.BACKGROUND_COLOR};") 


# QWIDGET WINDOW
window_widgets = QMainWindow()
window_widgets.setStyleSheet(f"background-color: {cv.BACKGROUND_COLOR};") 


''' SCROLL BARS '''
scroll_bar_ver = QScrollBar()
scroll_bar_ver.setStyleSheet(
                            "QScrollBar::vertical"
                                "{"
                                "width: 10px;"
                                "}"
                            )

scroll_bar_hor = QScrollBar()
scroll_bar_hor.setStyleSheet(
                            "QScrollBar::horizontal"
                                "{"
                                "height: 10px;"
                                "}"
                            )

window_main.setVerticalScrollBar(scroll_bar_ver)
window_main.setHorizontalScrollBar(scroll_bar_hor)



''' WIDGETS '''
def button_test():
    print("\nTEST\n")

testb = MyButton(window_widgets, 60, 60, button_test)




window_main.resize(cv.WINDOW_WIDTH, cv.WINDOW_HEIGHT)
window_widgets.resize(cv.WINDOW_WIDTH, cv.WINDOW_HEIGHT)

window_main.setWidget(window_widgets)
window_main.show()

sys.exit(app.exec())

