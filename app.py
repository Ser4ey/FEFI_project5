import sys

from PyQt6.QtWidgets import QApplication
from UI.uimain import UIMain

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UIMain()
    sys.exit(app.exec())
