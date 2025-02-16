import sys

from PySide6 import QtGui
from PySide6.QtGui import QPalette, Qt
from PySide6.QtWidgets import QApplication

from utils.environment import Environment
from view.screen_login import ScreenLogin

app = QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon(Environment.resource_path('static/images/icon.png')))

# Set light mode
palette = QPalette()
# noinspection PyUnresolvedReferences
palette.setColor(QPalette.Window, Qt.white)
# noinspection PyUnresolvedReferences
palette.setColor(QPalette.WindowText, Qt.black)
# noinspection PyUnresolvedReferences
palette.setColor(QPalette.Base, Qt.white)
# noinspection PyUnresolvedReferences
palette.setColor(QPalette.AlternateBase, Qt.lightGray)
# noinspection PyUnresolvedReferences
palette.setColor(QPalette.ToolTipBase, Qt.white)
# noinspection PyUnresolvedReferences
palette.setColor(QPalette.ToolTipText, Qt.black)
# noinspection PyUnresolvedReferences
palette.setColor(QPalette.Text, Qt.black)
# noinspection PyUnresolvedReferences
palette.setColor(QPalette.Button, Qt.lightGray)
# noinspection PyUnresolvedReferences
palette.setColor(QPalette.ButtonText, Qt.black)
# noinspection PyUnresolvedReferences
palette.setColor(QPalette.BrightText, Qt.red)
# noinspection PyUnresolvedReferences
palette.setColor(QPalette.Highlight, Qt.blue)
app.setPalette(palette)
app.setStyleSheet("""
    QMenu {
        background-color: #f9f9f9;
        color: black;
        padding: 0px 0px 0px 0px;
        font-size: 16px;
        border-width: 0 0 1px;
    }
    QMenu::item:selected {
        background-color: darkgray;
    }
    QMenu::item {
        padding: 2px 20px 2px 20px;
        margin: 0px 0px 0px 0px;
        font-size: 16px;
    }
    QMenuBar {
        background-color: #f9f9f9;
        font-size: 17px;
    }
    QMenuBar::item {
        background-color: #f9f9f9;
        color: black;
    }
    QMenuBar::item:selected {
        background-color: darkgray;
    }
    QTableWidget::item:selected {
        background-color: #dddddd;
        color: #000000;
    }
""")
login_screen = ScreenLogin()
login_screen.show()
app.exec()
