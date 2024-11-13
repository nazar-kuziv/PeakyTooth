from PySide6.QtWidgets import QPushButton


class ButtonBase(QPushButton):
    def __init__(self, text: str = ''):
        super().__init__(text)
        self.setStyleSheet("""
            QPushButton {
                background-color: #e9e9e9; 
                border: 1px solid #b0b0b0;  
                padding: 8px;
                border-radius: 5px;
                font-weight: bold;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: #d0d0d0; 
            }
            QPushButton:pressed {
                background-color: #bfbfbf;  
            }
        """)
