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
    MySaveButton,
    MyScrollBar,
    MyTextLine,
    MyTextField,
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
Y_BASE=40
X_LEFT_SIDE_BASE = 25
X_LEFT_SIDE_FIELD = X_LEFT_SIDE_BASE + 30

def y_location(gap):
    location = int(Y_BASE + 40 * gap)
    return location

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
n = 6
MyTitle(X_LEFT_SIDE_BASE, y_location(n), 'EXPERIENCE')

X_LEFT_SIDE_FIELD_2nd = X_LEFT_SIDE_FIELD + 300
X_LEFT_SIDE_BASE_2nd = X_LEFT_SIDE_BASE + 300
for key in db["experience"]:
    MyTextLine(X_LEFT_SIDE_FIELD, y_location(n+1), 'long', 'experience', key, 'title')
    MyButton(X_LEFT_SIDE_BASE, y_location(n+1), cv.dic['experience'][key]['title'])
    
    MyTextLine(X_LEFT_SIDE_FIELD_2nd, y_location(n+1), 'date', 'experience', key, 'from')
    MyButton(X_LEFT_SIDE_BASE_2nd, y_location(n+1), cv.dic['experience'][key]['from'])

    MyTextLine(X_LEFT_SIDE_FIELD, y_location(n+2), 'long', 'experience', key, 'company')
    MyButton(X_LEFT_SIDE_BASE, y_location(n+2), cv.dic['experience'][key]['company'])
    
    MyTextLine(X_LEFT_SIDE_FIELD_2nd, y_location(n+2), 'date', 'experience', key, 'to')
    MyButton(X_LEFT_SIDE_BASE_2nd, y_location(n+2), cv.dic['experience'][key]['to'])

    MyTextField(X_LEFT_SIDE_FIELD, y_location(n+3), 'job_description', 'experience', key, 'description')
    MyButton(X_LEFT_SIDE_BASE, y_location(n+3), cv.dic['experience'][key]['description'])

    n += 9

window_widgets_height = y_location(n + 1)


# CONTACTS
PUSH = 60
X_RIGHT_SIDE_BASE = X_LEFT_SIDE_BASE + cv.INTRO_AND_JOBDESC_WIDTH + PUSH
X_RIGHT_SIDE_FIELD = X_LEFT_SIDE_FIELD + cv.INTRO_AND_JOBDESC_WIDTH + PUSH

MyTitle(X_RIGHT_SIDE_BASE, y_location(0), 'CONTACTS')

n = 1
for key in db["contacts"]:
    MyTextLine(X_RIGHT_SIDE_FIELD, y_location(n), 'long', 'contacts', key)
    MyButton(X_RIGHT_SIDE_BASE, y_location(n), cv.dic['contacts'][key])
    n += 1


# EDUCATION
MyTitle(X_RIGHT_SIDE_BASE, y_location(n), 'EDUCATION')

PUSH_DATE = 150
X_RIGHT_SIDE_BASE_2nd = X_RIGHT_SIDE_BASE + PUSH_DATE
X_RIGHT_SIDE_FIELD_2nd = X_RIGHT_SIDE_FIELD + PUSH_DATE
for key in db["education"]:
    MyTextLine(X_RIGHT_SIDE_FIELD, y_location(n+1), 'long', 'education', key, 'school')
    MyButton(X_RIGHT_SIDE_BASE, y_location(n+1), cv.dic['education'][key]['school'])
    
    MyTextLine(X_RIGHT_SIDE_FIELD, y_location(n+2), 'long', 'education', key, 'subject')
    MyButton(X_RIGHT_SIDE_BASE, y_location(n+2), cv.dic['education'][key]['subject'])

    MyTextLine(X_RIGHT_SIDE_FIELD, y_location(n+3), 'date', 'education', key, 'from')
    MyButton(X_RIGHT_SIDE_BASE, y_location(n+3), cv.dic['education'][key]['from'])
    
    MyTextLine(X_RIGHT_SIDE_FIELD_2nd, y_location(n+3), 'date', 'education', key, 'to')
    MyButton(X_RIGHT_SIDE_BASE_2nd, y_location(n+3), cv.dic['education'][key]['to'])
    
    if key != list(db["education"])[-1]:
        n += 3.2

# SKILLS
n += 3
MyTitle(X_RIGHT_SIDE_BASE, y_location(n+1), 'SKILLS')
MyTextField(X_RIGHT_SIDE_FIELD, y_location(n+2), 'bulk', 'mixed', 'skills')
MyButton(X_RIGHT_SIDE_BASE, y_location(n+2), cv.dic['mixed']['skills'])
b_sep = MyButton(X_RIGHT_SIDE_BASE, y_location(n+3), cv.dic['mixed']['skills'])
b_sep.clicked.connect(lambda: b_sep.copy_skills_separately())


# ACHIEVEMENTS
n += 7.5
MyTitle(X_RIGHT_SIDE_BASE, y_location(n), 'ACHIEVEMENTS')
MyTextField(X_RIGHT_SIDE_FIELD, y_location(n+1), 'bulk_tall', 'mixed', 'achievements')
MyButton(X_RIGHT_SIDE_BASE, y_location(n+1), cv.dic['mixed']['achievements'])


# EXTRA
n += 9.5
MyTitle(X_RIGHT_SIDE_BASE, y_location(n), 'EXTRA')
MyTextField(X_RIGHT_SIDE_FIELD, y_location(n+1), 'bulk_tall', 'mixed', 'extra')
MyButton(X_RIGHT_SIDE_BASE, y_location(n+1), cv.dic['mixed']['extra'])


# SAVE
MySaveButton(cv.WINDOW_WIDTH - 105, 20, 60, 30)


window_main.resize(cv.WINDOW_WIDTH, cv.WINDOW_HEIGHT)
cv.window_widgets.resize(cv.WINDOW_WIDTH, window_widgets_height)

window_main.setWidget(cv.window_widgets)
window_main.show()

sys.exit(app.exec())