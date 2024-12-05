from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import QWidget, QSizePolicy, QVBoxLayout
from PySide6.QtCore import Signal


class ButtonUndo(QWidget):
    clicked = Signal()
    def __init__(self, foo_to_execute):
        super().__init__()
        # noinspection PyUnresolvedReferences
        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.setObjectName("ButtonUndo")
        self.clicked.connect(foo_to_execute)

        self.setStyleSheet("""
            #ButtonUndo {
                background-color: #e9e9e9; 
                border: 1px solid #b0b0b0;  
                padding: 8px;
                border-radius: 5px;
                font-weight: bold;
                font-size: 13px;
            }
            #ButtonUndo:hover {
                background-color: #d0d0d0; 
            }
            #ButtonUndo:pressed {
                background-color: #bfbfbf;  
            }
        """)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        svg_img = QSvgWidget('static/images/undo.svg')
        svg_img.setFixedSize(50, 50)
        self.layout.addWidget(svg_img)

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)
