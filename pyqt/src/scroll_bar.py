from PyQt6.QtWidgets import QScrollBar


class MyScrollBar():
    def __init__(self, window):
        vertical = ScrollBarVer()
        horizontal = ScrollBarHor()
        window.setVerticalScrollBar(vertical)
        window.setHorizontalScrollBar(horizontal)



class ScrollBarVer(QScrollBar):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(
                            "QScrollBar::vertical"
                                "{"
                                "width: 10px;"
                                "}"
                            )



class ScrollBarHor(QScrollBar):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(
                            "QScrollBar::horizontal"
                                "{"
                                "height: 10px;"
                                "}"
                            )
    

        