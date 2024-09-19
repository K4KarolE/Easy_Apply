from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QScrollArea,
    QMainWindow
    )


import sys


from src import (
    cv,
    MyButton,
    MyTextField,
    MyScrollBar
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
cv.window_widgets = QMainWindow()
cv.window_widgets.setStyleSheet(f"background-color: {cv.BACKGROUND_COLOR};") 


''' SCROLL BARS '''
MyScrollBar(window_main)



''' WIDGETS '''
testql = MyTextField(120, 80, "job_description", "hello")
testb = MyButton(60, 80, testql)





window_main.resize(cv.WINDOW_WIDTH, cv.WINDOW_HEIGHT)
cv.window_widgets.resize(cv.WINDOW_WIDTH, cv.WINDOW_HEIGHT)

window_main.setWidget(cv.window_widgets)
window_main.show()

sys.exit(app.exec())

