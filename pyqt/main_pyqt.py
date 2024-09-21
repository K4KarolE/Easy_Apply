from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QScrollArea,
    QMainWindow
    )

import sys

from src import (
    cv,
    db,
    MyButton,
    MyTextLine,
    MyTextField,
    MyScrollBar,
    MyTitle
)




''' APP '''
app = QApplication(sys.argv)


'''
QSCROLLAREA WINDOW <-- QWIDGET WINDOW <-- QWIDGETS
'''
# MAIN / QSCROLL AREA WINDOW
window_main = QScrollArea()
window_main.setWindowTitle("Easy Apply")
window_main.setWindowIcon(QIcon('pictures/icon.ico'))
window_main.setStyleSheet(f"background-color: {cv.BACKGROUND_COLOR};")


# QWIDGET WINDOW
cv.window_widgets = QMainWindow()
cv.window_widgets.setStyleSheet(f"background-color: {cv.BACKGROUND_COLOR};") 


''' SCROLL BARS '''
MyScrollBar(window_main)



''' WIDGETS '''
def y_location(gap):
    location = Y_BASE + 40 * gap
    return location

## PACING
Y_BASE=40
X_LEFT_SIDE_BASE = 25
X_LEFT_SIDE_FIELD = X_LEFT_SIDE_BASE + 30

# NAME
MyTitle(X_LEFT_SIDE_BASE, y_location(0), 'NAME')
# FIRST NAME
MyTextLine(X_LEFT_SIDE_FIELD, y_location(1),'name', 'mixed','first_name')
MyButton(X_LEFT_SIDE_BASE, y_location(1), cv.dic['mixed']['first_name'])
# LAST NAME
PUSH = 150
MyTextLine(X_LEFT_SIDE_FIELD + PUSH, y_location(1), 'name', 'mixed','last_name')
MyButton(X_LEFT_SIDE_BASE + PUSH, y_location(1), cv.dic['mixed']['last_name'])


# INTRO
MyTitle(X_LEFT_SIDE_BASE, y_location(2), 'INTRO')
MyTextField(X_LEFT_SIDE_FIELD, y_location(3), 'intro','mixed','intro')
MyButton(X_LEFT_SIDE_BASE, y_location(3), cv.dic['mixed']['intro'])


# EXPEREIENCE
MyTitle(X_LEFT_SIDE_BASE, y_location(7), 'EXPERIENCE')

n = 8
X_LEFT_SIDE_FIELD_2nd = X_LEFT_SIDE_FIELD + 300
X_LEFT_SIDE_BASE_2nd = X_LEFT_SIDE_BASE + 300
for key in db["experience"]:
    MyTextLine(X_LEFT_SIDE_FIELD, y_location(n), 'long', 'experience', key, 'title')
    MyButton(X_LEFT_SIDE_BASE, y_location(n), cv.dic['experience'][key]['title'])
    
    MyTextLine(X_LEFT_SIDE_FIELD_2nd, y_location(n), 'date', 'experience', key, 'from')
    MyButton(X_LEFT_SIDE_BASE_2nd, y_location(n), cv.dic['experience'][key]['from'])

    MyTextLine(X_LEFT_SIDE_FIELD, y_location(n+1), 'long', 'experience', key, 'company')
    MyButton(X_LEFT_SIDE_BASE, y_location(n+1), cv.dic['experience'][key]['company'])
    
    MyTextLine(X_LEFT_SIDE_FIELD_2nd, y_location(n+1), 'date', 'experience', key, 'to')
    MyButton(X_LEFT_SIDE_BASE_2nd, y_location(n+1), cv.dic['experience'][key]['to'])

    MyTextField(X_LEFT_SIDE_FIELD, y_location(n+2), 'job_description', 'experience', key, 'description')
    MyButton(X_LEFT_SIDE_BASE, y_location(n+2), cv.dic['experience'][key]['description'])

    n += 9

window_widgets_height = y_location(n)





 
window_main.resize(cv.WINDOW_WIDTH, cv.WINDOW_HEIGHT)
cv.window_widgets.resize(cv.WINDOW_WIDTH, window_widgets_height)

window_main.setWidget(cv.window_widgets)
window_main.show()

sys.exit(app.exec())

